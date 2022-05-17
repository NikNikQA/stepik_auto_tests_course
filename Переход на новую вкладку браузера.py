from selenium import webdriver
import time
import math

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    trollface = browser.find_element_by_class_name("trollface.btn.btn-primary")
    trollface.click()
    
    new_window = browser.window_handles[1] 
    # Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
    # first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    
    num_x = browser.find_element_by_id("input_value")
    num_value = num_x.text
    x = num_value
    y = calc(x)
    
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()    

finally:
    time.sleep(10)
    browser.quit