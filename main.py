import requests
from bs4 import BeautifulSoup



def print_unicode_grid(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the document")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table  = soup.find('table')
    content = []
    for row in table.find_all('tr'):
        columns = row.find_all(['td'])
        content.append([column.text for column in columns])
    
    points = [(int(row[0]), int(row[2]), row[1]) for row in content[1:]]
    # Determine grid size
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = char

    # Print the grid rotated
    for row in reversed(grid):
        print(''.join(row))

       
    

print_unicode_grid('https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub')
print_unicode_grid('https://docs.google.com/document/d/e/2PACX-1vSZ1vDD85PCR1d5QC2XwbXClC1Kuh3a4u0y3VbTvTFQI53erafhUkGot24ulET8ZRqFSzYoi3pLTGwM/pub')