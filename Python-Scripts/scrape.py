import re
from PIL import Image
import requests
from bs4 import BeautifulSoup
import os
import json
from io import BytesIO

list = ['Grain+Processing+Machine', 'Tillers+and+Cultivator', 'Brush+Cutter+and+Accessories', 'Chaff+Cutter',
        'Sprayers', 'Chain+Saw', 'Water+Pump+Sets', 'Lawn+Mower', 'Earth+Auger', 'Seed+Planter', 'Garden+Hand+Tools',
        'Fertilizer+and+Pest+Control', 'Fogging+Machine', 'Garden+Hoe', 'Harvester', 'Pest+and+Animal+Repellant',
        'Petrol+Blower', 'Shredder', 'Sprinklers', 'Hedge+Trimmer', 'Watering+Systems', 'Blowers', 'Stacking+Pots',
        'Agriculture+Implements', 'Pruning+Tools', 'Weed+Control+Mats', 'Plant+Containers', 'Artificial+Grass',
        'Gang+Mowers', 'Garden+Roller', 'Rotary+Slashers', 'Trailing+Seat', 'Flower+Pots', 'Pulverizer+Machine',
        'Gardening+Accessories', 'Pruners', 'Weeding+Fork', 'Planters']


# Function to download an image
def download_image(url, save_directory):
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split("/")[-1]
        save_path = os.path.join(save_directory, filename)

        # Convert JPG to WebP
        image = Image.open(BytesIO(response.content))
        webp_save_path = os.path.splitext(save_path)[0] + '.webp'
        image.save(webp_save_path, 'WebP', lossless=True)
        print("Image saved as WebP:", os.path.basename(webp_save_path))
    else:
        print("Failed to download the image.")


for i in list:
    result_url = "https://dir.indiamart.com/search.mp?ss=" + i + "&prdsrc=1&stype=attr=1|attrS&res=RC4"

    j = i.replace("+", " ")

    # Directory to save the images
    save_directory = "/home/aswin/Downloads/hh/" + j + "/"

    # Create the save directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Send a GET request to the result page
    response = requests.get(result_url)
    pattern = r'window\.__INITIAL_DATA__ = (.*?)};'

    # Find the matched string using regex

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the JSON data from the script tag
        script_tag = soup.findAll("script")
        # print(script_tag)
        for script in script_tag:
            if "window.__INITIAL_DATA__" in script.text:
                # print(script.text)
                match = re.search(pattern, script.text)

                if match:
                    matched_string = match.group(1)
                    matched_string = matched_string + "}"
                    json_data = json.loads(matched_string)
                    for product in json_data['catwidgetData']:
                        pdt = product['breadcrumb']
                        pattern = r"'mediumimg': '([^']+)'"

                        # Find all matches using the pattern
                        matches = re.findall(pattern, str(pdt))

                        # Access the mediumimg values
                        for mediumimg in matches:
                            download_image(mediumimg, save_directory)
