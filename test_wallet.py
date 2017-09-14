##lessons 2 pytesting

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Return a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    #wallet = Wallet()
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    #wallet = Wallet(100)
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    #wallet = Wallet(10)
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    #wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    #wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)
