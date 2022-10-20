from dotenv import load_dotenv
from django.conf import settings
from azure.storage.blob import BlobClient,BlobServiceClient
from azure.storage.fileshare import ShareFileClient
import os

load_dotenv()

connect_str = os.getenv('connection_string')
container_name = os.getenv('AZURE_CONTAINER')

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
# container_client = blob_service_client.create_container(container_name)

def uploadFile(filename):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)
    with open(filename, "rb") as data:
        blob_client.upload_blob(data)



uploadFile("files/DAMINI BDE (1) (1).pdf")





# import cloudconvert

# cloudconvert.configure(api_key=API_KEY, sandbox=False)

# cloudconvert.download(filename="", url="https://recruiterstorageacc.blob.core.windows.net/demo/files/Starleen_Burton_Resume.docx")

# job = cloudconvert.Job.create(payload={
#      "tasks": {
#          'import-my-file': {
#               'operation': 'import/url',
#               'url': 'https://recruiterstorageacc.blob.core.windows.net/demo/files/Starleen_Burton_Resume.docx'
#          },
#          'convert-my-file': {
#              'operation': 'convert',
#              'input': 'import-my-file',
#              'output_format': 'pdf',
#              'some_other_option': 'value'
#          },
#          'export-my-file': {
#              'operation': 'export/url',
#              'input': 'convert-my-file'
#          }
#      }
#  })

# job = cloudconvert.Job.wait(id=job['id'])



# for task in job["tasks"]:
#     if task.get("name") == "export-my-file" and task.get("status") == "finished":
#         export_task = task

# file = export_task.get("result").get("files")[0]

# print("file",file)
# print("file",file['filename'])
# print("file",file['url'])
# cloudconvert.download(filename=file['filename'], url=file['url'])




# cloudconvert.Job.create(payload={
#     "tasks": {
#         'import-my-file': {
#             'operation': 'import/url',
#             'url': 'https://recruiterstorageacc.blob.core.windows.net/demo/files/Starleen_Burton_Resume.docx'
#         },
#         'convert-my-file': {
#             'operation': 'convert',
#             'input': 'import-my-file',
#             'output_format': 'pdf',
#             'some_other_option': 'value'
#         },
#         'export-my-file': {
#             'operation': 'https://recruiterstorageacc.blob.core.windows.net/demo/files/test.pdf',
#             'input': 'convert-my-file'
#         }
#     }
# })


# job = cloudconvert.Job.create(payload={
#      "tasks": {
#          'import-my-file': {
#               'operation': 'import/url',
#               'url': 'https://my.url/file.docx'
#          },
#          'convert-my-file': {
#              'operation': 'convert',
#              'input': 'import-my-file',
#              'input_format': 'docx',
#              'output_format': 'pdf'
#          },
#          'export-my-file': {
#              'operation': 'export/url',
#              'input': 'convert-my-file'
#          }
#      }
#  })




















# from bs4 import BeautifulSoup as bs
# soup = bs(open("files/Jyoti-Ranjan-kalta-Latest-Resume-_2_.doc", encoding="ISO-8859-1").read(), 'lxml')
# [s.extract() for s in soup(['style', 'script'])]
# tmpText = soup.get_text()
# text = "".join("".join(tmpText.split('\t')).split('\n')).strip()
# print("***")



# # def str_to_list(text):
# #     text = text.lower()
# #     text = text.replace("\n","")
# #     text = text.replace("\t","")
# #     text = list(text.split(" "))
# #     text = set(text)
# #     return text
# # text = str_to_list(text)
# print(text)

# # test = ['','']
# # test = set(test)
# # print('test',test)



# # import pypandoc
# # # from pypandoc.pandoc_download import download_pandoc
# # # download_pandoc()
# # # output = pypandoc.convert_text('# some title', 'rst', format='md')
# # pypandoc.convert_file('files/Fake Resume.docx', format='docx', to='pdf',outputfile='abc.pdf')
# # print(output)



# # import mammoth

