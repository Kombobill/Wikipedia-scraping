## Wikipedia Kenya Article Scraper
This project contains a Python script that retrieves the main article content from the Wikipedia page for Kenya. It uses requests to fetch the page's HTML content and BeautifulSoup for parsing and extracting paragraphs from the article.

Table of Contents
Description
System Requirements
Installation
Clone Repository
Download ZIP
Usage
Code Explanation
Description
The script retrieves and parses the HTML content of Wikipedia's Kenya article, extracting paragraphs from the main content section. It checks for a successful HTTP response, and if successful, retrieves the article's main text and outputs it to the console.

System Requirements
To run this script, you need:

Python 3.6 or higher
requests and BeautifulSoup4 libraries
You can install the necessary libraries via pip:

bash
Copy code
pip install requests beautifulsoup4
Installation
You can set up this project by either cloning the repository or downloading the files manually.

Clone Repository
Open a terminal or command prompt.
Use the following git command to clone the repository:
bash
Copy code
git clone https://github.com/your-username/repository-name.git
Navigate to the cloned directory:
bash
Copy code
cd repository-name
Download ZIP
Go to the repository page on GitHub.
Click on the Code button and select Download ZIP.
Extract the ZIP file to a desired location.
Open a terminal and navigate to the extracted directory:
bash
Copy code
cd path/to/extracted-folder
Usage
After navigating to the project directory, you can run the script with:

bash
Copy code
python wiki_scraper.py
Code Explanation
Here's a breakdown of what each section in the script does:

python
Copy code
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
This script:

Fetches the HTML content of the Kenya article.
Parses the HTML to locate the main content area.
Extracts paragraphs from the main content.
Prints each paragraph’s text, giving the article's main content as output.
