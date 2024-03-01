from evm_wallet import Chains
from evm_wallet import Coin
from evm_wallet.coins import BNB
from evm_wallet import Wallet
from evm_wallet import W3Transactor
from evm_wallet import W3Error

from evm_bridger.contracts import BridgerContract
from evm_bridger.contracts import OPBNBBridge
from evm_bridger.contracts import Bungee

import random


class Bridger(W3Transactor):

    chain: Chains
    wallet: Wallet
    contract: BridgerContract

    def __init__(self, contract: BridgerContract):
        self.contract = contract
        self.wallet = contract.wallet
        self.chain = contract.wallet.chain

        if not contract.is_chain_available(self.chain):
            raise W3Error(
                f'This chain is not available in this protocol'
            )

    async def bridge(self, token: Coin, chain_to: Chains, amount):

        if not self.contract.is_chain_available(chain_to):
            raise W3Error(
                f'This chain is not available in this protocol'
            )

        self.wallet.logger.info(f"[Bridger] [{self.wallet.address}] Start bridge {amount} of {token.__class__.__name__} "
                                f"from {self.chain} to {chain_to} by {self.contract.__class__.__name__}")

        token_to_bridge = self.wallet.web3.to_checksum_address(token.get_address())
        self.check_gas()

        amount_wei = self.wallet.get_amount_wei(token_to_bridge, amount)
        self.approve_token_if_need(token, amount_wei, self.contract.router_address)

        txn = self.contract.get_transaction(token_to_bridge, chain_to, amount_wei)
        tx_hex = await self.wallet.sigh_transaction(txn)

        self.wallet.logger.success(f"[Bridger] [{self.wallet.address}] Transaction send succeed "
                                   f"{self.chain.get_scan_url()}{tx_hex}")
        return tx_hex

    @staticmethod
    async def __refill_opbnb_gas__(wallet: Wallet,amount=0):

        try:
            wallet = Wallet(Chains.OPBNB, wallet.private_key)

            balance_op_bnb = wallet.get_balance()
            if balance_op_bnb['balance'] > 0.005:
                wallet.logger.info(f"[Bridger] [{wallet.address}] Already have enough op_bnb {balance_op_bnb['balance']}")
                return

            wallet = Wallet(Chains.BSC, wallet.private_key)
            balance_bnb = wallet.get_balance()
            if balance_bnb['balance'] < 0.0007:
                raise W3Error(f"[Bridger] [{wallet.address}] Balance of bnb is too low {balance_bnb['balance']}")

            bridger = Bridger(OPBNBBridge(wallet))

            if amount == 0:
                amount = random.randint(20, 30)

            await bridger.bridge(BNB(Chains.BSC), Chains.OPBNB, amount / 10000)

        except W3Error as e:
            wallet.logger.error(e.msg)

    @staticmethod
    async def __refill_chain_gas__(wallet: Wallet, chain_from: Chains, chain_to: Chains,amount=0):

        try:
            wallet = Wallet(chain_to, wallet.private_key)

            balance_gas = wallet.get_balance()
            if balance_gas['balance'] > chain_to.get_min_gas()*5:
                wallet.logger.info(
                    f"[Bridger] [{wallet.address}] Already have enough {chain_to.name} {balance_gas['balance']}")
                return

            wallet = Wallet(chain_from, wallet.private_key)
            balance_from = wallet.get_balance()

            if amount == 0:
                amount = random.randint(10, 20)
                amount_to_send = amount * chain_from.get_min_gas()
            else:
                amount_to_send = amount

            if balance_from['balance'] < (amount_to_send + chain_from.get_min_gas()):
                raise W3Error(f"[Bridger] [{wallet.address}] Balance of {chain_from.name} is too low "
                              f"{balance_from['balance']} need {amount_to_send}")

            bridger = Bridger(Bungee(wallet))
            await bridger.bridge(chain_from.get_main_coin(), chain_to, amount_to_send)

        except W3Error as e:
            wallet.logger.error(e.msg)

    @staticmethod
    async def refill_chain_gas(wallet: Wallet, chain_from: Chains, chain_to: Chains, amount=0):

        if chain_from.name == Chains.BSC.name and chain_to.name == Chains.OPBNB.name:
            await Bridger.__refill_opbnb_gas__(wallet, amount)
        else:
            await Bridger.__refill_chain_gas__(wallet, chain_from, chain_to, amount)
