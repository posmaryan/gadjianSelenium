from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\Documents\fast8\Selenium\drivers\chromedriver.exe')

# login r4h514
driver.get("https://user.gadjian.com/r4h514/190900171")
driver.find_element_by_id("email").send_keys("naya@gadjian.com")
driver.find_element_by_id("password").send_keys("cilukba")
driver.find_element_by_xpath("//button[@type='submit']").click()


# assign polkerkar
driver.get("https://user.gadjian.com/polkerkar")
driver.find_element_by_xpath("//*[@id='page-content']/div[5]/div/div/div/div[3]/div[4]/div/table/tbody/tr[1]/td[6]/a/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='polker_chosen']/a").click()
driver.find_element_by_xpath("//div[@id='polker_chosen']/div/ul/li").click()
# pilih tanggal dari - sampai berlaku polkerkar
driver.find_element_by_xpath("//form[@id='form-polkerkar']/div[3]/div/div/div/div/span[2]/i").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/thead/tr[2]/th[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div[2]/table/tbody/tr/td/span").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/tbody/tr/td[4]").click()
time.sleep(3)
driver.find_element_by_xpath("//form[@id='form-polkerkar']/div[3]/div/div/div[2]/div/span[2]/i").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/thead/tr[2]/th[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div[2]/table/tbody/tr/td/span[12]").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/tbody/tr[5]/td[5]").click()
# submit assign polkerkar
driver.find_element_by_xpath("(//button[@type='button'])[21]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[3]/div/div/div[3]/div/div/button[1]").click()
# verify toast berhasil
driver.find_element_by_xpath("/html/body/div[5]")


# delete polker
time.sleep(3)
driver.find_element_by_xpath("//*[@id='page-content']/div[1]/div[2]/div/div/div[2]/div/div/table/tbody/tr/td[8]/div/a[3]/i").click()
Alert(driver).accept()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[5]")


# assign polkerkar lagi
driver.get("https://user.gadjian.com/polkerkar")
driver.find_element_by_xpath("//*[@id='page-content']/div[5]/div/div/div/div[3]/div[4]/div/table/tbody/tr[1]/td[6]/a/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='polker_chosen']/a").click()
driver.find_element_by_xpath("//div[@id='polker_chosen']/div/ul/li").click()
# pilih tanggal dari - sampai berlaku polkerkar
driver.find_element_by_xpath("//form[@id='form-polkerkar']/div[3]/div/div/div/div/span[2]/i").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/thead/tr[2]/th[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div[2]/table/tbody/tr/td/span").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/tbody/tr/td[4]").click()
time.sleep(3)
driver.find_element_by_xpath("//form[@id='form-polkerkar']/div[3]/div/div/div[2]/div/span[2]/i").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/thead/tr[2]/th[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div[2]/table/tbody/tr/td/span[12]").click()
time.sleep(3)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/tbody/tr[5]/td[5]").click()
# submit assign polkerkar
driver.find_element_by_xpath("(//button[@type='button'])[21]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[3]/div/div/div[3]/div/div/button[1]").click()
# verify toast berhasil
driver.find_element_by_xpath("/html/body/div[5]")


# verify BHK di libur nasional pada pola kerja
time.sleep(3)
driver.get("https://user.gadjian.com/absensi")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[12]/div[2]/div[6]/div/div/div/div[3]/div[3]/div/form/div/div/span/i").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@data-date='1590969600000']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='tabelAbsensi']/tbody/tr[1]/td[3]/div/div[2]/button/div[10]")