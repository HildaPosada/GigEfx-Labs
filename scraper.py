import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# --- Setup stealth Chrome ---
options = uc.ChromeOptions()
options.headless = False  # Set to True to run in background
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

driver = uc.Chrome(options=options)

try:
    print("🔄 Loading Wootware GPU page...")
    driver.get("https://www.wootware.co.za/computer-components/graphics-cards.html")

    print("⏳ Waiting for products to load...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-item-info'))
    )

    products = driver.find_elements(By.CLASS_NAME, 'product-item-info')
    print(f"✅ Found {len(products)} products.")

    with open("wootware_products.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Price", "Link", "Vendor"])

        for product in products:
            try:
                name = product.find_element(By.CLASS_NAME, 'product-item-name').text
                price = product.find_element(By.CLASS_NAME, 'price').text
                link = product.find_element(By.TAG_NAME, 'a').get_attribute('href')

                print("🛒", name)
                print("💸", price)
                print("🔗", link)
                print("-" * 50)

                writer.writerow([name, price, link, "Wootware"])
            except Exception as e:
                print("⚠️ Skipping product due to error:", e)
                continue

except Exception as e:
    print("❌ Failed to scrape Wootware:", e)

finally:
    driver.quit()
    print("✅ Scraper finished and browser closed.")
