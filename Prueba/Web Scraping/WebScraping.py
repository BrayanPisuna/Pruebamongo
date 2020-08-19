import requests
from bs4 import BeautifulSoup
# Import MongoClient from pymongo so we can connect to the database
from pymongo import MongoClient




if __name__ == '__main__':
    # Instantiate a client to our MongoDB instance
    db_client = MongoClient()
    bdd3 = db_client. bdd3
    bdd3 =  bdd3


    response = requests.get("https://blogs.futbolred.com/ ")
    soup = BeautifulSoup(response.content, "lxml")

    post_titles = soup.find_all("a", itemprop="url")

    extracted = []
    for post_title in post_titles:
        extracted.append({
            'title' : post_title.text,
            'link'  : "blogs.futbolred.com" + post_title['href']
        })

    # Iterate over each post. If the link does not exist in the database, it's new! Add it.
    for post in extracted:
        if db_client.bdd3. bdd3.find_one({'link': post['link']}) is None:
            # Let's print it out to verify that we added the new post
            print("Found a new listing at the following url: ", post['link'])
            db_client.bdd3.bdd3.insert(post)