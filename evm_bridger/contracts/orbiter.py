from evm_wallet import Chains
from evm_bridger.contracts import BridgerContract


class Orbiter(BridgerContract):

    router_address = "0x80C67432656d59144cEFf962E8fAF8926599bCF8"
    router_abi = ""

    def is_chain_available(self, chain: Chains):
        if (chain == Chains.POLYGON or chain == Chains.OPTIMISM or chain == Chains.BSC or chain == Chains.BASE or
                chain == Chains.ARBITRUM or chain == Chains.AVALANCHE or chain == Chains.ZKSYNC):
            return True
        else:
            return False

    def get_transaction(self, token, chain_to: Chains, amount):

        tx_data = self.wallet.get_trans_options(amount)
        tx_data.update({"to": self.wallet.web3.to_checksum_address(self.router_address)})

        tx_hex = self.wallet.sigh_transaction(tx_data)
        return tx_hex
