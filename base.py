from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Specify the path to the Chrome WebDriver
webdriver_path = r'C:\Users\ASUS\Desktop\zoom selenium\join-zoom-calls\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Initialize Chrome WebDriver
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

#  Google Form
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform?pli=1'
driver.get(form_url)

# Function to wait for an element and send keys
def fill_text_field(xpath, text):
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.send_keys(text)
    except Exception as e:
        print(f"Error locating element with XPath: {xpath}")
        print(e)


fill_text_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', 'Abdul Raheman Shaikh')
fill_text_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input', '8788819257')
fill_text_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', 'iamraheman555@gmail.com')
fill_text_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea', 'B/111 Shobha Nagar Nanded Maharashtra')
fill_text_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input', '431605')
fill_text_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input', '06-06-2002')
fill_text_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input', 'Male')

# Extracting the code from <b> tag and fill in the next answer field
try:
    code_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="i30"]/span[1]/b'))
    )
    code_text = code_element.text
    fill_text_field('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input', code_text)
except Exception as e:
    print("Error extracting code text.")
    print(e)

# submit the form
submit_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))
)
submit_button.click()

# Wait for 1 minute to check  (for personal use)
time.sleep(60)

# Close the WebDriver
driver.quit()
