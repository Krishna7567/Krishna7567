# pyweather
Config files for my GitHub profile.
Using Python Web Scraping
Scrapping Weather prediction Data using Python and BS4
Last Updated : 29 Dec, 2020
This article revolves around scrapping weather prediction d data using python and bs4 library. Let’s checkout components used in the script –

BeautifulSoup– It is a powerful Python library for pulling out data from HTML/XML files. It creates a parse tree for parsed pages that can be used to extract data from HTML/XML files.
Requests – It is a Python HTTP library. It makes HTTP requests simpler. we just need to add the URL as an argument and the get() gets all the information from it.

We will be scrapping data from https://weather.com/en-IN/weather/tenday/l/INKA0344:1:IN.
Step 1 – Run the following command to get the stored content from the URL into the response object(file):
