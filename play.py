from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.amazon.co.jp/s?i=instant-video&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=125XTV54KGWRQ&sprefix=%2Cinstant-video%2C454&ref=nb_sb_noss')

# レビュー数を取得
review_selector_name = 'span.a-size-base.s-underline-text'
review_elements = driver.find_elements(By.CSS_SELECTOR, review_selector_name)
reviews = []
for review_element in review_elements:
  reviews.append(review_element.text)

# そのタイトルを取得
title_selector_name = 'span.a-size-base-plus.a-color-base.a-text-normal'
title_elements = driver.find_elements(By.CSS_SELECTOR, title_selector_name)
titles = []
for title_element in title_elements:
  titles.append(title_element.text)

# 出力
# print(reviews)
# print(titles)
review_dict = dict(zip(titles,reviews))
# print(review_dict)

for ad_val in review_dict.items():
    print(ad_val)
