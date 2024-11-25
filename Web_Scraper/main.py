from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
# .find() search for first result of "ol" instance/element with attribute "id"
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)

        if 1==1 :
            print("Parent:", item.find("a").parent)
            print("Summary:", item.find("a").parent.parent.find("p").text)
            # find children of that parent element, in this case one of the "li" elements that is extracted
            children = item.children
            for child in children:
                print("Child:", child)
            # find next element near searched element
            children = item.find("h2")
            print("Next sibling of the h2:", children.next_sibling)

