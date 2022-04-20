from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium import webdriver
#selenium ve webdirver kütüphanelerini indirdim

os.environ['PATH'] += r";C:/Python/SeleniumDrivers"
driver = webdriver.Chrome()

"""chrome versiyonuma göre driver indirdim 
path hatası vermemesi için os modülünü import ettim ve chrome driver'ın bulunduğu path'i yukarıdaki gibi ekledim.

selenium easy links:
https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html
https://demo.seleniumeasy.com/
"""

driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
#gitmek istediğimiz web sitesinin adresini get metodu ile yazdık.


'''Implicit Wait : Bekleme ayarlanırsa, her findElement/findElements çağrısı için belirtilen süre kadar bekler.
webDriver nesnesinin tüm süresi için ayarlanır. Diyelim ki belirli bir süre beklemek istiyorsunuz, diyelim ki 
her bir öğe veya web sayfasındaki birçok öğe yüklenmeden önce 5 saniye. Şimdi, aynı kodu tekrar tekrar yazmak istemezsiniz. 
Bu nedenle, örtük bekleme. Ancak, yalnızca bir öğeyi beklemek istiyorsanız, açık öğesini kullanın.'''

driver.implicitly_wait(8)
my_element = driver.find_element_by_id('downloadButton')
my_element.click()
#sayfadaki butona sağ tık yapıp incele dedik ve butonun id'sinde yazan değeri find_element_by_id metodu ile çalıştırdık.
#ardından butona tıklamak için click metodunu çalıştırdık.


progress_element = driver.find_element_by_class_name('progress-label')
#sayadaki complete yazısının div etiketi içinde class adı ile tutulduğunu gördük.
#Bu yüzden yukarıdaki gibi class adı ile elementi aldık.
#print(f"{progress_element.text}") #sayfa çalışırken progress-element'te tuttuğumuz değeri prin ile console'a yazdırdık
print(f"{progress_element.text == 'Completed!'}") #yukardakinden farklı olarak etikette completed' yazdığı zaman console'a yazdırdık.


'''Explicit Wait : Eğer wait ayarlanmışsa bekleyecek ve sağlanan koşul gerçekleştiğinde 
bir sonraki adıma geçecektir, aksi takdirde belirtilen süre kadar bekledikten sonra bir istisna atacaktır.
Yalnızca web öğesinin görünmesi için değil, aynı zamanda tıklanabilir olması veya web öğelerinin diğer belirli 
özelliklerini yerine getirmesi için de ihtiyacınız vardır. Bu tür bir esneklik ancak açık bir bekleme ile sağlanabilir.
Web sayfasına dinamik veriler yükleniyorsa özellikle yararlıdır. Açık beklemeyi kullanarak bu öğenin geliştirilmesini 
(yalnızca DOM'da görünmekle kalmayıp) bekleyebilirsiniz.'''

#yukarıdakinin bir diğer yazılımı aşağıdaki gibidir.
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        # Element filtration
        (By.CLASS_NAME, 'progress-label'), #class adı ile bulmanın bir diğer yolu
        # The expected text
        'Complete!'
    )
)
# Yukarıda butona tıkladıktan sonra 'Complete!' yazısını görünce programı başarılı bir şekilde tamamlıyor.










