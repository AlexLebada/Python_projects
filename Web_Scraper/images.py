import os

from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def Search():
    search = input("Search for:")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir("./scraped_images/"+ dir_name):
        os.makedirs("./scraped_images/"+ dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("img", {"class": "mimg"})

    i = 0
    for item in links[:5]:
        i += 1
        try:
            img_url = item.attrs.get("src")
            if not img_url:
                continue

            img_obj = requests.get(img_url)
            img = Image.open(BytesIO(img_obj.content))
            title = f"{search}_{i}.{img.format.lower()}"
            file_path = os.path.join("./scraped_images/"+ dir_name + "/", title)
            img.save(file_path, img.format)

        except Exception as e:
            print(e)
            print(f"Could not save image:")

    Search()

Search()