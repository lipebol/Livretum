import os
import textwrap
import requests
from PIL import Image

def extractOne(data, n, headers):

    wrapperI = textwrap.TextWrapper(width=42)
    wrapperII = textwrap.TextWrapper(width=35)

    URL_book = data['items'][n]['selfLink'] + "?fields=volumeInfo"
    selector = data['items'][n]['volumeInfo']
    if 'subtitle' not in selector:
        title = "".join(data['items'][n]['volumeInfo']['title'])
    else:
        title = data['items'][n]['volumeInfo']['title'],"-", data['items'][n]['volumeInfo']['subtitle']
        title = " ".join(title)
        title = wrapperI.fill(text=title)
        title = "".join(title)
    if 'authors' not in selector:
        authors = None
    else:
        authors = ", ".join(data['items'][n]['volumeInfo']['authors'])
        authors = wrapperII.fill(text=authors)
        authors = "".join(authors)
    if 'imageLinks' not in selector:
        image = 'app/src/images/noimage.png'
    else:
        URL_image = data['items'][n]['volumeInfo']['imageLinks']['smallThumbnail']
        r = requests.get(url=URL_image, headers=headers, stream=True)
        if r.status_code == 200:
            with open('app/src/images/book.jpeg', 'wb') as image:
                image.write(r.content)
            image = Image.open('app/src/images/book.jpeg')
            image.save('app/src/images/book.png')
            os.remove('app/src/images/book.jpeg')
            if image.size[0] != 128 or image.size[1] < 155:
                image = 'app/src/images/noimage.png'
            else:
                image = 'app/src/images/book.png'
    
    return URL_book, title, authors, image