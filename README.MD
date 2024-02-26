# EVM_Bridger

Module to bridge with EVM web3 wallets

## Bridge coins

    from evm_bridger import Bridger
    from evm_bridger import Bungee
    from evm_wallet import W3Error

    try:
        bridger = Bridger(Bungee(wallet))
        bridger.bridge(ETH(chain), Chains.POLYGON, 0.0001)
    except W3Error as e:
        wallet.logger.error(e.msg)

##  Bridge Gas to chain

    from evm_bridger import Bridger
    from evm_wallet import Chains

    Bridger.refill_chain_gas(wallet, Chains.BSC, Chains.OPBNB)