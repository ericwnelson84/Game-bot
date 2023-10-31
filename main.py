from selenium import webdriver
from selenium.webdriver.common.by import By

# use code below to keep browser window open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

# ######below is an example of using a webdriver on amazon to get the price ################
# driver.get('https://www.amazon.com/ASUS-Graphics-DisplayPortTM-Full-Coverage-Radiator/dp/B0C8X3RD63/ref=sr_1_1?crid='
#            '38FMAI3YIX9PC&keywords=nvidia+4090&qid=1693360511&sprefix=nvidia+4090%2Caps%2C134&sr=8-1&ufe=app_'
#            'do%3Aamzn1.fos.ac578592-0362-4e0a-958c-0f2dd61d30d4')
#
# price_dollar = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
# # price_cents = driver.find_element(By.CLASS_NAME, 'a-price-fraction').text
#
# print(f'The price is ${price_dollar}.{price_cents}')

######## below is an example of usign the webdriver on a python website ######
driver.get('https://www.python.org')
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar)
# print(search_bar.tag_name)
# print(search_bar.get_attribute('placeholder'))
#
# button = driver.find_element(By.ID, value='submit')
# print(button.text)
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a').text
# print(documentation_link)

### below we can search elements using XPATH. when inspecting a wep page in chrom you can right click and inspect
# teh element you want then right click in teh HTML code and copy XPATH then past that into your code as seen below
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[4]/a')
# print(bug_link.text)
# print(bug_link)

###### all the find methods above can work with find_elements with the s to find all the elements of a particular type

event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}

for time in event_times:
    print(time.text)

for name in event_names:
    print(name.text)

# putting everything in a dict

for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text,
    }

print(events)

# .close closes the current tab and .quit closes the entire browser
driver.close()
driver.quit()