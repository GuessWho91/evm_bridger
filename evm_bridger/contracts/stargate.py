from evm_bridger.contracts import BridgerContract
from evm_wallet import Chains


def get_bridge_address(chain: Chains):
    if chain == Chains.POLYGON:
        return "0x9d1B1669c73b033DFe47ae5a0164Ab96df25B944"
    elif chain == Chains.OPTIMISM:
        return "0x701a95707A0290AC8B90b3719e8EE5b210360883"
    elif chain == Chains.BSC:
        return "0x6694340fc020c5E6B96567843da2df01b2CE1eb6"
    elif chain == Chains.ARBITRUM:
        return "0x352d8275AAE3e0c2404d9f68f6cEE084B5bEB3DD"
    elif chain == Chains.AVALANCHE:
        return "0x9d1B1669c73b033DFe47ae5a0164Ab96df25B944"

    return "0x296F55F8Fb28E498B858d0BcDA06D955B2Cb3f97"


def get_router_address(chain: Chains):
    if chain == Chains.POLYGON:
        return "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd"
    elif chain == Chains.OPTIMISM:
        return "0xB0D502E938ed5f4df2E681fE6E419ff29631d62b"
    elif chain == Chains.BSC:
        return "0x4a364f8c717cAAD9A442737Eb7b8A55cc6cf18D8"
    elif chain == Chains.ARBITRUM:
        return "0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614"
    elif chain == Chains.AVALANCHE:
        return "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd"

    return "0x8731d54E9D02c286767d56ac03e8037C07e01e98"


