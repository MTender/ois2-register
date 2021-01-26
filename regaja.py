from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


def register(username, password):
    driver = webdriver.Firefox()

    driver.get('https://ois2.ut.ee/')

    time.sleep(1)
    driver.find_element_by_xpath("//button[@color='primary']").click()
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element_by_link_text('Registreeringud').click()
    time.sleep(1)
    while True:
        try:
            driver.find_element_by_id('mat-checkbox-1').click()
            target = driver.find_elements_by_xpath("//button[@class='full-width mat-raised-button "
                                                   "mat-button-base mat-primary ng-star-inserted']")
            target[1].click()
        except IndexError:
            print("Registreeritud!")
            break
        except NoSuchElementException:
            driver.refresh()
            time.sleep(10)


# Muuda ainult järgmist kahte rida
usr = "Sinu Õis2 kasutajanimi"
pwd = "Sinu Õis2 parool"

register(usr, pwd)
