# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.maximize_window()

driver.implicitly_wait(10)
#ele=driver.find_element_by_xpath("//div[@class='bdbriimgtitle']")
#ele=driver.find_element_by_class_name('bdbriimgtitle')
ele=driver.find_element_by_xpath("//*[@id='u1']/a[8]")

ActionChains(driver).move_to_element(ele).perform()
time.sleep(1)
ele1=driver.find_element_by_link_text(u"搜索设置")
ele1.click()
#time.sleep(5)
driver.find_element_by_link_text(u"保存设置").click()

result=driver.switch_to_alert().text
if result==u'已经记录下您的使用偏好':
    print 'aa'
else:
    print 'bb'

driver.quit()