from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Assume the HTML file is saved locally as test.html
url = 'ex2.html'  # replace with your actual file path

options = Options()
options.add_argument('--headless')  # run headlessly
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = 'file://' + os.path.abspath('ex2.html')  # or your HTML filename
driver.get(url)
time.sleep(1)  # wait for page load

def get_div_and_check_border_radius(expected_id, expected_border_radius):
    div = driver.find_element(By.ID, expected_id)
    border_radius = div.value_of_css_property('border-radius')
    print(f"Div id: {expected_id}, Border-radius: '{border_radius}'")
    # border_radius may be returned as e.g. '50%' or '50px', or '0px' if unset; normalize for check
    return border_radius == expected_border_radius or (expected_border_radius == '100%' and (border_radius == '100%' or border_radius in ['', '0px']))

# Initial state: id should be div1 with border-radius 100% or none
assert get_div_and_check_border_radius('div1', '100%'), "Initial div should have border-radius 100% or none"

button = driver.find_element(By.TAG_NAME, 'button')

# Click to toggle to div2 (border-radius 50%)
button.click()
time.sleep(0.5)
assert get_div_and_check_border_radius('div2', '50%'), "After 1st click div should have border-radius 50%"

# Click to toggle back to div1 (border-radius 100%)
button.click()
time.sleep(0.5)
assert get_div_and_check_border_radius('div1', '100%'), "After 2nd click div should have border-radius 100% or none"

print("All tests passed.")
driver.quit()
