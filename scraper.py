from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_zomato(city="bangalore"):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    url = f"https://www.zomato.com/{city}/restaurants"
    driver.get(url)
    time.sleep(5)

    for _ in range(3):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        time.sleep(2)

    names, cuisines, ratings, locations = [], [], [], []

    restaurants = driver.find_elements(
        By.CSS_SELECTOR, "div.sc-1mo3ldo-0"
    )

    for r in restaurants:
        try:
            name = r.find_element(By.CSS_SELECTOR, "a").text
        except:
            name = "N/A"

        try:
            cuisine = r.find_element(By.CSS_SELECTOR, "p").text
        except:
            cuisine = "N/A"

        try:
            rating = r.text
        except:
            rating = "N/A"

        try:
            location = r.text
        except:
            location = "N/A"

        names.append(name)
        cuisines.append(cuisine)
        ratings.append(rating)
        locations.append(location)

    driver.quit()

    df = pd.DataFrame({
        "Restaurant": names,
        "Cuisine": cuisines,
        "Rating": ratings,
        "Location": locations
    })

    return df