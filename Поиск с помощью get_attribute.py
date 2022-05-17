from selenium import webdriver
import time
import math

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)
    
    treasure_x = browser.find_element_by_id("treasure")
    treasure_value = treasure_x.get_attribute("valuex")
    x = treasure_value
    y = calc(x)
    
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()    

finally:
    time.sleep(10)
    browser.quit()