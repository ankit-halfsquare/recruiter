
import os
import re
import docx
import PyPDF2
# import textract
from dotenv import load_dotenv
from django.conf import settings
from azure.storage.blob import BlobClient,BlobServiceClient
from azure.storage.fileshare import ShareFileClient

load_dotenv()

connect_str = os.getenv('connection_string')
container_name = os.getenv('AZURE_CONTAINER')

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

def uploadFile(filename):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)
    with open(filename, "rb") as data:
        blob_client.upload_blob(data)


def getText(filename):
    file, file_extension = os.path.splitext(f"{filename}")
    if file_extension == ".pdf":
        pdfFileObj = open(f"{filename}", 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        n = pdfReader.numPages
        text = ""
        for i in range(n):
            pageObj = pdfReader.getPage(i)
            text += pageObj.extractText()
        return text

   



def delete_file(filename):
    try:
        os.remove(filename)
    except:
        pass


def str_to_list(text):
    text = text.lower()
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    text = list(text.split(" "))
    return text


def read_file(filename):
    text = getText(filename)
    textlst = str_to_list(text)
    delete_file(filename)

    return text, textlst
    


# def get_file_client(file):
#     file_client = ShareFileClient.from_connection_string(
#         conn_str=os.getenv('connection_string'),
#         share_name=os.getenv('share_name'),
#         file_path=f"{file}.pdf")

#     return file_client


# def get_blob(filename):
#     # print("os.getenv('account_url')", os.getenv('account_url'))
#     blob = BlobClient(account_url="https://recruiterstorageacc.blob.core.windows.net",
#                       container_name=settings.AZURE_CONTAINER,
#                       blob_name=f"{filename}",
#                       credential=settings.AZURE_ACCOUNT_KEY)
#     return blob


# def dowload_file(filename, blob):
#     with open(f"{filename}", "wb") as download_file:
#         download_file.write(blob.download_blob().readall())