from CartPage.add_to_cart import AddToCart
from HomePage.verify_product import verification
from Login.invalidLogin import InvalidLog


def test_valid1(seconddriver, valid_login):
    pass

def test_invalid(seconddriver):
    neg_logged_in=InvalidLog(seconddriver)
    neg_logged_in.neg_username("locked_out_user")
    neg_logged_in.neg_password("secret_sauce")
    neg_logged_in.neg_login()

def test_sorting(seconddriver, valid_login):
    sorting=verification(seconddriver)
    sorting.sorting("Price (low to high)")

def test_add_to_cart(seconddriver, valid_login):
    add=AddToCart(seconddriver)
    add.add_to_cart(2)
    add.check_badge(2)





