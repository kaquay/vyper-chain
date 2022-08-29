from brownie import accounts, config, TokenERC20
from scripts.helpful_scripts import get_account


initial_supply = 1000000000000000000000  # 1000
token_name = "KQToken"
token_symbol = "KQt"


def main():
    account = get_account()
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}
    )