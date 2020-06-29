import requests
import time
import csv

from selenium import webdriver
from bs4 import BeautifulSoup

f = open('starbucks.csv', 'w+', encoding='utf-8')
cw = csv.writer(f)
cw.writerow(['menu', 'category', 'name', 'nutrition', 'allergy'])


#다운받은 웹드라이버 위치
driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')

#페이지 접근
driver.get('https://www.starbucks.co.kr/menu/drink_list.do')

#html 소스 추출 
html = driver.page_source

#bs로 html parsing
bs = BeautifulSoup(html, 'html.parser')

#product name crawling
products = bs.select('.product_list a.goDrinkView')

for product in products:
    product_id = product['prod']


    #이름
    name = product.select('img')[0]['alt']


    driver.get(f'https://www.starbucks.co.kr/menu/drink_view.do?product_cd={product_id}')
    html_source = driver.page_source
    bs = BeautifulSoup(html_source, 'html.parser')

    #메뉴
    menu = bs.select_one('.sub_tit_wrap > div > ul > li:nth-child(5) > a').text
 

    #카테고리
    category = bs.select('.cate')[0].text

    # #용량
    # volume = bs.select_one('#product_info01').text

    #영양정보
    nutrition = []
    kcal = bs.select_one('.product_info_content .kcal dd').text
    sat_FAT = bs.select_one('.product_info_content .sat_FAT dd').text
    protein = bs.select_one('.product_info_content .protein dd').text
    fat = bs.select_one('.product_info_content .fat dd').text
    trans_FAT = bs.select_one('.product_info_content .trans_FAT dd').text
    sodium = bs.select_one('.product_info_content .sodium dd').text
    sugars = bs.select_one('.product_info_content .sugars dd').text
    caffeine = bs.select_one('.product_info_content .caffeine dd').text
    cholesterol = bs.select_one('.product_info_content .cholesterol dd').text
    chabo = bs.select_one('.product_info_content .chabo dd').text
    nutrition += [kcal, sat_FAT, protein, fat, trans_FAT, sodium, sugars, caffeine, cholesterol, chabo]


    #알레르기
    try:
        allergy = bs.select_one('.product_factor > p').text
        allergy = allergy.split(":")
        allergy = allergy[1]
    except Exception:
        allergy = ''

    
    print(menu, category, name, nutrition, allergy)
    time.sleep(3)

    
    cw.writerow( (menu, category, name, nutrition, allergy) )

f.close()
driver.quit()