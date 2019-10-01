from selenium import webdriver
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('./chromedriver',chrome_options =options)
#자원 로드 될때 까지 기다림
keyWord = input("카페 이름 상세히 입력해주세요 :") 
driver.implicitly_wait(3)
driver.get('https://naver.com')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
elem =driver.find_element_by_name('query').send_keys(keyWord)
btn = driver.find_element_by_xpath('//*[@id="sform"]/fieldset/button').click()

driver.find_element_by_xpath('//*[@id="place_main_ct"]/div/div/div[1]/div[3]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 전화 번호
phone = soup.select('div.ct_box_area > div.bizinfo_area > div.list_bizinfo > div.list_item.list_item_biztel > div.txt')
print("전화 번호 : ",phone[0].text.strip())

# 개장 시간
notices = soup.select('div.ct_box_area > div.bizinfo_area > div.list_bizinfo > div.list_item.list_item_biztime > div.txt')
#print(list(notices))
for n in notices:
    print(n.text.strip())

# 카페 메뉴
menus = soup.select('div.ct_box_area > div.bizinfo_area > div.list_bizinfo > div.list_item.list_item_menu > div.txt')

for n in menus :
    print(n.text.strip())

# 지하철 역
subways = soup.select('#panel01 > div > div.sc_box.contact > div.contact_area > div.transport_area > div > ul.list_station > li > div > div > a')


#얼마나 걸리는지
t = soup.select('#panel01 > div > div.sc_box.contact > div.contact_area > div.transport_area > div > ul > li > div > div > span > span')
for i in range(0,len(t)) :
    print("지하철 역",subways[i].text.strip(),", 도보 :",t[i].find_all('em')[0].text.strip())
    print("----------------------")


# driver.quit()