class Stargate(BridgerContract):

    SLIPPAGE = 1

    router_abi = '[{"inputs":[{"internalType":"address","name":"_layerZeroEndpoint","type":"address"},{"internalType":"address","name":"_router","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"msgType","type":"uint8"},{"indexed":false,"internalType":"uint64","name":"nonce","type":"uint64"}],"name":"SendMsg","type":"event"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approveTokenSpender","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"bridgeLookup","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"forceResumeReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint8","name":"","type":"uint8"}],"name":"gasLookup","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"layerZeroEndpoint","outputs":[{"internalType":"contract ILayerZeroEndpoint","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"lzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint8","name":"_functionType","type":"uint8"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"bytes","name":"_transferAndCallPayload","type":"bytes"},{"components":[{"internalType":"uint256","name":"dstGasForCall","type":"uint256"},{"internalType":"uint256","name":"dstNativeAmount","type":"uint256"},{"internalType":"bytes","name":"dstNativeAddr","type":"bytes"}],"internalType":"struct IStargateRouter.lzTxObj","name":"_lzTxParams","type":"tuple"}],"name":"quoteLayerZeroFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"components":[{"internalType":"uint256","name":"credits","type":"uint256"},{"internalType":"uint256","name":"idealBalance","type":"uint256"}],"internalType":"struct Pool.CreditObj","name":"_c","type":"tuple"},{"internalType":"uint256","name":"_amountSD","type":"uint256"},{"internalType":"bytes","name":"_to","type":"bytes"},{"components":[{"internalType":"uint256","name":"dstGasForCall","type":"uint256"},{"internalType":"uint256","name":"dstNativeAmount","type":"uint256"},{"internalType":"bytes","name":"dstNativeAddr","type":"bytes"}],"internalType":"struct IStargateRouter.lzTxObj","name":"_lzTxParams","type":"tuple"}],"name":"redeemLocal","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"components":[{"internalType":"uint256","name":"credits","type":"uint256"},{"internalType":"uint256","name":"idealBalance","type":"uint256"}],"internalType":"struct Pool.CreditObj","name":"_c","type":"tuple"},{"components":[{"internalType":"uint256","name":"dstGasForCall","type":"uint256"},{"internalType":"uint256","name":"dstNativeAmount","type":"uint256"},{"internalType":"bytes","name":"dstNativeAddr","type":"bytes"}],"internalType":"struct IStargateRouter.lzTxObj","name":"_lzTxParams","type":"tuple"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"redeemLocalCallback","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"router","outputs":[{"internalType":"contract Router","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"components":[{"internalType":"uint256","name":"credits","type":"uint256"},{"internalType":"uint256","name":"idealBalance","type":"uint256"}],"internalType":"struct Pool.CreditObj","name":"_c","type":"tuple"}],"name":"sendCredits","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"bytes","name":"_bridgeAddress","type":"bytes"}],"name":"setBridge","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint256","name":"_configType","type":"uint256"},{"internalType":"bytes","name":"_config","type":"bytes"}],"name":"setConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint8","name":"_functionType","type":"uint8"},{"internalType":"uint256","name":"_gasAmount","type":"uint256"}],"name":"setGasAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"version","type":"uint16"}],"name":"setReceiveVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"version","type":"uint16"}],"name":"setSendVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"enable","type":"bool"}],"name":"setUseLayerZeroToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"components":[{"internalType":"uint256","name":"credits","type":"uint256"},{"internalType":"uint256","name":"idealBalance","type":"uint256"}],"internalType":"struct Pool.CreditObj","name":"_c","type":"tuple"},{"components":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"eqFee","type":"uint256"},{"internalType":"uint256","name":"eqReward","type":"uint256"},{"internalType":"uint256","name":"lpFee","type":"uint256"},{"internalType":"uint256","name":"protocolFee","type":"uint256"},{"internalType":"uint256","name":"lkbRemove","type":"uint256"}],"internalType":"struct Pool.SwapObj","name":"_s","type":"tuple"},{"components":[{"internalType":"uint256","name":"dstGasForCall","type":"uint256"},{"internalType":"uint256","name":"dstNativeAmount","type":"uint256"},{"internalType":"bytes","name":"dstNativeAddr","type":"bytes"}],"internalType":"struct IStargateRouter.lzTxObj","name":"_lzTxParams","type":"tuple"},{"internalType":"bytes","name":"_to","type":"bytes"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"swap","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"useLayerZeroToken","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
    bridge_abi = '[{"inputs":[{"internalType":"address","name":"_stargateEthVault","type":"address"},{"internalType":"address","name":"_stargateRouter","type":"address"},{"internalType":"uint16","name":"_poolId","type":"uint16"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"addLiquidityETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"poolId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stargateEthVault","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stargateRouter","outputs":[{"internalType":"contract IStargateRouter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"uint256","name":"_amountLD","type":"uint256"},{"internalType":"uint256","name":"_minAmountLD","type":"uint256"}],"name":"swapETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"components":[{"internalType":"uint256","name":"amountLD","type":"uint256"},{"internalType":"uint256","name":"minAmountLD","type":"uint256"}],"internalType":"struct RouterETH.SwapAmount","name":"_swapAmount","type":"tuple"},{"components":[{"internalType":"uint256","name":"dstGasForCall","type":"uint256"},{"internalType":"uint256","name":"dstNativeAmount","type":"uint256"},{"internalType":"bytes","name":"dstNativeAddr","type":"bytes"}],"internalType":"struct IStargateRouter.lzTxObj","name":"_lzTxParams","type":"tuple"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"swapETHAndCall","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

    def __init__(self, wallet):
        self.router_address = get_router_address(wallet.chain)
        self.bridge_address = get_bridge_address(wallet.chain)
        super().__init__(wallet)

    def is_chain_available(self, chain: Chains):
        if (chain == Chains.BSC or chain == Chains.OPTIMISM or chain == Chains.ETHEREUM
                or chain == Chains.ARBITRUM or chain == Chains.POLYGON):
            return True
        else:
            return False

    def get_l0_fee(self, chain_to: Chains):
        contract = self.wallet.web3.eth.contract(address=self.router_address, abi=self.router_abi)

        fee = contract.functions.quoteLayerZeroFee(
            chain_to.value,
            1,
            self.wallet.address,
            "0x",
            {
                'dstGasForCall': 0,
                'dstNativeAmount': 0,
                'dstNativeAddr': "0x"
            }
        ).call()

        return int(fee[0] * 1.1)

    def get_transaction(self, token, chain_to: Chains, amount):

        l0_fee = self.get_l0_fee(chain_to)
        tx_data = self.wallet.get_trans_options(amount + l0_fee)

        contract = self.wallet.web3.eth.contract(address=self.bridge_address, abi=self.bridge_abi)
        transaction = contract.functions.swapETH(
            self.wallet.chain.value,
            self.wallet.address,
            self.wallet.address,
            amount,
            int(amount - (amount / 100 * self.SLIPPAGE))
        ).build_transaction(tx_data)

        return transaction
