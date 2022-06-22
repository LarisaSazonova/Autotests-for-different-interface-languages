from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

def test_add_to_basket_button_available(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(10)

    elements = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")

    assert elements is not None, "Didn't find 'Add to basket' button"

