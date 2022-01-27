from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import time
import lxml.html as parser
import requests
import csv
import random
import ftplib
from urllib.parse import urlsplit, urljoin, urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np


driver = webdriver.Chrome(ChromeDriverManager().install())

#driver.get('https://www.google.com/shopping/product/12746421292469448165')

df = pd.read_csv('GSHOP3.csv',sep=";")

desc = {}


nomes = []
precos = []

for x in df['URL'].to_list():
    try:
        driver.get(x)
        time.sleep(2)
        names = driver.find_elements_by_xpath("//a[@class='b5ycib shntl']")
        for nam in names[3:]:
            #print(nam.text)
            nomes.append(nam.text)

        prices = driver.find_elements_by_xpath("//div[@class='drzWO']")
        for pric in prices:
            #print(pric.text)
            precos.append(pric.text)
    except:
        print('Produto Não encontrado')

desc = []
for i in range(len(nomes)):
    valores = {}
    valores[nomes[i]] = precos[i]
    desc.append(valores)

df = pd.DataFrame(desc)

df.to_csv("teste06.05")