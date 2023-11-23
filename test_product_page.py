from .pages.product_page import ProductPage
import time


link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.solve_quiz_and_get_code()

    page.should_be_product_name()
    page.should_be_product_name_after_adding()
    page.should_be_equal_names()
    page.should_be_equal_prices()

    # time.sleep(10)



