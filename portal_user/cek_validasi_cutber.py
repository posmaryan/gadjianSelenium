from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\Documents\fast8\Selenium\drivers\chromedriver.exe')

# login r4h514
driver.get("https://user.gadjian.com/r4h514/190900171")
driver.find_element_by_id("email").send_keys("naya@gadjian.com")
driver.find_element_by_id("password").send_keys("cilukba")
driver.find_element_by_xpath("//button[@type='submit']").click()

# add polker ke karyawan
driver.get("https://user.gadjian.com/polkerkar")
driver.find_element_by_xpath("//*[@data-original-title='Tambah pola kerja baru']").click()
sleep(1.5)
driver.find_element_by_xpath("//*[@id='polker_chosen']/a").click()
sleep(1.5)
driver.find_element_by_xpath("//div[@id='polker_chosen']/div/ul/li").click()
sleep(1.5)
# pilih tanggal dari - sampai berlaku polkerkar
driver.find_element_by_xpath("//form[@id='form-polkerkar']/div[3]/div/div/div/div/span[2]/i").click()
sleep(1.5)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/thead/tr[2]/th[2]").click()
sleep(1.5)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div[2]/table/tbody/tr/td/span").click()
sleep(1.5)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/tbody/tr/td[4]").click()
sleep(1.5)
driver.find_element_by_xpath("//form[@id='form-polkerkar']/div[3]/div/div/div[2]/div/span[2]/i").click()
sleep(1.5)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/thead/tr[2]/th[2]").click()
sleep(1.5)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div[2]/table/tbody/tr/td/span[12]").click()
sleep(1.5)
driver.find_element_by_xpath("//body[@id='dashboard']/div[15]/div/table/tbody/tr[5]/td[5]").click()
# submit add polkerkar
sleep(1.5)
driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[4]/div/div/div/div[3]/div/div/form/div[8]/div/button").click()
sleep(1.5)
driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[3]/div/div/div[3]/div/div/button[1]").click()

# cek halaman cuti tahunan (cek apakah cuti bersama tertampil atau tidak)
sleep(1.5)
driver.find_element_by_xpath("//*[@id='daftar-personalia']/div[3]/div[1]/div/div/button[5]").click()
jmlcutibersama = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/p[3]").text
assert jmlcutibersama !=('Cuti bersama: 0')

# hapus polker dari karyawan
sleep(3)
driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[1]/div[1]/div/div/div[3]/div[1]/div/div/button[10]").click()
sleep(3)
driver.find_element_by_xpath("//*[@id='page-content']/div[1]/div[2]/div/div/div[2]/div/div/table/tbody/tr/td[8]/div/a[3]/i").click()
Alert(driver).accept()
sleep(3)
driver.find_element_by_xpath("/html/body/div[5]")

# cek lagi halaman cuti tahunan
sleep(1.5)
driver.find_element_by_xpath("//*[@id='daftar-personalia']/div[3]/div[1]/div/div/button[5]").click()
sleep(1.5)
driver.find_element_by_xpath("//*[@id='daftar-personalia']/div[3]/div[1]/div/div/button[5]").click()
jmlcutibersama = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/p[3]").text
assert jmlcutibersama ==('Cuti bersama: 0')

# delete polker
sleep(3)
driver.find_element_by_xpath("//*[@id='page-content']/div[1]/div[2]/div/div/div[2]/div/div/table/tbody/tr/td[8]/div/a[3]/i").click()
Alert(driver).accept()
sleep(3)
driver.find_element_by_xpath("/html/body/div[5]")