import requests
from bs4 import BeautifulSoup
import pandas as pd

# define the URL to scrape
url = 'https://swiggy.com/restaurants/hungry-hope-rbi-flats-colony-kankarbagh-patna-152335'

# make a request to the URL
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# create empty lists to store the data
item_names = []
rupees = []
# image_srcs = []

# find all elements with the class 'styles_itemNameText__3ZmZZ'
for item_name in soup.find_all(class_='styles_itemNameText__3ZmZZ'):
    item_names.append(item_name.text.strip())

# find all elements with the class 'ruppee'
for rupee in soup.find_all(class_='rupee'):
    rupees.append(rupee.text.strip())

# create a pandas dataframe from the data
data = {
    'item_name': item_names,
    'rupee': rupees,
}

df = pd.DataFrame(data)

# print the dataframe
print(df)
