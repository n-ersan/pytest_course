import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium import Faker 

fake = Faker()
driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def test_login_positive():
    driver.get('https://www.saucedemo.com/') 
    username = driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys('standard_user')
    password = driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys('secret_sauce')
    login_button = driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()
    time.sleep(3) 

def test_login_negative():
    driver.get('https://www.saucedemo.com/') 
    username = driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys('user')
    password = driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys('user')
    login_button = driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()
    time.sleep(3)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', "Login failed. Please try again."
    
def test_add_to_cart(test_login_positive):
    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(6)

def test_if_item_in_the_cart(test_login_positive):
    driver.get('https://www.saucedemo.com/cart.html')
    try:
        item_in_the_cart = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']")
    except NoSuchElementException:
        print("Item is not present in the cart.")
    return True 

def test_delete_item_in_the_cart(test_login_positive):
    driver.get('https://www.saucedemo.com/cart.html')
    remove_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]').click()
    time.sleep(3)
    
    
def test_if_item_was_removed(test_login_positive):
    driver.get('https://www.saucedemo.com/cart.html') 
    try:
        driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']")
        print("Item was not removed") 
    except NoSuchElementException:
        print("Item was successfully removed")

# Добавление товара в корзину из карточки товара
def test_add_item_from_product_page(test_login_positive):
    product_page = driver.get(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')
    add_to_cart_button = driver.get(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    time.sleep(4)
    add_to_cart_button.click()
    time.sleep(4) 

#def test_if_item_in_the_cart(test_login_positive):
#    driver.get('https://www.saucedemo.com/cart.html') 
#    try:
#        item_in_the_cart = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']")
#    except NoSuchElementException:
#        print("Item is not present in the cart.")
#    return True 

# Оформление заказа используя корректные данные
def test_add_to_cart(test_login_positive):
    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.get('https://www.saucedemo.com/cart.html')
    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="checkout"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-test="firstName"]').send_keys(fake.name)
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-test="lastName"]').send_keys(fake.lastname)
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-test="postalCode"]').send_keys(fake.)
    time.sleep(2)
    continue_button = driver.find_element(By.XPATH, '//input[@data-test="continue"]').click()
    time.sleep(2)
    finish_button = driver.find_element(By.XPATH, '//button[@data-test="finish"]').click()
    time.sleep(2)

# роверка работоспособности фильтра (A to Z)
def test_filtr_button(test_login_positive):
    filtr_button = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]').click()







