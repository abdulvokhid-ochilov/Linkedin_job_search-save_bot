from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\chromedriver_win32\chromedriver.exe"
email = "your email"
password_gmail = "your password"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=105149562&keywords=developer%20intern&location=South%20Korea")
time.sleep(3)
sign_up = driver.find_element_by_link_text("Sign in")
sign_up.click()

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
button = driver.find_element_by_tag_name("button")

username.send_keys(email)
password.send_keys(password_gmail)
button.click()

time.sleep(3)

search_results = driver.find_elements_by_class_name("jobs-search-results__list-item")
pop_up = driver.find_element_by_class_name("msg-overlay-bubble-header")
pop_up.click()

for item in range(len(search_results)):
    title = search_results[item].find_element_by_tag_name("a")
    title.click()
    time.sleep(2)
    save_button = driver.find_element_by_class_name("jobs-save-button")
    save_button.click()
    time.sleep(2)
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.ESCAPE)
    notification = driver.find_element_by_css_selector(".artdeco-toasts_toasts button")
    notification.click()

