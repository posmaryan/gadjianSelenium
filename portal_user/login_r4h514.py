from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path=r'C:\Users\Administrator\Documents\fast8\Selenium\drivers\chromedriver.exe')

browser.set_page_load_timeout(10)
browser.get('https://user.hadirr.com/r4h514/')
browser.find_element_by_name('email').send_keys('dara.sativa@fast-8.com')
browser.find_element_by_name('password').send_keys('daraayus')
#klik button login
browser.find_element_by_xpath('/html/body/div/div/div/div/form/div[2]/div/div[2]/div/button').click()
browser.save_screenshot('hasil.png')
time.sleep(2)
browser.quit()
