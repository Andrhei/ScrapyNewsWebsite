from google.cloud import storage
from datetime import datetime

import os

os.environ.setdefault("GCLOUD_PROJECT", "my-project-1234")

BUKET_NAME="web-scraping-scrapy-bbc"
PATH_FILE=f'{os.getcwd()}\\ScrapyNewsWebsite\\json\\news_bbc.json'
BLOB_NAME=f'bbc/news_bbc{datetime.now()}.json'

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

upload_blob(BUKET_NAME, PATH_FILE, BLOB_NAME)