import os
import json
import requests
from PIL import Image


def get_imgur_client_id():
    """
     gets the imgur client id key from config.txt file.
    """
    with open('config.txt', 'r') as f:
        client_id = f.read()

    return client_id

def create_download_dir():
    """
    creates a download directory for images.
    """
    dir_images = os.path.join('images')

    if not os.path.exists(dir_images):
        os.mkdir(dir_images)

    return dir_images


def download_image_from_url(url, directory):
    """
    download image and save into given directory.
    """
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filename = os.path.basename(url)
        filepath = os.path.join(directory, f'{filename}')
        with open(filepath, 'wb') as f:
            f.write(response.content)
    

def build_link_list(client_id, num_of_images):
    """
    builds a list of image links.
    """
    i = 1
    cnt = 0
    url_list = []
    url_list_len = []

    try:
        while(cnt < num_of_images):
            # get request
            response = requests.get(
                f'https://api.imgur.com/3/gallery/random/random/{i}', 
                headers={'Authorization': f'Client-ID {client_id}'},
                stream=True
            )
            
            # control
            if response.status_code == 200:
                data_list = json.loads(response.content)['data']
                url_list.extend([
                    i['link']
                    for i in data_list 
                    if 'type' in i 
                    and i['type'] in ('image/png', 'image/jpeg')
                    and i['link'] not in url_list
                ])

                cnt = len(url_list)
                url_list_len.append(cnt)
                i += 1
                
                # control if api doesn't return anything new
                if set(url_list_len[-10:]) == 1:
                    break
            
            elif response.status_code == 429:
                print('too many requests, enough, or you can choose to put time.sleep() in here...') 
                break

            else:
                break

    except:
        print('api limit reached!')
        
    
    return url_list


def create_thumbnail(size, path):
    """
    create resized version of the image path given, with the same name 
    extended with _thumbnail.
    """
    try:
        # create thumbnail
        image = Image.open(path)
        image.thumbnail(size)

        # create path for thumbnail
        dir_images = os.path.join(path)
        filename, extension = os.path.splitext(path)
        new_filename = os.path.join('{}{}{}'.format(filename, '_thumbnail', extension))

        # save thumbnail
        image.convert('RGB').save(new_filename)
    except:
        'image error'