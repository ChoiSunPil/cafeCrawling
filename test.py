from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome('./chromedriver')

#자원 로드 될때 까지 기다림
driver.implicitly_wait(3)

# driver.get('https://naver.com')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# elem =driver.find_element_by_name('query').send_keys('투썸')
# btn = driver.find_element_by_xpath('//*[@id="sform"]/fieldset/button').click()


driver.get('https://store.naver.com/restaurants/detail?id=12952314')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

notices = soup.select('div.ct_box_area > div.bizinfo_area > div.list_bizinfo > div.list_item.list_item_biztime > div.txt')

#print(list(notices))
for n in notices:
    print(n.text.strip())