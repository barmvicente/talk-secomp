from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.google.com.br/')
driver.find_element_by_xpath('//*[@id="lst-ib"]').send_keys('Dory')
driver.find_element_by_xpath('//*[@id="sblsbb"]/button/span').click()