import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize the webdriver (example with Chrome)
browser = webdriver.Chrome()

# Open the initial webpage
browser.get("https://www.justwatch.com/in/movies?release_year_from=2000")
time.sleep(1)

# Scroll down to load more movies
elem = browser.find_element(By.TAG_NAME, "body")
no_of_pagedowns = 2

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    no_of_pagedowns -= 1

# Collect movie URLs
movie_urls = []
post_elems = browser.find_elements(By.CLASS_NAME, "title-list-grid__item--link")

for post in post_elems:
    movie_urls.append(post.get_attribute('href'))

# Open new tabs and interact with the page
number_of_movies = len(movie_urls)

browser.execute_script("window.open('');")
time.sleep(2)



# Switch back to the original tab
browser.switch_to.window(browser.window_handles[0])


for i in range(number_of_movies):
    # Open a new tab
    browser.execute_script("window.open('');")
    time.sleep(2)

    # Switch to the new tab
    browser.switch_to.window(browser.window_handles[-1])
    movie = movie_urls[number_of_movies-1]
    # Navigate to the movie URLhttps://www.justwatch.com/in/tv-show/mirzapur
    browser.get(movie)
    time.sleep(2)
    # Find the desired elements
    try:
        amazon_prime_element = browser.find_element(By.XPATH, "//img[@alt='Amazon Prime Video']")
        if amazon_prime_element:

    except Exception:
        print(f"{movie} is not available on Amazon Prime Video.")

    try:
        amazon_prime_element = browser.find_element(By.XPATH, "//img[@alt='Netflix']")
        if amazon_prime_element:

    except Exception:
        print(f"{movie} is not available on Amazon Prime Video.")

    try:
        amazon_prime_element = browser.find_element(By.XPATH, "//img[@alt='Jio Cinema']")
        if amazon_prime_element:

    except Exception:
        print(f"{movie} is not available on Amazon Prime Video.")

    try:
        amazon_prime_element = browser.find_element(By.XPATH, "//img[@alt='Zee5']")
        if amazon_prime_element:

    except Exception:
        print(f"{movie} is not available on Amazon Prime Video.")

    try:
        amazon_prime_element = browser.find_element(By.XPATH, "//img[@alt='Sony Liv]")
        if amazon_prime_element:

    except Exception:
        print(f"{movie} is not available on Amazon Prime Video.")
    # Close the current tab
    browser.close()
    number_of_movies-=1
    # Switch back to the original tab
    browser.switch_to.window(browser.window_handles[0])