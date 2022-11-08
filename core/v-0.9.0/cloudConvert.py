import os
import cloudconvert

API_KEY = os.getenv('cloudConvert_API_KEY')

cloudconvert.configure(api_key=API_KEY, sandbox=False)


def convertAndDownloadFile(filename):
    
    job = cloudconvert.Job.create(payload={
        "tasks": {
            'import-my-file': {
                'operation': 'import/url',
                'url': f'https://recruiterstorageacc.blob.core.windows.net/demo/{filename}'
            },
            'convert-my-file': {
                'operation': 'convert',
                'input': 'import-my-file',
                'output_format': 'pdf',
                'some_other_option': 'value'
            },
            'export-my-file': {
                'operation': 'export/url',
                'input': 'convert-my-file'
            }
        }
    })

    job = cloudconvert.Job.wait(id=job['id'])

    for task in job["tasks"]:
        if task.get("name") == "export-my-file" and task.get("status") == "finished":
            export_task = task

    file = export_task.get("result").get("files")[0]

    fileName=file['filename']
    fileName = f'files/{fileName}'

    cloudconvert.download(filename=fileName, url=file['url'])

    return fileName


def downloadFile(fileName):
    URL = f"https://recruiterstorageacc.blob.core.windows.net/demo/{fileName}"
    cloudconvert.download(filename=fileName, url=URL)