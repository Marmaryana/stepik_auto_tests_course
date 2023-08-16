from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_addbutton_on_page(browser):
    browser.get(link)
    button = browser.find_elements(By.CLASS_NAME, "add-to-basket")
    assert button, "No button found"
    time.sleep(10)

