import os
filename= "files\HelloWorld_5qguuat.docx"
filename, file_extension = os.path.splitext(f"{filename}")
print(filename)

# from PyPDF2 import PdfReader

# reader = PdfReader("files\HelloWorld_Yi1K5wC.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# print(number_of_pages)
# text = page.extract_text()
# print(text)


# from docx2pdf import convert

# file  = convert("files\HelloWorld_5qguuat.docx")

# print(file)
# # convert(r'https://recruiterstorageacc.blob.core.windows.net/demo/files/HelloWorld.docx')
# # convert('files/HelloWorld.docx')

# import os, uuid
# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


# from azure.storage.blob import BlobClient
# upload_file_path = r"files/ankitdemo.pdf"
# blob = BlobClient(account_url="https://recruiterstorageacc.blob.core.windows.net",
#                   container_name="demo",
#                   blob_name=upload_file_path,
#                   credential="TMIx6oaskIB8HdwDPCI4zBaYfxucJcSryzQTgaIpt8PwWs2+JzTXP3TNd9bwJwlz2uHUfZ8jgF5q+AStGCB1vA==")

# # # print(dir(blob))

# with open(upload_file_path, "rb") as data:
#     blob.upload_blob(data)

# with open("demo.docx", "wb") as download_file:
#     download_file.write(blob.download_blob().readall())
    

# connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
# container_name =""
# blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

# download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
# container_client = blob_service_client.get_container_client(container= container_name) 
# print("\nDownloading blob to \n\t" + download_file_path)

# with open(download_file_path, "wb") as download_file:
#  download_file.write(container_client.download_blob(blob.name).readall())