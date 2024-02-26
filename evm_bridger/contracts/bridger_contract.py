from evm_wallet import Chains
from evm_wallet import Wallet


class BridgerContract:

    router_address = ""
    router_abi = ""

    fee = 3000
    slippage = 0.01

    def __init__(self, wallet: Wallet):
        self.wallet = wallet
        self.contract = wallet.web3.eth.contract(address=wallet.web3.to_checksum_address(self.router_address),
                                                 abi=self.router_abi)

    def is_chain_available(self, chain: Chains):
        pass

    def get_transaction(self, token, chain_to: Chains, amount):
        pass
