from data.credentials import Credentials
from pages.login.login import LoginPage
from pages.products_to_cart.prodeucts_to_cart import ProductsToCart
from pages.delete_cart_products.delete_cart_products import DeleteCartProduct
from pages.checkout.checkout import Checkout


class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsToCart(self.driver)
        self.delete_cart_products = DeleteCartProduct(self.driver)
        self.checkout = Checkout(self.driver)
