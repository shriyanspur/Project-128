from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

find_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
driver = webdriver.Edge("./edgedriver/msedgedriver.exe")

driver.get(find_url)

time.sleep(10)

headers = ['Name', 'Radius', 'Mass', 'Distance']
new_stars_data = []
star_data = []
temp_list = []

def scrape_data():
    for i in range(0, 59):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for tr_tags in soup.find_all('tr', attrs={'title'}):
            td_tags = tr_tags.find_all('td')
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find('a').contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append('')

        new_stars_data.append(temp_list)

    with open("scrapper.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers)
        csvwriter.writerows(new_stars_data)

scrape_data()