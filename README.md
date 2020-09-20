# web-scraping-challenge
Data bootcamp web scraping homework repository

Web Scraping Homework - Mission to Mars

In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

Before You Begin


Create a new repository for this project called web-scraping-challenge. Do not add this homework to an existing repository.


Clone the new repository to your computer.


Add your notebook files and flask app to this folder.


Push the above changes to GitHub or GitLab.



Step 1 - Scraping
Complete your initial scraping using a Jupyter Notebook, BeautifulSoup, Pandas, Requests, and Splinter.

Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.


NASA Mars News

Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."

JPL Mars Space Images - Featured Image


Visit the url for JPL Featured Space Image here.


Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.


Make sure to find the image url to the full size .jpg image.


Make sure to save a complete url string for this image.


# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'

Mars Facts


Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.


Use Pandas to convert the data to a HTML table.



Mars Hemispheres


Visit the USGS Astrogeology site here to obtain high resolution images for each of Mars's hemispheres.


You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.


Save the url string for the full resolution hemisphere image as well as the Hemisphere title containing the hemisphere name. Use a Python dictionary to store these values using the keys img_url and title.


Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]


Step 2 - MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.


Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.


Next, create a route called /scrape that will call your scrape_mars.scrape function. Note that you'll have to import scrape_mars.py.

Store the dictionary that gets returned to your MongoDB.



Create an index route / that will query your Mongo database and pass the Mars data into an HTML template to be displayed.


Create a template HTML file called index.html that will take the dictionary of Mars data and display its values in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.
Step 3 - Submission
To submit your work to BootCampSpot, create a new GitHub repository and upload the following:


The Jupyter Notebook containing the scraping code used.


Screenshots of your final application.


Then submit the link to this repository to BootCampSpot. Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

Hints


Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse the necessary data.


Use Pymongo for database CRUD operations. For this homework, you can simply overwrite the existing document each time the /scrape url is visited and new data is obtained.


Use Bootstrap to structure your HTML template.



Copyright
Trilogy Education Services © 2020. All Rights Reserved.