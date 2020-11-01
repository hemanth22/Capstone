import time
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 800))
display.start()
chrome_options = webdriver.ChromeOptions()
# below trick saved my life
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument("headless")
# set the folder where you want to save your file
prefs = {'download.default_directory' : os.getcwd()}
chrome_options.add_experimental_option('prefs', prefs)

# Optional argument, if not specified will search path.
driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options,service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
chrome_options=chrome_options

# Scraping steps
driver.get("http://54.201.142.247/")
time.sleep(3)
print(driver.title)
time.sleep(3)
print(' [*] Finished!')
print(driver.current_url)
driver.close()
driver.quit()
