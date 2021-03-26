from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

from secret import secret


def open_browser():
    driver = webdriver.Chrome('./chromedriver')
    return driver


def check_exists_by_xpath(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def login(driver):
    driver.get('http://www.neopets.com/prehistoric/omelette.phtml?rand=11996')

    username = driver.find_element_by_xpath('/html/body/div[6]/div[2]/form/input[3]')
    password = driver.find_element_by_id('loginPassword')
    login = driver.find_element_by_class_name("login-button")
    username.send_keys("baby94_2_2")
    password.send_keys(secret)
    login.click()


def take_omelete(driver):
    driver.get('http://www.neopets.com/prehistoric/omelette.phtml?rand=11996')
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td[2]/center[2]/form/input[2]').click()


def fight(driver):
    driver.get("http://www.neopets.com/dome/fight.phtml")



    driver.find_element_by_class_name('nextStep').click() #Select neopet
    sleep(20)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[6]/div[5]/div[3]/div[4]').click() #Go to next
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[6]/div[5]/div[4]/div[1]/div[3]/div[2]/table/tbody/tr[16]/td[4]/div[1]').click() #Choose fighter
    driver.find_element_by_xpath('//*[@id="bdFightStep3FightButton"]').click() #Go to the fight
    sleep(30)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/div[1]/div[1]/button/div').click() #start the fight

    # #first fight
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/a[1]/div').click() #open the weapons 1
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/a[1]/div').click() #open the weapons 1
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/div[2]/div[3]/ul[1]/li[1]/img').click() #select the first weapon
    
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/a[2]/div').click() #open the weapons 2
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/div[2]/div[3]/ul[1]/li[2]/img').click() #select the second weapon

    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/a[3]/div').click() #open the habilities
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/div[6]/div[3]/table/tbody/tr/td[1]/div/div').click() #select hability
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/form/button[3]/div').click() #fight
    sleep(25)

    # #fight's loop
    while not check_exists_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/div[1]/div[2]/button[1]', driver):
        driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/form/button[3]/div').click() #fight
        sleep(25)

    driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr/td/div[3]/div[1]/div[2]/button[1]').click() #Take rewards


def collect_bank_interest(driver):
    driver.get("http://www.neopets.com/bank.phtml")
    driver.find_element_by_xpath('/html/body/div[12]/div[3]/div[2]/div[2]/div[2]/div/form/input[3]').click()


def close(driver):
    driver.close()


driver = open_browser()
login(driver)
# take_omelete(driver)
fight(driver)
# collect_bank_interest(driver)
sleep(5)
close(driver)