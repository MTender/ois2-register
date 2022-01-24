import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def register(username, password):
	driver.get('https://ois2.ut.ee/')
	time.sleep(5)
	
	try:
		driver.find_element(By.XPATH, "//div[contains(text(), 'Registreeringud')]").click()
	except NoSuchElementException:
		driver.find_element(By.XPATH, "//button[@color='primary']").click()
		time.sleep(2)
		driver.find_element(By.ID, "username").send_keys(username)
		driver.find_element(By.ID, "password").send_keys(password)
		driver.find_element(By.XPATH, "//button[@type='submit']").click()
		time.sleep(10)
		driver.find_element(By.XPATH, "// div[contains(text(), 'Registreeringud')]").click()
	
	time.sleep(5)
	while True:
		try:
			driver.find_element(By.XPATH, "// mat-chip[contains(text(), ' 2021/22 kevad ')]").click()
			time.sleep(2)
			driver.find_element(By.ID, 'mat-checkbox-1').click()
			time.sleep(5)
			target = driver.find_elements(By.XPATH, "// span[contains(text(), 'Registreeru õppeainetele ')]")
			target[1].click()
		except IndexError:
			print("Registreeritud!")
			break
		except NoSuchElementException:
			driver.refresh()
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
