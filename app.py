from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': '88.0',
 'os': 'Windows',
 'name': 'BStack-[Python] Sample Test'

}

username = os.environ.get('BROWSERSTACK_USERNAME')
password = os.environ.get('BROWSERSTACK_ACCESS_KEY')
desired_cap['build'] = os.environ.get('BROWSERSTACK_BUILD_NAME')
driver = webdriver.Remote(
    command_executor='https://' + username + ':' + password + '@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
driver.get("http://localhost:3000")
# if not "Google" in driver.title:
#     raise Exception("Unable to load google page!")
# elem = driver.find_element_by_name("q")
# elem.send_keys("BrowserStack")
# elem.submit()
# try:
#     WebDriverWait(driver, 5).until(EC.title_contains("BrowserStack"))
#     # Setting the status of test as 'passed' or 'failed' based on the condition; if title of the web page starts with 'BrowserStack'
#     driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
# except TimeoutException:
#     driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
print(driver.title)
driver.quit() 
