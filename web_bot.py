from selenium import webdriver
import time


#prompts
# name = input(str("What is your first and last name?"))
# first_name = name.split()[0]
# last_name = name.split()[1]
# message = input(str("What message do you want to say?"))

# code
driver = webdriver.Chrome()
driver.get('https://www.zola.com/registry/henryandryann')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="root"]/div[1]/section[4]/div/div[2]/div/div[2]/div[1]/div/span/button[1]/div').click()
time.sleep(2)
driver.find_element_by_id('bx-close-inside-1260082').click()
driver.find_element_by_id('cart-checkout-button').click()
text_box = driver.find_element_by_class_name('form-control ng-pristine ng-valid ng-valid-maxlength ng-touched')
text_box.send_keys('Merry Christmas! Love you guys!')
