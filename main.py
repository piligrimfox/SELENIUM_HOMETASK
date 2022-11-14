driver = webdriver.Chrome(executable_path="./C:\Users\pilig\Desktop\selenim\webdriver")
import codecs
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        driver.get("https://www.wildberries.ru/")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")
        goods_str = ''
        for good in goods_arr:
            good_title = good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text
            print(good_title)
            goods_str = goods_str + good_title + "\n"
        with codecs.open("parsing.txt", "w", "utf-8") as stream:
            stream.write(goods_str)
    except Exception as ex:
        print("An error occured: \n" + str(ex))
main()
