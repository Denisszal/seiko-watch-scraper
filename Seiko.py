#241RDB159 un 241RDB155
import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://laiksjewellery.lv/lv/"
driver.get(url)


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "acceptPrivacyAllBtn"))).click()


search_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "search-inp")))
search_input.send_keys("Seiko")

search_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"][value="Meklēt"]')))
search_button.click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[@class="filter-head" and normalize-space()="Aproce"]'))).click()
WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[title="Ādas siksniņa"]'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[@class="filter-head" and normalize-space()="Dzimums"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[title="Vīriešu"]'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[@class="filter-head" and normalize-space()="Stikls"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[title="Safīra stikls"]'))).click()

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-box")))

products = driver.find_elements(By.CLASS_NAME, "product-box")
print(f"Total items: {len(products)}")

model_codes = []

with open("seiko_watches.txt", "w", encoding="utf-8") as file:
    for idx, product in enumerate(products, 1):
        try:
            link_el = product.find_element(By.CSS_SELECTOR, 'a[href*="/lv/product/"]')
            link = link_el.get_attribute("href").strip()

            title_el = product.find_element(By.CLASS_NAME, "title")
            name = title_el.text.strip().replace("Rokas pulkstenis", "").strip(" ,")

            match = re.search(r'\b[A-Z]{2,}\d{2,}[A-Z]?\d*\b', name)
            model_code = match.group(0) if match else "UNKNOWN"
            model_codes.append(model_code)

            try:
                price_el = product.find_element(By.CLASS_NAME, "isoldprice")
                price = price_el.text.strip()
            except:
                price = "No price found"

            line = f"{idx}. {name}, {price} — {link}\n"
            print(line.strip())
            file.write(line)
        except Exception as e:
            print(f"Error parsing product: {e}")

with open("ebay_results.txt", "w", encoding="utf-8") as ebay_file:
    for code in model_codes:
        if code == "UNKNOWN":
            ebay_file.write(f"{code}: Not found (invalid code)\n")
            continue

        ebay_search_url = f"https://www.ebay.com/sch/i.html?_nkw={code}&_sacat=0&LH_TitleDesc=0"
        driver.get(ebay_search_url)
        
        try:
            cookie_button = driver.find_element(By.ID, "gdpr-banner-accept")
            cookie_button.click()
        except:
            pass 

        items = driver.find_elements(By.CSS_SELECTOR, ".s-item")
        found = False

        for item in items:
            try:
                title_el = item.find_element(By.CSS_SELECTOR, ".s-item__title")
                title = title_el.text.strip()

                if not title or "Shop on eBay" in title:
                    continue

                if code.upper() not in title.upper():
                    continue

                price_el = item.find_element(By.CSS_SELECTOR, ".s-item__price")
                price = price_el.text.strip()

                link_el = item.find_element(By.CSS_SELECTOR, ".s-item__link")
                link = link_el.get_attribute("href").strip()

                ebay_file.write(f"{code}: {title} — {price} — {link}\n")
                print(f"{code}: {title} — {price} — {link}")
                found = True
            except:
                continue

        if not found:
            ebay_file.write(f"{code}: Not found\n")
            print(f"{code}: Not found")

driver.quit()

os.startfile("seiko_watches.txt")
os.startfile("ebay_results.txt")

print("Model codes:", model_codes)
