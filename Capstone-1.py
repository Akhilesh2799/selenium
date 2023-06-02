Bit = int(input("ENTER YOUR BIT 64 OR 32"))
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys
driver = webdriver.Chrome(executable_path='C:\\Users\\amini\\Downloads\\chromedriver_win32.zip\\chromedriver.exe')
driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(3)

if Bit==64:
    element = driver.find_element(By.XPATH,"//*[@id='APjFqb']")
    element.clear()
    element.send_keys('python.org')
    time.sleep(3)

    element.send_keys(Keys.RETURN)
    time.sleep(3)

    pyt = "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a/div/span/div/img"
    driver.find_element(By.XPATH, pyt).click()
    time.sleep(3)

    element = driver.find_element(By.XPATH,"//*[@id='downloads']/a")
    element.click()
    
    element1 = driver.find_element(By.XPATH,"//*[@id='touchnav-wrapper']/header/div/div[2]/div/div[3]/p/a")
    element1.click()
elif Bit==32:
    element = driver.find_element(By.XPATH,"//*[@id='APjFqb']")
    element.clear()
    element.send_keys('https://www.python.org/downloads/windows/')
    time.sleep(3)

    element.send_keys(Keys.RETURN)
    time.sleep(3)
    
    '''pzt = "//*[@id='rso']/div[1]/div/div/div[1]/div/a/h3/span/div/img"
    driver.find_element(By.XPATH, pzt).click()
    time.sleep(3)'''
    element = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div[1]/div/a/h3")
    element.click()

    element = driver.find_element(By.XPATH,"//*[@id='content']/div/section/article/div/div[1]/ul/li[2]/ul/li[4]/a")
    element.click()
