from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("num1")
    num_x = x.text
    
    y = browser.find_element_by_id("num2")
    num_y = y.text
    
    sum = (int(num_x) + int(num_y))
    strsum = str(sum)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(strsum)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()    


finally:
    time.sleep(5)
    browser.quit()