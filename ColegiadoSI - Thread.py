import csv
import time
import sqlite3
import pandas as pd
from threading import Thread
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def digitar_by_xpath(driver, xpath, texto):
    try:
        driver.find_element_by_xpath(xpath).send_keys(texto)
    except NoSuchElementException:
        return False
    return True

def clicar_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
    except NoSuchElementException:
        return False
    return True

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def capturar_by_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath).text

def capturar_by_xpath_value(driver, xpath):
    return driver.find_element_by_xpath(xpath).get_attribute("value")

class Th(Thread):

        def __init__ (self, num):
              Thread.__init__(self)
              self.num = num

        def run(self):
            print("Processo: "+str(self.num))
            # ------------------Site--------------------#
            driver = webdriver.Chrome()
            driver.get("http://www.csi.uneb.br/")
            #--------------Verifica Site---------------#
            i = 0
            while (i == 0):
                if (driver.title == 'Colegiado de Sistemas de Informação'):
                    i = 1

            clicar_by_xpath(driver, '//*[@id="menu"]/li[1]/span')

            time.sleep(2)
            driver.close()

a = Th(1)
a.start()