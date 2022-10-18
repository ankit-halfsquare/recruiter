
import os
import re
import docx
import PyPDF2
# import textract
from dotenv import load_dotenv
from django.conf import settings
from azure.storage.blob import BlobClient
from azure.storage.fileshare import ShareFileClient

load_dotenv()

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

    if file_extension == ".docx":
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)
        

    if file_extension == ".txt":
        with open(f"{filename}") as f:
            text = f.readlines()
            text = '\n'.join(text)
        return text


def get_file_client(file):
    file_client = ShareFileClient.from_connection_string(
        conn_str=os.getenv('connection_string'),
        share_name=os.getenv('share_name'),
        file_path=f"{file}.pdf")

    return file_client


def get_blob(filename):
    # print("os.getenv('account_url')", os.getenv('account_url'))
    blob = BlobClient(account_url="https://recruiterstorageacc.blob.core.windows.net",
                      container_name=settings.AZURE_CONTAINER,
                      blob_name=f"{filename}",
                      credential=settings.AZURE_ACCOUNT_KEY)
    return blob


def dowload_file(filename, blob):
    with open(f"{filename}", "wb") as download_file:
        download_file.write(blob.download_blob().readall())


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
    blob = get_blob(filename)
    dowload_file(filename, blob)
    text = getText(filename)
    textlst = str_to_list(text)
    delete_file(filename)

    return text, textlst
    pass
