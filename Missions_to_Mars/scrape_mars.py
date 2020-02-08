# Dependencies
import time
from bs4 import BeautifulSoup 
from splinter import Browser
from selenium.webdriver.common.by import By
import pandas as pd


def scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    time.sleep(3)
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(4)

    # Create a dictionary for all of the scraped data
    mars_data = {}


    # NASA Mars News
    nasa_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_news_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # The latest Mars news
    article = soup.find("div", class_="list_text")
    date = article.find("div", class_="list_date").text
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_="article_teaser_body").text 
  
    # Add the news date, title and paragraph to the dictionary
    mars_data["date"] = date
    mars_data["news_title"] = news_title
    mars_data["news_p"] = news_p



    # JPL Mars Space Images - Featured Image
    space_image_url = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(space_image_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    full_image = browser.find_by_id("full_image")
    full_image.click()
    time.sleep(3)
    browser.find_link_by_partial_text("more info").click()
    time.sleep(3)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # Full image
    image = soup.find('img', class_="main_image")["src"]
    image_url = "https://jpl.nasa.gov"+image
    featured_image_url = image_url

    # Add the featured image url to the dictionary
    mars_data["featured_image_url"] = featured_image_url



    # Mars Weather
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    tweet = soup.find("div", {"data-testid" : "tweet"}).find('div', {"lang" : "en"}).find('span').text
    
    # Add the Mars weather
    mars_data["tweet"] = tweet



    # Mars Facts
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    mars_facts=pd.read_html(facts_url)
    mars_info=pd.DataFrame(mars_facts[0])
    mars_info.columns=["Description","Value"]
    mars_table=mars_info.set_index("Description")
    marsinformation = mars_table.to_html(classes='marsinformation')
    marsinformation =marsinformation.replace('\n', ' ')

    # Add the Mars facts table to the dictionary
    mars_data["mars_table"] = marsinformation



    # Mars Hemispheres
    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemisphere_img_urls = []

    # Cerberus
    browser.find_link_by_partial_text("Cerberus Hemisphere Enhanced").click()
    time.sleep(3)
    full_image = browser.find_by_id("wide-image-toggle")
    full_image.click()
    time.sleep(3)
    cerberus_image = browser.html
    soup = BeautifulSoup(cerberus_image, 'html.parser')
    image = soup.find("img", class_="wide-image")['src']
    cerberus_img_url = "https://astrogeology.usgs.gov" + image
    print(cerberus_img_url)
    cerberus_title = soup.find("h2", class_="title").text
    print(cerberus_title)
    cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
    hemisphere_img_urls.append(cerberus)
    # back_button 
    browser.back()  

    # Schiaparelli
    browser.find_link_by_partial_text("Schiaparelli Hemisphere Enhanced").click()
    time.sleep(3)
    full_image = browser.find_by_id("wide-image-toggle")
    full_image.click()
    time.sleep(3)
    schiaparelli_image = browser.html
    soup = BeautifulSoup(schiaparelli_image, 'html.parser')
    image = soup.find("img", class_="wide-image")['src']
    schiaparelli_img_url = "https://astrogeology.usgs.gov" + image
    print(schiaparelli_img_url)
    schiaparelli_title = soup.find("h2", class_="title").text
    print(schiaparelli_title)
    schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
    hemisphere_img_urls.append(schiaparelli)
    # back_button 
    browser.back()
    
    # Syrtis
    browser.find_link_by_partial_text("Syrtis Major Hemisphere Enhanced").click()
    time.sleep(3)
    full_image = browser.find_by_id("wide-image-toggle")
    full_image.click()
    time.sleep(3)
    syrtis_image = browser.html
    soup = BeautifulSoup(syrtis_image, 'html.parser')
    image = soup.find("img", class_="wide-image")['src']
    syrtis_img_url = "https://astrogeology.usgs.gov" + image
    print(syrtis_img_url)
    syrtis_title = soup.find("h2", class_="title").text
    print(syrtis_title)
    syrtis = {"image title":syrtis_title, "image url": syrtis_img_url}
    hemisphere_img_urls.append(syrtis)
    # back_button 
    browser.back()

    # Valles
    browser.find_link_by_partial_text("Valles Marineris Hemisphere Enhanced").click()
    time.sleep(3)
    full_image = browser.find_by_id("wide-image-toggle")
    full_image.click()
    time.sleep(3)
    valles_image = browser.html
    soup = BeautifulSoup(valles_image, 'html.parser')
    image = soup.find("img", class_="wide-image")['src']
    time.sleep(3)
    valles_img_url = "https://astrogeology.usgs.gov" + image
    print(valles_img_url)
    valles_title = soup.find("h2", class_="title").text
    time.sleep(3)
    print(valles_title)
    valles = {"image title":valles_title, "image url": valles_img_url}
    hemisphere_img_urls.append(valles)

    mars_data['hemisphere_img_urls'] = hemisphere_img_urls
    browser.quit()
    # Return the dictionary
    return mars_data