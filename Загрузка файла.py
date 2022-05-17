from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    name = browser.find_element_by_name("firstname")
    name.send_keys("Nikolai")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Galich")
    email = browser.find_element_by_name("email")
    email.send_keys("galich_87@mail.ru")
    
    directory = "C:/Selenium_Python/readme.txt"
    add_file = browser.find_element_by_id("file")
    add_file.send_keys(directory)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
        
finally:
    time.sleep(10)
    browser.quit()
        