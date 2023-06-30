from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome()
wb = Workbook()
sheet = wb.active


def get_all_mobail_details():
    n = 1

    page_number = get_page_number()
    for page_num in range(page_number+1):
        url = 'https://www.amazon.in/s?i=electronics&rh=n%3A1389432031&fs=true&page={0}&qid=1688070157&ref=sr_pg_{1}'.format(page_num, page_num)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        div = soup.find('div', class_='s-main-slot')
        for a in div.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'):
            print("Title:", a.text.replace('\n', ''))
            sheet.cell(row=n, column=n).value = a.text
            n =+ 1
        wb.save("Mobile_list.xmlx")




def get_page_number():
    url = 'https://www.amazon.in/s?rh=n%3A1389432031&fs=true&ref=lp_1389432031_sar'
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    pagediv = soup.find('div', class_='a-section a-text-center s-pagination-container')
    finalpage = pagediv.find_all('span')[-1].text
    print('Total Number of pages:',finalpage)
    return int(finalpage)


get_all_mobail_details()

driver.close()
