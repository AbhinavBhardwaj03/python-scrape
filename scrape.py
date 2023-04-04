import requests
from bs4 import BeautifulSoup
import pandas as pd

# define the URL to scrape
url = 'https://swiggy.com/restaurants/hungry-hope-rbi-flats-colony-kankarbagh-patna-152335'

try:
    # make a request to the URL and handle connection errors
    response = requests.get(url)

    # parses the HTML content of the response using the BeautifulSoup library and stores the result in the soup variable.
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser') 
except Exception as e:
    print(f"Error: {e}")
    exit()

# create empty lists to store the data
item_names = []
rupees = []

try:

    # find all elements with the class 'styles_itemNameText__3ZmZZ' and handle attribute errors

    for item_name in soup.find_all(class_='styles_itemNameText__3ZmZZ'):
        item_names.append(item_name.text.strip())

    # find all elements with the class 'rupee' and handle attribute errors

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
