from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Имя")
    browser.find_element(By.NAME, "lastname").send_keys("Фамилия")
    browser.find_element(By.NAME, "email").send_keys("email@example.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    with open(file_path, 'w') as file:
        file.write("Тестовый файл")

    file_element = browser.find_element(By.ID, "file")
    file_element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
