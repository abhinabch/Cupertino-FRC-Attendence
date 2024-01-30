from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def search_link():
    # Specify the path to the Chrome webdriver
    webdriver_path = r'C:\Users\abhin\OneDrive\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe'  # Update with the correct path to your chromedriver

    #link_to_search = input("Enter the link to search (or 'quit' to exit): ")

    # Initialize the Chrome webdriver with specified path
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)

    while True:
        # Ask the user for the link
        link_to_search = input("Enter the link to search (or 'quit' to exit): ")

        if link_to_search.lower() == 'quit':
            break

        # Open the provided link
        driver.get(link_to_search)

        # Wait for the page to load (you can adjust the time as needed)
        time.sleep(5)

    # Close the webdriver
    driver.quit()

if __name__ == "__main__":
    # Example usage
    search_link()
