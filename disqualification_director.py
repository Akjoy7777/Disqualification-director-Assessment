from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import os

# Path to your ChromeDriver executable
chrome_driver_path = "C://Python_selenium_framework_project//Driver//chromedriver-win64//chromedriver-win64//chromedriver.exe"

# Create a Service object with the path to the ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Initialize WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Load your HTML file locally or use it in a string and load it
html_file_path = os.path.abspath('Disqualified_Directors.html')  # Assuming you saved the file locally
driver.get(f"C://Python_selenium_framework_project//Disqualified_Directors.html")


directors = []

sections = driver.find_elements(By.CLASS_NAME, 'accordion-item')

# Loop through each section to extract the information
for section in sections:
    divs = section.find_elements(By.CSS_SELECTOR, "div.rte")

    # Loop through each div and extract data
    for div in divs:
        details = {}
        paragraphs = div.find_elements(By.TAG_NAME, 'p')
        
        for paragraph in paragraphs:
            text = paragraph.text.strip()
            # Extract the text content of each <p> element
            if 'Name:' in text:
                details['Name'] = text.split('Name:')[1]
            elif 'Address (at date of disqualification):' in text:
                details['Address'] = text.split('Address (at date of disqualification):')[1]
            elif 'Date of Birth:' in text:
                details['DOB'] = text.split('Date of Birth:')[1]
            elif 'Period of Disqualification:' in text:
                details['Period of Disqualification'] = text.split('Period of Disqualification:')[1]
            elif 'Dates of Disqualification:' in text:
                details['Dates of Disqualification'] = text.split('Dates of Disqualification:')[1]

        directors.append(details)

# Convert to JSON format
directors_json = json.dumps(directors, indent=4)

with open('disqualification_director.json', 'w') as f:
    json.dump(directors, f, indent=4)

# Clean up
driver.quit()
