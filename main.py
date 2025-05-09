import requests
from bs4 import BeautifulSoup

from collections import defaultdict

def print_unicode_grid(url):
    # Fetch the document content
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the document")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table  = soup.find('table')
    print(table)
    content = []
    for row in table.find_all('tr'):
        columns = row.find_all(['td'])
        content.append([column.text for column in columns])
    # print((content))
       
    

# Example usage:
print_unicode_grid('https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub')