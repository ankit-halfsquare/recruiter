import docx
from django.conf import settings 

import os
from dotenv import load_dotenv
load_dotenv()

from azure.storage.blob import BlobClient
from azure.storage.fileshare import ShareFileClient


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def get_file_client(file):
    file_client = ShareFileClient.from_connection_string(
                conn_str=os.getenv('connection_string'), 
                share_name=os.getenv('share_name'),
                file_path=f"{file}.pdf")

    return file_client


def get_blob(filename):
    print("os.getenv('account_url')",os.getenv('account_url'))
    blob = BlobClient(account_url="https://recruiterstorageacc.blob.core.windows.net",
                    container_name=settings.AZURE_CONTAINER,
                    blob_name=f"{filename}",
                    credential=settings.AZURE_ACCOUNT_KEY)
    return blob



def dowload_file(filename,blob):
    with open(f"{filename}", "wb") as download_file:
                download_file.write(blob.download_blob().readall())

def delete_file(filename):
    try:
        os.remove(filename)
    except :
        pass

def str_to_list(text):
    text = text.lower()
    text = text.replace("\n","")
    text = text.replace("\t","")
    text = list(text.split(" "))
    return text

def read_file(filename):
    blob = get_blob(filename)
    dowload_file(filename,blob)
    text = getText(filename)
    textlst = str_to_list(text)
    delete_file(filename)

    return text,textlst
    pass