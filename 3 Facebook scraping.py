from bs4 import BeautifulSoup as Bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height


driver = webdriver.Chrome(executable_path='C:/WebDrivers/chromedriver.exe')

url = 'https://www.facebook.com/login'
driver.get(url)

driver.implicitly_wait(10)

email = 'Your Email'
email_xpath = """//*[@id="email"]"""
find_email_element = driver.find_element_by_xpath(email_xpath)
find_email_element.send_keys(email)

driver.implicitly_wait(10)

password = 'Your Password'
password_xpath = """//*[@id="pass"]"""
find_password_element = driver.find_element_by_xpath(password_xpath)
find_password_element.send_keys(password)
find_password_element.send_keys(Keys.ENTER)

sleep(6)

group_url = 'https://www.facebook.com/groups/playstoreappofficial/members'
driver.get(group_url)

driver.implicitly_wait(10)

scroll(driver, 2)

names = []
final_names = []

src = driver.page_source
html_soup = Bs4(src, 'lxml')
html_soup.prettify()

for name in html_soup.find_all('a', {'class': "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"}):
    text = name.get_text()
    list_0 = names.append(text)


for final_name in names[1:]:
    final_names.append(final_name)


df = pd.DataFrame(final_names)
df.to_csv('Group_Members.csv', index=True)


driver.quit()
