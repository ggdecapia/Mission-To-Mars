from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "c:/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    #########################
    # Scrape NASA Mars News #
    #########################
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(2)

    html = browser.html
    mars_news_soup = bs(html, "html.parser")

    latest_news = mars_news_soup.find('div', class_="bottom_gradient")
    news_title = latest_news.find('h3').text
    
    news_div = mars_news_soup.find('div', class_="image_and_description_container")
    news_div_inner = news_div.find('div', class_="rollover_description_inner")
    news_p = news_div.find('div', class_="rollover_description_inner").text

    #################################################
    # Scrape JPL Mars Space Images - Featured Image #
    #################################################
    url = 'https://www.jpl.nasa.gov/spaceimages/'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    JPL_mars = bs(html, "html.parser")

    full_image_button = browser.links.find_by_partial_text('FULL IMAGE')
    full_image_button.click()
    time.sleep(1)

    html = browser.html
    full_image_page = bs(html, "html.parser")

    image_div = full_image_page.find('div', class_="carousel_items")
    image_article = full_image_page.find('article', class_="carousel_item")
    image_div = full_image_page.find('div', id="fancybox-lock")
    img_class = image_div.find('img')
    src = img_class.get('src')
    featured_image_url = 'https://www.jpl.nasa.gov' + src

    ###################################
    # Scrape Space Facts - Mars Facts #
    ###################################
    mars_df = pd.read_html("https://space-facts.com/mars/")[0]
    mars_df = mars_df.rename(columns={0:"Description", 
                                      1:"Value"})
    mars_df.set_index("Description", inplace=True) 
    mars_html = mars_df.to_html(classes="table table-striped")
    
    ###########################
    # Scrape Mars Hemispheres #
    ###########################
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    mars_hemispheres = bs(html, "html.parser")

    hemispheres_div = mars_hemispheres.find_all('div', class_="item")
    hemispheres = []
    hemispheres = hemispheres_div
    hemisphere_urls = []
    
    for i in range(len(hemispheres)):
        hemisphere = {}
        a = hemispheres[i].find('a')
        href = a.get('href')
        url = 'https://astrogeology.usgs.gov' + href
        browser.visit(url)

        html = browser.html
        hemispheres_full_img = bs(html, "html.parser")

        sample = browser.links.find_by_text("Sample").first
        hemisphere["img_url"] = sample["href"]
        hemisphere["title"] = hemispheres_full_img.find('h2', class_="title").text
        
        hemisphere_urls.append(hemisphere)

    # Store scraped data into a dictionary
    scraped_mars_data = {
        "mars_news_title": news_title,
        "mars_news_paragraph": news_p,
        "mars_featured_image": featured_image_url,
        "mars_facts": mars_html,
        "mars_hemispheres": hemisphere_urls
    }
    
    print('hemisphere_urls')
    print(hemisphere_urls)
    # Close the browser after scraping
    browser.quit()

    # Return results
    return scraped_mars_data
