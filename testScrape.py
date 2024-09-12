import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.cincinnatichildrens.org/health/d/diabetes-nutrition'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the sections you are interested in based on their HTML structure
sections = soup.find_all('div', class_='article health_body module _healthtopicarticle')

# Extract the content from each section
for section in sections:
    # Extract the section title
    title = section.find('h2').text.strip()
    print(f'Section: {title}\n')

    # Extract the section content
    content = section.find_all('p')
    for paragraph in content:
        print(paragraph.text.strip())
    print('\n')
