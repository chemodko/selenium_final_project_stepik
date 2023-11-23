from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button is not presented"

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_name_after_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name after adding is not presented"

    def get_product_name_after_adding(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING).text

    def should_be_equal_names(self):
        name = self.get_product_name()
        name_after_add = self.get_product_name_after_adding()
        assert name == name_after_add, "Names are not equal"

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_cart_price(self):
        return self.browser.find_element(*ProductPageLocators.CART_PRICE).text

    def should_be_equal_prices(self):
        prod_price = self.get_product_price()
        cart_price = self.get_cart_price()
        assert prod_price == cart_price, "Prices are not equal"



