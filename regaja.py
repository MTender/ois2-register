from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


def register(username, password):
    driver.get('https://ois2.ut.ee/')
    time.sleep(5)

    try:
        driver.find_element_by_link_text('Registreeringud').click()
    except NoSuchElementException:
        driver.find_element_by_xpath("//button[@color='primary']").click()
        time.sleep(2)
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(10)
        driver.find_element_by_link_text('Registreeringud').click()

    time.sleep(5)
    while True:
        try:
            driver.find_element_by_id('mat-checkbox-1').click()
            time.sleep(5)
            target = driver.find_elements_by_xpath("//button[@class='full-width mat-raised-button "
                                                   "mat-button-base mat-primary ng-star-inserted']")
            target[1].click()
        except IndexError:
            print("Registreeritud!")
            break
        except NoSuchElementException:
            driver.refresh()
            time.sleep(10)


# Muuda ainult j2rgmist kahte rida
usr = "Sinu Õis2 kasutajanimi"
pwd = "Sinu Õis2 parool"

driver = webdriver.Firefox()
while True:
    try:
        register(usr, pwd)
        break
    except Exception:
        time.sleep(10)
