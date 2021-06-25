""" Use to dowload data file from Drive 
"""

import requests
import logging
import zipfile
import os

logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(filename)s -   %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
        level=logging.INFO)

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":
    file_id = '0BzQ6rtO2VN95a0c3TlZCWkl3aU0'
    name = "finished_files.zip"
    destination = 'data/finished_files.zip'
    
    if os.path.exists(os.path.join('data/', name)):
        logging.info(f"Path {os.path.exists(os.path.join('data/', name))} already exists.")
        logging.info(f'Skipped download of {name} model.')
    else:
        os.makedirs(os.path.join('data/'), exist_ok=True)
        logging.info(f'Downloading {name} (~958MB folder) preprocessed vertion of CNN/DailyMail data set')
        download_file_from_google_drive(file_id, destination)

    if not os.path.exists(os.path.join('data/', name.split('.')[0])):
        folder = 'data/' + name.split('.')[0] +'/'
        with zipfile.ZipFile(destination, 'r') as zip_ref:
            logging.info(f'Extracting {destination} to {folder}')
            zip_ref.extractall('data/')