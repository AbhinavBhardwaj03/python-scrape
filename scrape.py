import requests
from bs4 import BeautifulSoup
import pandas as pd

# define the URL to scrape
url = 'https://swiggy.com/restaurants/hungry-hope-rbi-flats-colony-kankarbagh-patna-152335'

# make a request to the URL and handle connection errors
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit()

# parse the HTML content using BeautifulSoup and handle parsing errors
try:
    soup = BeautifulSoup(response.content, 'html.parser')
except Exception as e:
    print(f"Error: {e}")
    exit()

# create empty lists to store the data
item_names = []
rupees = []

# find all elements with the class 'styles_itemNameText__3ZmZZ' and handle attribute errors
try:
    for item_name in soup.find_all(class_='styles_itemNameText__3ZmZZ'):
        item_names.append(item_name.text.strip())
except AttributeError as e:
    print(f"Error: {e}")
    exit()

# find all elements with the class 'rupee' and handle attribute errors
try:
    for rupee in soup.find_all(class_='rupee'):
        rupees.append(rupee.text.strip())
except AttributeError as e:
    print(f"Error: {e}")
    exit()

# create a pandas dataframe from the data
data = {
    'item_name': item_names,
    'rupee': rupees,
}

df = pd.DataFrame(data)

# print the dataframe
print(df)
