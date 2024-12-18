# Wikipedia Kenya Article Scraper
This project contains a Python script that retrieves the main article content from the Wikipedia page for Kenya. It uses requests to fetch the page's HTML content and BeautifulSoup for parsing and extracting paragraphs from the article.

## Table of Contents

Description
System Requirements
Installation
Clone Repository
Download ZIP
Usage
Code Explanation

## Description
The script retrieves and parses the HTML content of Wikipedia's Kenya article, extracting paragraphs from the main content section. It checks for a successful HTTP response, and if successful, retrieves the article's main text and outputs it to the console.

## System Requirements
To run this script, you need:

Python 3.6 or higher
requests and BeautifulSoup4 libraries
You can install the necessary libraries via pip:

        pip install requests beautifulsoup4


## Installation
You can set up this project by either cloning the repository or downloading the files manually.

Clone Repository
Open a terminal or command prompt.
Use the following git command to clone the repository:


        git clone https://github.com/your-username/repository-name.git
Navigate to the cloned directory:


        cd repository-name


Go to the repository page on GitHub.
Click on the Code button and select Download ZIP.
Extract the ZIP file to a desired location.

Open a terminal and navigate to the extracted directory:


        cd path/to/extracted-folder


### Usage

After navigating to the project directory, you can run the script with:

        python wiki_scraper.py
