from selenium import webdriver
import time
import math

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)
    
    num_x = browser.find_element_by_id("input_value")
    num_value = num_x.text
    x = num_value
    y = calc(x)
    
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click() 

finally:
    time.sleep(10)
    browser.quit()