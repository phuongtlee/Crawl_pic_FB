from aifc import Error
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="chromedriver.exe")

browser.get('https://www.facebook.com/Paimoncutee/photos')
sleep(1)
txtUser = browser.find_element(By.NAME, 'email')
txtUser.send_keys('Phuongle.89593@gmail.com')

txtPass = browser.find_element(By.NAME, 'pass')
txtPass.send_keys('0908784608phuong@')

txtPass.send_keys(Keys.ENTER)
sleep(1)
img = browser.find_elements(By.CSS_SELECTOR, 'div.x8gbvx8.x78zum5')
print(img)
#p = []
#for i in browser.find_elements(By.CLASS_NAME, 'x1n2onr6'):
#    pic = i.find_element(By.TAG_NAME, "img")
#    pic1 = pic.get_attribute('scr')
#    #p.append(pic)
#    print(pic1)
browser.close()
