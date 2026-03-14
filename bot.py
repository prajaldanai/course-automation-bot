from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://c4mpus.com")

print("Login and open the first lesson, then press ENTER")
input()

wait = WebDriverWait(driver, 10)

while True:
    try:

        # scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # START NOW BUTTON
        try:
            start_btn = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Start Now')]"))
            )

            driver.execute_script("arguments[0].scrollIntoView();", start_btn)
            time.sleep(0.5)

            print("Clicking Start Now")
            driver.execute_script("arguments[0].click();", start_btn)

        except:
            pass


        # MARK AS COMPLETE
        try:
            mark_btn = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Mark as complete')]"))
            )

            driver.execute_script("arguments[0].scrollIntoView();", mark_btn)
            time.sleep(0.5)

            print("Clicking Mark as complete")
            driver.execute_script("arguments[0].click();", mark_btn)

        except:
            pass


        # NEXT BUTTON
        try:
            next_btn = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Next')]"))
            )

            driver.execute_script("arguments[0].scrollIntoView();", next_btn)
            time.sleep(0.5)

            print("Clicking Next")
            driver.execute_script("arguments[0].click();", next_btn)

        except:
            print("No Next button found. Finished.")
            break

        time.sleep(2)

    except Exception as e:
        print("Error:", e)
        break

driver.quit()