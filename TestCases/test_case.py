from CartPage.add_to_cart import AddToCart
from HomePage.verify_product import verification
from Login.invalidLogin import InvalidLog
from CheckOut.checkingOut import Checkout
from LogOut.loggingOut import Logouts


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
    add=AddToCart(seconddriver)
    #add.sort_products()
    add.get_all_prices()
    add.add_to_cart(3)
    add.cart()
    check = Checkout(seconddriver)
    check.click_checkout()
    check.name_input()
    check.surname_input()
    check.code()
    check.continue_click()
    check.click_finish()
    submit = Logouts(seconddriver)
    submit.click_back_to_home()
    submit.click_menu()
    submit.click_logout()




