from bs4 import BeautifulSoup
import re

class extract():
    def url_extract(self, html_content):
        self.html_content = html_content
        soup = BeautifulSoup(html_content, 'html.parser')
        links_info = []  # List to store information about each link
        for link in soup.find_all('a'):
            href_value = str(link.get('href'))  # Extract href
            link_text = link.text.strip()  # Extract text and strip whitespace
            if re.search(r'https?://', href_value):
                links_info.append({'href': href_value, 'text': link_text})  # Store in a dictionary
            else:
                continue
        
        return links_info
    
    def url_extract_less(self, html_content):
        self.html_content = html_content
        soup = BeautifulSoup(html_content, 'html.parser')
        links_info = []  # List to store information about each link
        for link in soup.find_all('a'):
            href_value = str(link.get('href'))  # Extract href
            if re.search(r'https?://', href_value):
                links_info.append(href_value)  # Store in a dictionary
            else:
                continue
        
        return links_info