from allure_commons._allure import step
from selene import browser, have, be
import allure
from methods.add_to_cart_api import add_to_cart


@allure.tag("web")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Добавление товаров в корзину")
@allure.story("Успешное добавление товара в корзину")
def test_successful_add_to_cart(base_url):
    with step("Добавить товар в корзину через API"):
        response = add_to_cart(base_url + '/addproducttocart/details/13/1',
                               data = {"addtocart_13.EnteredQuantity": 1})
    with step("Получить куки сессии"):
        cookie = response.cookies.get("Nop.customer")
    with step("Проверить, что в корзину добавлен товар"):
        browser.open('')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
        browser.driver.refresh()
        browser.open('/cart')
        browser.element('.order-summary-content .cart').should(be.present)


@allure.tag("web")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Добавление товаров в корзину")
@allure.story("Успешное добавление товаров в корзину меняет счетчик корзины в хэдере")
def test_successful_add_to_cart_change_counter_in_header(base_url):
    with step("Добавить 2 товара в корзину через API"):
        response = add_to_cart(base_url + '/addproducttocart/details/13/1',
                               data = {"addtocart_13.EnteredQuantity": 2})
    with step("Получить куки сессии"):
        cookie = response.cookies.get("Nop.customer")
    with step("Проверить, что счетчик у корзины в хэдере отображает кол-во добавленных товаров"):
        browser.open('')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
        browser.driver.refresh()
        browser.element('#topcartlink .cart-qty').should(have.text('(1)'))


@allure.tag("web")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Добавление товаров в корзину")
@allure.story("Не успешное добавление товара в корзину")
def test_not_successful_add_to_cart(base_url):
    with step("Добавить без заполнения обязательных полей"):
        response = add_to_cart(base_url + '/addproducttocart/details/1/1',
                               data = {"addtocart_13.EnteredQuantity": 1})
    with step("Получить куки сессии"):
        cookie = response.cookies.get("Nop.customer")
    with step("Проверить, что в корзине не добавлен товар"):
        browser.open('')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
        browser.driver.refresh()
        browser.open('/cart')
        browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))
