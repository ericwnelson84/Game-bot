from selenium import webdriver

chrome_driver_path = 'C:/Users/eric/OneDrive/Desktop/Python/Day48-selenium-Webdriver-and-game-playing-bot/chromedriver/chromedriver.exe'
driver = webdriver.Chrome()

driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element_by_css_selector('#articlecount a')

# print(article_count)
# .encode("utf-8")
# executable_path=r"C:\path\to\chromedriver.exe"
# 'C:\Users\eric\OneDrive\Desktop\Python\Day48-selenium-Webdriver-and-game-playing-bot\chromedriver\chromedriver.exe'