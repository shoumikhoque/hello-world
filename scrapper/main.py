import requests
from bs4 import BeautifulSoup
import pdfkit
def fetch_chapter(chapter_number):
    # URL of the webpage
    url = f"https://xperimentalhamid.com/novels/millionaire-son-in-law-novel-chapter-{chapter_number}/"
    # Send a GET request to fetch the page content
    response = requests.get(url)
    print(f'response:{response.status_code} found from {url}')
    if response.status_code == 200:
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', class_='entry-content')
        content_string = f'</h1><b>Chapter {chapter_number}</b></h1><div>\n'
        if content:
            paragraphs = content.find_all('p')
            paragraphs=paragraphs[1:]
            for p in paragraphs:
                content_string += (("<p>") + p.text + ("</p>"))
            content_string += ("\n\n</div>")
            return content_string
    else:
        print("Failed to retrieve page. Status code:", response.status_code)
        return ''
if __name__ == '__main__':
    start=6751
    end=7000
    for i in range(start,end+1,100):
        st =i
        en=i+100
        chapter_data = ''
        for chapter_number in range(i,i+100):
            chapter_data+=(fetch_chapter(chapter_number))
        ebook_name=f"Chapter {i}-{i+99}.pdf"
        pdfkit.from_string(chapter_data,ebook_name , options={"encoding": "utf-8"})
        print(f"Generated PDF : {ebook_name}")

