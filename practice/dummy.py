from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# URL of the Amazon product page
url = "https://www.amazon.com/Amazon-Basics-Gaming-Computer-Mouse/dp/B07BZSP9ZJ/ref=sr_1_1_ffob_sspa?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&keywords=gaming+mouse&pd_rd_r=0abf9fa5-d576-467a-94b0-84244c51b64f&pd_rd_w=GC3lC&pd_rd_wg=vG8Wl&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=G3SR26DSJ75YTPZPX5EB&qid=1695882441&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
driver.get(url)

# Find the product title by its ID
product_title = driver.find_element(By.ID, "productTitle").text

# Find the product price by class name
product_price = driver.find_element(By.CLASS_NAME, "a-price").text

# Get the current URL (product link)
product_link = driver.current_url

try:
    # Find the product description by its ID (if available)
    product_description = driver.find_element(By.ID, "universal-product-alert").text
except:
    product_description = "Description not found"

# Print the extracted information
print("Title:", product_title)
print("Price:", product_price)
print("Link:", product_link)
print("Description:", product_description)

# Close the WebDriver
driver.quit()