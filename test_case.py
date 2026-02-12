from CartPage.add_to_cart import AddToCart


#def test_valid1(driver, valid_login):
 #   pass

#def test_invalid(driver):
 #   neg_logged_in=InvalidLog(driver)
  #  neg_logged_in.neg_username("locked_out_user")
   # neg_logged_in.neg_password("secret_sauce")
    #neg_logged_in.neg_login()

#def test_sorting(driver, valid_login):
 #   sorting=verification(driver)
  #  sorting.sorting("Price (low to high)")

def test_add_to_cart(driver, valid_login):
    add=AddToCart(driver)
    add.add_to_cart(2)
    add.check_badge(2)





