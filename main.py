from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


chrome_selenium_driver_path = 'C:\bin\chromedriver.exe'


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

