import requests
from bs4 import BeautifulSoup
import re

URLS = {
    "Drama": 'https://www.imdb.com/search/title/?title_type=feature&genres=drama',
    "Action": 'https://www.imdb.com/search/title/?title_type=feature&genres=action',
    "Comedy": 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy',
    "Horror": 'https://www.imdb.com/search/title/?title_type=feature&genres=horror',
    "Crime": 'https://www.imdb.com/search/title/?title_type=feature&genres=crime',
    "Romance": 'https://www.imdb.com/search/title/?title_type=feature&genres=romance',
    "History": 'https://www.imdb.com/search/title/?title_type=feature&genres=history',
    "Animation": 'https://www.imdb.com/search/title/?title_type=feature&genres=animation',
    
}

def main(emotion):
    url = URLS.get(emotion)
    print("ok", url)
    if not url:
        print('Invalid emotion.')
        return []
    
    headers = {
        'User Agent':
        'Chrome/138.0.7204.184'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'lxml')
    
    titles = [a.get_text() for a in soup.find_all('a', herf=re.compile(r'/title/tt\d+/'))]
    return titles

if __name__ == '__main__':
    emotion = input("Enter your Faaz: ").strip()
    movie_titles = main(emotion)
    
    if not movie_titles:
        print("No titles found.")
    else:
        max_titles = 14 if emotion in ['Drama', 'Action', 'Comedy', 'Horror', 'Crime', 'Romance', 'History', 'Animation'] else 12
        for title in movie_titles[:max_titles]:
            print(title)