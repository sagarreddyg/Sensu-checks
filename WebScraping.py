from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome()
wb = Workbook()
sheet = wb.active


def Get_Booklist():
    n = 1
    url = 'https://www.amazon.in/s?rh=n%3A1389432031&fs=true&ref=lp_1389432031_sar'
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    div = soup.find('div', class_='s-main-slot')
    for a in div.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'):
        print(a.text.replace('\n',''))
        print(a['href'])
        print('\n')
        sheet.cell(row=n, column=n).value = a.text
        n = + 1
    wb.save("Mobile_list.xmlx")


Get_Booklist()

driver.close()