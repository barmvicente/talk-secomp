from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import sys

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

#login

secret = open('senha', 'r').readlines()[0]
driver = webdriver.Firefox()
driver.get("http://www.neopets.com/dome/fight.phtml")
username = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td/div[3]/div[4]/form/div/div[1]/div[2]/input')
password = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td/div[3]/div[4]/form/div/div[2]/div[2]/input')
login = driver.find_element_by_class_name("welcomeLoginButton")
username.send_keys("baby94_2_2")
password.send_keys(secret)
login.click()


driver.find_element_by_xpath('//*[@id="bdFightStep1"]/div[3]').click() #Select neopet
driver.find_element_by_xpath('//*[@id="bdFightStep2"]/div[4]').click() #Go to next
driver.find_element_by_xpath('//*[@id="npcTable"]/tbody/tr[16]/td[4]/div[1]').click() #Choose fighter
driver.find_element_by_xpath('//*[@id="bdFightStep3FightButton"]').click() #Go to the fight
time.sleep(30)
driver.find_element_by_xpath('//*[@id="start"]/div').click() #start the fight

#first fight
driver.find_element_by_xpath('//*[@id="p1e1m"]/div').click() #open the weapons 1
time.sleep(5)
driver.find_element_by_xpath('//*[@id="p1e1m"]/div').click() 
driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="content"]/table/tbody/tr/td/div/div/div/ul/li[1]/img').click() #select the first weapon
driver.find_element_by_xpath('//*[@id="p1e2m"]').click() #open the weapons 2
driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="content"]/table/tbody/tr/td/div/div/div/ul/li[2]/img').click() #select the second weapon
driver.find_element_by_xpath('//*[@id="p1am"]').click() #open the habilities
driver.find_element_by_xpath('//*[@id="p1ability"]/div[3]/table/tbody/tr/td[2]/div/div').click() #select hability
driver.find_element_by_xpath('//*[@id="fight"]/div').click() #fight
time.sleep(25)

#fight's loop
while not check_exists_by_xpath('//*[@id="playground"]/div[2]/button[1]'):
	driver.find_element_by_xpath('//*[@id="fight"]/div').click() #fight
	time.sleep(25)

driver.find_element_by_xpath('//*[@id="playground"]/div[2]/button[1]').click() #Take rewards

time.sleep(10)
driver.get("http://www.neopets.com/bank.phtml")
driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td/div/form/input[2]').click()
time.sleep(10)
driver.close()