# # with open("files/HimanshuResume.doc", "rb") as docx_file:
# #     result = mammoth.extract_raw_text(docx_file)
# #     text = result.value # The raw text
# #     with open('output.txt', 'w') as text_file:
# #         text_file.write(text)




# # import subprocess


# # def doc2pdf_linux(doc):
# #     """
# #     convert a doc/docx document to pdf format (linux only, requires libreoffice)
# #     :param doc: path to document
# #     """
# #     cmd = 'libreoffice --convert-to pdf'.split() + [doc]
# #     p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
# #     p.wait(timeout=10)
# #     stdout, stderr = p.communicate()
# #     if stderr:
# #         raise subprocess.SubprocessError(stderr)

# # doc2pdf_linux("files/Jyoti-Ranjan-kalta-Latest-Resume-_2_.doc")


# # import textract
# # text = textract.process("files/Fake-Resume.doc")

# # print(text)
# # 
# # # from pyresparser import ResumeParser

# # data = ResumeParser('files/DAMINI BDE (1) (1).pdf').get_extracted_data()
# # print(data)




# # from urllib.request import urlopen
# # from bs4 import BeautifulSoup
# # from io import BytesIO
# # from zipfile import ZipFile


# # document = ZipFile("files/DAMINI BDE (1) (1).pdf")
# # content = document.read('word/document.xml')
# # word_obj = BeautifulSoup(content.decode('utf-8'))
# # text_document = word_obj.findAll('w:t')
# # for t in text_document:
# #     print(t.text)









# # special_chars = {
# #     "b'\\t'": '\t',
# #     "b'\\r'": '\n',
# #     "b'\\x07'": '|',
# #     "b'\\xc4'": 'Ä',
# #     "b'\\xe4'": 'ä',
# #     "b'\\xdc'": 'Ü',
# #     "b'\\xfc'": 'ü',
# #     "b'\\xd6'": 'Ö',
# #     "b'\\xf6'": 'ö',
# #     "b'\\xdf'": 'ß',
# #     "b'\\xa7'": '§',
# #     "b'\\xb0'": '°',
# #     "b'\\x82'": '‚',
# #     "b'\\x84'": '„',
# #     "b'\\x91'": '‘',
# #     "b'\\x93'": '“',
# #     "b'\\x96'": '-',
# #     "b'\\xb4'": '´'
# # }


# # def get_string(path):
# #     string = ''
# #     with open(path, 'rb') as stream:
# #         stream.seek(2560) # Offset - text starts after byte 2560
# #         current_stream = stream.read(1)
# #         while not (str(current_stream) == "b'\\xfa'"):
# #             if str(current_stream) in special_chars.keys():
# #                 string += special_chars[str(current_stream)]
# #             else:
# #                 try:
# #                     char = current_stream.decode('UTF-8')
# #                     if char.isalnum():
# #                         string += char
# #                 except UnicodeDecodeError:
# #                     string += '--'
# #             current_stream = stream.read(1)
# #     return string



# # print(get_string("files/Jyoti-Ranjan-kalta-Latest-Resume-_2_.doc"))

# # import docx2txt


# # text = docx2txt.process("files/Fake_Resume_YlyT4SH.docx")
# # print(text)

# # with open('files/kisan-kumar-singh.doc',encoding='ISO-8859-1') as f:
# #     text = f.readlines()
# #     text = '\n'.join(text)


# # f = open('files/test.txt','w')
# # f.write(text)
# # f.close()


# # print("ankit*****")
# # print(text)


# # import os


# # filename = "DAMINI BDE (1) (1).pdf"

# # file, file_extension = os.path.splitext(f"{filename}")

# # print(file, file_extension)


# # import PyPDF2 

# # pdfFileObj = open('files/DAMINI BDE (1) (1).pdf', 'rb') 
# # pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# # n  = pdfReader.numPages
# # text  = ""
# # for i in range(n):
# #     pageObj = pdfReader.getPage(i) 
# #     text += pageObj.extractText()

# # print(text)




# # import docx2txt






# # text = docx2txt.process("files/Fake-Resume.doc")
# # # 

# # # print(text)
# # # text = text.decode("utf-8")
# # print(text)
