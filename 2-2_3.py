from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# print(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# print(os.path.abspath(os.path.dirname(__file__)))
# element.send_keys(file_path)

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "lastname")
    input1.send_keys("Volkov")
    input2 = browser.find_element(By.NAME, "firstname")
    input2.send_keys("Peter")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("123@321.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
