#! C:\Users\Murchik\cittadinanza\venv\Scripts python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
from credential import *


try:
    options = Options()

    options.add_argument('--headless')

    link = "https://nullaostalavoro.dlci.interno.it/Ministero/Index2"
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    browser.find_element_by_css_selector("span.close").click()  # chiudo la finestra pup up

    buttons = browser.find_elements_by_css_selector("button.italia-it-button")  #clicko per inserire credenziali
    buttons[1].click()

    confirm = browser.switch_to.alert   # chiudo la finestra pup up per scelta
    confirm.accept()
    try:
        mail = browser.find_element_by_name("userLogin")    # inserisco login
        mail.send_keys(LOGIN)

        pas = browser.find_element_by_css_selector("#passwordLogin")    # inserisco password
        pas.send_keys(PASSWORD)

        time.sleep(1)

        browser.find_element_by_css_selector("input[type='submit']").click()    # clicko per intrare

        browser.find_element_by_css_selector("#linkCittadinanza").click()   # cerco cittadinanza dal menu

        browser.find_element_by_css_selector('#linkCittadinanza2VisualizzaStato').click()   # cerco e clicko sul visualizza la domanda

        result = browser.find_elements_by_xpath("//div[contains(@class,'valoreStatoPratSicitt')]")

        print(result[-1].text)

        browser.find_element_by_css_selector("a[href='Logout']").click()    # clicko sul logout
        time.sleep(1)
    except NoSuchElementException:  # catturo errore per cambio password
        print('Devi aggiornare la password')

finally:

    browser.quit() # Chiudo il browser
