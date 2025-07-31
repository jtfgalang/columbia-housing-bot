from selenium import webdriver
import time
import pickle

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=selenium_session")
driver = webdriver.Chrome(options=options)

driver.get("https://residential.cuf.columbia.edu/c/Asn/Osu.aspx")
input("🔐 Log in and approve DUO. Once housing page loads, press ENTER to save cookies.")
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
driver.quit()
