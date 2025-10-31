import requests
from bs4 import BeautifulSoup

# List of keywords to search
keywords = ['keyword1', 'keyword2', 'keyword3']

# List of URLs to check
urls = [
    'https://isc.sans.edu/',
    'https://www.troyhunt.com/',
    'https://blog.didierstevens.com/',
    'https://www.sans.org/reading-room/popular/week',
    'https://www.darkreading.com/',
    'https://www.fireeye.com/current-threats/threat-intelligence-reports.html',
    'https://www.fireeye.com/blog/threat-research.html',
    'https://www.fireeye.com/current-threats/apt-groups.html',
    'https://thehackernews.com/',
    'https://portswigger.net/daily-swig',
    'https://www.ibm.com/security/data-breach/threat-intelligence',
    # 'https://redcanary.com/threat-detection-report/', # failing to fetch
    'https://threatpost.com/',
    'https://www.cyberscoop.com/',
    'https://thisweekin4n6.com/',
    'https://googleprojectzero.blogspot.com/'
]

# Fetch the news titles from the url
def fetch_urls(url):
  
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page content: {response.status_code}")
    
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Assuming the news titles are within <h2> tags with class 'home-title'
    titles = soup.find_all('h2', class_='home-title')
    
    news_titles = [title.get_text().strip() for title in titles]
    
    return news_titles

# Check for keyword match
def check_for_keywords(titles, keywords):

    matching_titles = []
    
    for title in titles:
        for keyword in keywords:
            if keyword.lower() in title.lower():
                matching_titles.append(title)
                break  # No need to check other keywords if one is found
    
    return matching_titles

def main():
    try:
        for url in urls:
            print(f"Checking news titles from: {url}")
            titles = fetch_urls(url)
            matching_titles = check_for_keywords(titles, keywords)
            
            if matching_titles:
                print("News titles containing the specified keywords:")
                for title in matching_titles:
                    print(f"- {title}")
            else:
                print("No news titles found containing the specified keywords.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()




# Check if working properly in all sites, particularly due to assumption of news titles as 'h2' 'home-title'