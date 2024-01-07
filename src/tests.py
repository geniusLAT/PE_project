from selenium import webdriver
options = webdriver.ChromeOptions()
from selenium.webdriver.common.by import By
import time


URL='http://185.84.163.5:8080'

driver = webdriver.Chrome( options=options)
def CheckPhrase(phrase):
    global driver
    try:
        driver.get(URL)

        time.sleep(1)

        # Находим элемент input и вводим туда текст
        input_element = driver.find_element(By.TAG_NAME,'input') 
        input_element.send_keys(phrase)

        # Находим кнопку и нажимаем на неё
        button_element = driver.find_elements(By.TAG_NAME,"button")
        #print("buttons "+str(len(button_element)))
        button_element[1].click()

        time.sleep(1)

        # Получаем html код страницы после нажатия на кнопку
        html_code = driver.page_source

        if "toxic" in html_code:
            return ("toxic")
        else:
            print("Not toxic")

        if "neutral" in html_code:
            return ("neutral")
        else:
            print("Not neutral")
        return "no word"
    except:
        return "error"


if __name__ =="__main__":
    assert CheckPhrase("")!='error'
    assert CheckPhrase("Вы твари")=='toxic'
    assert CheckPhrase("Вы милые люди")=='neutral'
    