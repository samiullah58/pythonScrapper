# from selenium import webdriver

# from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()

# def extract_job_details_page(url):
#     try:

#         driver.get(url)

#         job_title = driver.find_element(By.TAG_NAME, "h1")
#         title = job_title.text


#         location_xpath = '//*[@id="top"]/section[3]/div/p'

#         location_element = driver.find_element(By.XPATH, location_xpath)

#         location = location_element.text

#         extracted_data = {
#             "title": title,
#             "location": location
#         }

#         return extracted_data
    
#     except Exception as e:
#         print(f"Error extracting text from {url}: {e}")

#     finally:
#         driver.quit()

# job_urls = [
#     "https://www.rolandberger.com/en/Join/All-Jobs/Consulting-Intern-(6-months)-REF2984N.html",
#     "https://www.rolandberger.com/en/Join/All-Jobs/Consulting-Intern-1177.html",
#     "https://www.rolandberger.com/en/Join/All-Jobs/Praktikant-Consulting-Healthcare-(m-w-d)-2498.html",
#     "https://www.rolandberger.com/en/Join/All-Jobs/Praktikant-Consulting-Healthcare-(m-w-d)-2498.html"
#     # Add more job URLs here
# ]

# for url in job_urls:
#     extracted_data = extract_job_details_page(url)
#     if extracted_data:
#         print(f"Job Details:")
#         print(f"Title: {extracted_data['title']}")
#         print(f"Job Details: {extracted_data['location']}")