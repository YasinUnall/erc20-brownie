from scripts.helpful_scripts import get_account
from brownie import config, network, OurToken, accounts
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy_token():
    account = get_account()
    token = OurToken.deploy(initial_supply, {"from": account}, publish_source=False)
    print(token.address)


def main():
    deploy_token()
