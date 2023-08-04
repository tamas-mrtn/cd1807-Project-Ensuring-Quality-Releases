#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging 

log = logging.getLogger(__name__)

def login(driver, user, password):
    url = 'https://www.saucedemo.com/'
    log.info(f'Login to URL: {url}...')
    try:
        driver.get(url)
        driver.find_element("id", "user-name").send_keys(user)
        driver.find_element("id", "password").send_keys(password)
        driver.find_element("id", "login-button").click()
        log.info(f'Login with username {user} and password {password} successful!')
    except:
        log.error(f'Login failed!')
        raise


def add_items_to_cart(driver):
    cart = []

    log.info('Add all items to the cart...')

    items = driver.find_elements(By.CLASS_NAME,"inventory_item")
    for item in items:
        item_name = item.find_element(By.CLASS_NAME,"inventory_item_name").text
        cart.append(item_name)
        item.find_element(By.CLASS_NAME,"btn_inventory").click()
        log.info(f'Added item: {item_name}')
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    log.info("All Items were added to shopping cart!")

def remove_items_to_cart(driver):
    log.info('Start removing items from cart...')
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click() 
    cart_items = len(driver.find_elements(By.CLASS_NAME,"cart_item"))

    log.info(f"Number of items in the cart = {cart_items}")

    for item in driver.find_elements(By.CLASS_NAME,"cart_item"):
        item_name = item.find_element(By.CLASS_NAME,"inventory_item_name").text
        item.find_element(By.CLASS_NAME,"cart_button").click()
        log.info(f'Removed {item_name}')

    log.info(f"{cart_items} Items are all removed from shopping cart.")
    

def run_tests():
    """Run the test"""
    log.info("Starting the browser...")
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")  
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=options)
    log.info('Starting the browser...')
    login(driver, "standard_user", "secret_sauce")
    add_items_to_cart(driver)
    remove_items_to_cart(driver)
    log.info("Tests Completed")

if __name__ == "__main__":
    run_tests()