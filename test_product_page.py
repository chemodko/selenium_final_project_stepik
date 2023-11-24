from .pages.product_page import ProductPage
import time
import pytest


# link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

xfail_num = 7
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [product_base_link + str(num) for num in range(10) if num != xfail_num]
xlink = pytest.param(product_base_link + str(xfail_num), marks=pytest.mark.xfail(reason="mistake on page"))
links.insert(xfail_num, xlink)


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.solve_quiz_and_get_code()

    page.should_be_product_name()
    page.should_be_product_name_after_adding()
    page.should_be_equal_names()
    page.should_be_equal_prices()

    # page.should_disappear_message()

    # time.sleep(10)


link_global = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"


@pytest.mark.xfail(reason="There should be success message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_global, 0)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_global, 0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Message should not disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_global, 0)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.should_disappear_message()


@pytest.mark.login_test
def test_guest_should_see_login_link_on_product_page(browser):
    local_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, local_link, 0)
    page.open()
    page.should_be_login_link()


@pytest.mark.login_test
def test_guest_can_go_to_login_page_from_product_page(browser):
    local_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, local_link, 0)
    page.open()
    page.go_to_login_page()

