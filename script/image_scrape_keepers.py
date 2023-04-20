import requests
from bs4 import BeautifulSoup
import os
league_ids = [[13,2],[53,2],[31,2],[19,2],[16,2]] #futhead league IDs and how many pages of results for each league
for j in range(0,5):
    for i in range(1,league_ids[j][1]+1):
        # URL of the webpage to scrape
        url = "https://www.futhead.com/22/players/?group=gk&club=all&league="+str(league_ids[j][0])+"&page="+str(i)+"&level=all_nif"

        # Send a request to the webpage and get the HTML response
        response = requests.get(url)

        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all image tags in the HTML
        img_tags = soup.find_all('img')

        # Create a directory to store the images
        if not os.path.exists('../data/images/players'):
            os.makedirs('../data/images/players')

        # Loop through each image tag and download the image
        for img in img_tags:
            try:
                img_url = img['data-src'] #player images stores in the data-src tag
            except KeyError:
                continue
            if 'http' not in img_url:
                # if the image URL doesn't have the http/https prefix, append it
                img_url = '{}{}'.format(url, img_url)

            if "players" in img_url: #catch in case it attempts to download a club logo or flag instead

                # Get the name of the image from the alt text
                img_name = img.get('alt')
                img_name = img_name[:-3]
                # Download the image and save it with the new name
                img_data = requests.get(img_url).content
                with open('../data/images/players/{}.png'.format(img_name), 'wb') as f:
                    f.write(img_data)
