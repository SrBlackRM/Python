import requests
import pandas as pd
from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.get("https://www.google.com.br")
