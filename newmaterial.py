from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# secret store the password readed of a file called 'senha'
secret = open('senha', 'r').readlines()[0]

# Open the browser
driver = webdriver.Firefox()

# Acess the website
driver.get("https://www.ggte.unicamp.br/ea/")
username = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[4]/td[2]/form/table/tbody/tr[3]/td[2]/div/input')
password = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[4]/td[2]/form/table/tbody/tr[4]/td[2]/div/input')
login_teleduc = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[4]/td[2]/form/table/tbody/tr[5]/td[2]/button/img")
username.send_keys("150556")
password.send_keys(secret)
login_teleduc.click()

driver.find_element_by_xpath('/html/body/form/center/table[2]/tbody/tr/td[2]/div/table/tbody/tr/td/font/p[5]/a').click()
driver.find_element_by_xpath('//*[@id="my_menu"]/div[2]/table/tbody/tr[3]/td[5]/font/a').click()
driver.find_element_by_xpath('//*[@id="menu8"]/font/a/nobr/b').click()

materials = driver.find_element_by_xpath('//*[@id="menu8"]/font/a')

print(materials)