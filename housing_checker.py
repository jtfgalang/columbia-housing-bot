import time, pickle, requests, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_alert():
    msg = "🏠 517 W 121st St is AVAILABLE! Check: https://residential.cuf.columbia.edu/c/Asn/Osu.aspx"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--user-data-dir=selenium_session")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://residential.cuf.columbia.edu/")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://residential.cuf.columbia.edu/c/Asn/Osu.aspx")
        time.sleep(5)
        if "517 W 121st St" in driver.page_source:
            send_alert()
        else:
            print("Still not available.")
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

while True:
    check()
    time.sleep(600)
