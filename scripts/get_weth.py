from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depositing ETH
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    # converting value into weth
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    print(f"Recieved 0.1 WETH")
    return tx
