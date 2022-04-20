import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #klavye tuşları
from selenium.webdriver.common.by import By
#selenium ve webdirver kütüphanelerini indirdim

os.environ['PATH'] += r";C:/Python/SeleniumDrivers"
driver = webdriver.Chrome()

"""chrome versiyonuma göre driver indirdim 
path hatası vermemesi için os modülünü import ettim ve chrome driver'ın bulunduğu path'i yukarıdaki gibi ekledim.

selenium easy links:
https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html
https://demo.seleniumeasy.com/
"""

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
#gitmek istediğimiz web sitesinin adresini get metodu ile yazdık.
driver.implicitly_wait(5)

#sayfa ilk açıldığında çıkan bildirim ekranındaki 'no thanks butonuna otomatik basılır.
#burada pop up ekranının her zaman açılmama ihtimaline karşı try-except içinde yazıyoruz.
try:
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    #no_button = driver.find_element(by=By.ClASS_NAME,value='at-cm-no-button')
    no_button.click()
except:
    print('No element with this class name.. Skipping....')

# input alanlarının id değerlerine göre alırız.
sum1 = driver.find_element_by_id('sum1')
#sum1 = driver.find_element(by=By.ID,value='sum1')
sum2 = driver.find_element_by_id('sum2')
#sum2 = driver.find_element(by=By.ID,value='sum2')


#manuel olarak bu alanlara değerler gönderebiliriz.
#sayfa çalıştığında input alanlarında 15 ve 20 yazdığı görülür.
#sum1.send_keys(15)
#sum2.send_keys(20)

#yukarıda manuel 15 yazmıştık, aşağıda ise klavye tuşlarını kullanarak yazdık
sum1.send_keys(Keys.NUMPAD1,Keys.NUMPAD5)
sum2.send_keys(Keys.NUMPAD2,Keys.NUMPAD5)

#elementleri her zaman class adı veya id'ye göre almak istemeyebiliriz
#CSS özelliklerine göre butonları alabiliriz.
#button tipindeki elementin onclick metodunda yazan return total() fonksiyonunu çalıştırırız.
btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()









