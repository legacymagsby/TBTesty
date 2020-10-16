from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

username = os.getenv("TESTINGBOT_KEY")
access_key = os.getenv("TESTINGBOT_SECRET")


caps = {
 'platform': 'Windows',
 'browserName': 'chrome',
}

driver = webdriver.Remote(
    command_executor="http://%s:%s@hub.testingbot.com/wd/hub"%(username, access_key),
    desired_capabilities=caps)



driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("TestingBot")
elem.submit()
print(driver.title)
driver.quit()
