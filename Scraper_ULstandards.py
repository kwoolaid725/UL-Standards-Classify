from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pandas as pd
import os


url = "https://www.shopulstandards.com/Catalog.aspx?UniqueKey=1"

chrome_options = Options()
# chrome doesn't close
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(r"/Users/woohyunkim/Desktop/chromedriver.exe", chrome_options=chrome_options)
driver.get(url)
item = 1

results = []
while True:
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    driver.implicitly_wait(2)
    for x in range(0, 10):

        try:
            standard = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_CatalogList_EditionNumberButton_" + str(x))
            standard_value = standard.get_attribute("value")
        except:
            standard_value = None

        try:
            description = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_CatalogList_EditionDescription_" + str(x)).text
        except:
            description = None
        try:
            label = driver.find_element(By.ID,"ContentPlaceHolder1_ContentPlaceHolder1_CatalogList_EditionLabel_" + str(x)).text.replace("(","").replace(")","")
        except:
            label = None
        try:
            catalog = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_CatalogList_EditionCatalog_" + str(x)).text
        except:
            catalog = None
        try:
            edition_date = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_CatalogList_EditionDate_" + str(x)).text.replace("Edition Date: ", "")
        except:
            edition_date = None
        try:
            type_label = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_CatalogList_StandardTypeLabel_" + str(x)).text.replace("Type: ", "")
        except:
            type_label = None

        data = {
            'Standard_Number': standard_value,
            'Description': description,
            'Label': label,
            'Catalog': catalog,
            'Edition_Date': edition_date,
            'Type': type_label
        }

        results.append(data)
        print("item: " + str(item))
        print(data)
        item += 1
    try:
        a = driver.find_element(By.XPATH, '//a[@id="ContentPlaceHolder1_ContentPlaceHolder1_CatalogList_CatalogPager_btnPagerNext" and @class="pagerNavigation"]')
        a.click()
    except Exception as e:
        print(f'Reached the last page.')
        break



print("Done------------------------------------------------------------------------------\n")
print("Total items: " + str(item))
print(results)
df = pd.DataFrame(results)
df.to_csv('UL-Standards-List.csv', mode='a',
          index=False, header=not os.path.exists('UL-Standards-List2.csv'),
          encoding='utf-8-sig')

