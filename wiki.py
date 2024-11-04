import requests
from bs4 import BeautifulSoup

# Making a GET request to fetch the HTML content of the Wikipedia page
r = requests.get('https://en.wikipedia.org/wiki/Kenya')

# Check if the request was successful
if r.status_code == 200:
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # Finding the main content section
    article_content = soup.find('div', class_='mw-body-content')
    
    # Extracting all paragraphs from the article content
    paragraphs = article_content.find_all('p')
    
    # Printing each paragraph's text
    for paragraph in paragraphs:
        print(paragraph.get_text())
else:
    print(f"Failed to retrieve the page. Status code: {r.status_code}")
