from Pages.LoginPg import LoginPg
from Pages.InvalidLogin import InvalidLogin



def test_valid_login(driver):
    logged_in = LoginPg(driver)
    logged_in.username("tomsmith")
    logged_in.password("SuperSecretPassword!")
    logged_in.click_login()
def test_invalid_login(driver):
    negative_test = InvalidLogin(driver)
    negative_test.neg_username("TomSmith")
    negative_test.neg_password("SuperSecret!")
    negative_test.neg_click_login()