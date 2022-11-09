from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.core.files.base import ContentFile,File

from datetime import datetime
from django.utils import timezone 
from tinymce.models import HTMLField

import os
from dotenv import load_dotenv
load_dotenv()

from .utils import *
from .cloudConvert import convertAndDownloadFile,downloadFile

# Create your models here.


class PowerSearch(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    query = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        managed = False
        db_table = 'keyword'


class Company(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'company'
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'project'

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'position'

    def __str__(self):
        return self.name


class Assignment(models.Model):
    project_division = models.CharField(max_length=255, blank=True, null=True)
    positionname = models.CharField(max_length=50, blank=True, null=True)
    desired_keywords = models.CharField(max_length=50, blank=True, null=True)
    target_start_date = models.DateField(null=True, blank=True)
    est_completion_date = models.DateField(null=True, blank=True)
    assigneeid = models.IntegerField(null=True, blank=True)
    actual_start_date = models.DateField(null=True, blank=True)
    active = models.IntegerField(null=True, blank=True)
    actual_completion_date = models.DateField(null=True, blank=True)
    assigner = models.CharField(max_length=128, null=True, blank=True)
    date_added = models.DateField(null=True, blank=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    statusid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.positionname

    class Meta:
        #managed = False
        db_table = 'assignment'


class CandidateStatus(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name_plural = "status"

    def __str__(self):
        return self.name

class CandidatePriority(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name_plural = "priority"
        
    def __str__(self):
        return self.name


class CandidateSkillLevel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Skill Level"

    def __str__(self):
        return self.name


class PlatformOrReferral(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Platform/Referral"

    def __str__(self):
        return self.name




class CandidateTable(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    history = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    active_assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE , blank=True, null=True )
    adder = models.IntegerField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True, blank=True, null=True)
    fk_ra_company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    fk_ra_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    fk_ra_position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)
    skill_keywords = models.TextField(blank=True, null=True)
    candidateFileName = models.CharField(max_length=255, blank=True, null=True)
    # candidateFileContents = models.TextField(blank=True, null=True)
    candidateFileContents = HTMLField(blank=True, null=True)
    candidateFileNameOriginal = models.FileField(upload_to='files/', blank=True, null=True)
    candidateFileNamePDF = models.CharField(max_length=255, null=True, blank=True)
    fileUploadDate = models.DateField(blank=True, null=True)
    candidateFileNameOriginalFull = models.CharField(max_length=255, null=True, blank=True)
    fileUploadUser = models.CharField(max_length=255, null=True, blank=True)
    archive = models.IntegerField(null=True, blank=True)
    skill_keywords_full = models.TextField(blank=True, null=True)

    year = models.IntegerField(blank=True,null=True)
    ww = models.IntegerField(blank=True,null=True)
    plateformOrReferral = models.ForeignKey(PlatformOrReferral, on_delete=models.CASCADE , blank=True, null=True )
    positionOrPerson = models.CharField(max_length=255,blank=True,null=True)
    refferedBy = models.CharField(max_length=255,blank=True,null=True)
    specialitySkillSet = models.CharField(max_length=255,blank=True,null=True)
    semi = models.CharField(max_length=255,blank=True,null=True)
    intel = models.CharField(max_length=255,blank=True,null=True)
    project1 = models.CharField(max_length=255,blank=True,null=True)
    project2 = models.CharField(max_length=255,blank=True,null=True)
    project3 = models.CharField(max_length=255,blank=True,null=True)
    status = models.ForeignKey(CandidateStatus,on_delete=models.CASCADE,blank=True,null=True)
    priority = models.ForeignKey(CandidatePriority,on_delete=models.CASCADE,blank=True,null=True)
    skillLevel = models.ManyToManyField(CandidateSkillLevel,blank=True,null=True)
    activity = models.TextField(blank=True,null=True)
    pay = models.TextField(blank=True,null=True)

    # def __str__(self):
    #     return self.first_name

    class Meta:
        #managed = False
        db_table = 'candidate_tbl'
        verbose_name_plural = "candidates"


    def save(self,*args, **kwargs):

        super().save(*args, **kwargs)

        if self.candidateFileNameOriginal and not self.candidateFileContents:
            filename = f"{self.candidateFileNameOriginal}"

            if ".pdf" in filename:
                downloadFile(filename)
            else:
                filename = convertAndDownloadFile(filename)
                uploadFile(filename)
                

            text,textlst = read_file(filename)
            

            try: 
                line = text.strip()
                emails = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+", line)
                if(len(emails) > 0):
                    self.email = emails[0]
            except Exception as e:
                print(e)

            self.candidateFileContents = text

            skills = Keyword.objects.all()
            skillfullkeywords=[]
            for skill in skills:
                skill = str(skill)
                if skill.lower() in textlst:
                    skillfullkeywords.append(skill)

            if len(skillfullkeywords):
                self.skill_keywords_full = ' '.join([str(elem) for elem in skillfullkeywords])

            file, file_extension = os.path.splitext(f"{filename}")
            self.candidateFileNamePDF = f"{file}.pdf"
            self.fileUploadDate = datetime.now().strftime('%Y-%m-%d')
            self.fileUploadUser = "comming soon"

            if not self.first_name and not self.last_name:
                self.first_name = file.split('/')[1].split('_')[0]
                self.last_name = file.split('/')[1].split('_')[1]
         
            self.save()

            # blob = get_blob(filename)

            # with open(f"{filename}", "wb") as download_file:
            #     download_file.write(blob.download_blob().readall())
            
            # text = getText(f"{filename}")
            # self.candidateFileContents = text

            # skills = Keyword.objects.all()
            # skillfullkeywords=[]
            # text = text.lower()
            # text = text.replace("\n","")
            # text = text.replace("\t","")
            # text = list(text.split(" "))
            # print("text",text)
            # for skill in skills:
            #     skill = str(skill)
            #     if skill.lower() in text:
            #         skillfullkeywords.append(skill)
                

            

            # pythoncom.CoInitialize()
            # convert(f"{filename}")

            # file, file_extension = os.path.splitext(f"{filename}")

            # file_client = get_file_client(file)
            # file_client.upload_file(f"{file}.pdf")

            # reader = PdfReader(f"{file}.pdf")
            # page = reader.pages[0]
            # text = page.extract_text()

            # self.candidateFileContents = text
            # self.candidateFileNamePDF = f"{file}.pdf"
            # try:
            #     os.remove(f"{file}.pdf")
            #     os.remove(filename)
            # except print(0):
            #     pass
            # self.save()
            

            # if not self.candidateFileNamePDF:
            #     myfile = ContentFile(f"{filename}.pdf")
            #     self.candidateFileNamePDF.save(f"{filename}.pdf",myfile)
                # with open(f"{filename}.pdf","rb") as f:
                #     self.candidateFileNamePDF.save(f"{filename}.pdf",ContentFile(f.file.read()) )
           
           
        #     content_file = ContentFile(self.candidateFileNameOriginal.file.read())
        #     # file = ContentFile(content_file.readlines().encode(), name="my_file.txt")
        #     # file.save()
        #     # print("content_file",dir(content_file))
        #     print("content_file",bytes(content_file.readlines()[0]).decode('utf-8'))
            # convert(r'https://recruiterstorageacc.blob.core.windows.net/demo/files/HelloWorld.docx')
            # convert('HelloWorld.docx')
            # print("candidateFileNameOriginal",self.candidateFileNameOriginal.file.read())
            # content_file = ContentFile(self.candidateFileNameOriginal.file.read())
            # loc = f"{self.candidateFileNameOriginal}"
            # with open("requirements.txt", "wb") as f:
            #     data = blob.download_blob().readall()
            #     # data.readinto(f)
          
            #     print("ankit",data)
            #     # print("kalal",data.read())
            #     # print(f.read())
            #     print("kalal")

            # convert(loc)
            # contented_file = convert(self.candidateFileNameOriginal)
            # file_client = ShareFileClient.from_connection_string(
            #     conn_str=os.getenv('connection_string'), 
            #     share_name=os.getenv('share_name'),
            #     file_path=f"demo1.pdf")
            
            # file_client.upload_file(contented_file)
        # print("first_name",self.first_name)
        # print("args",args)
        # print("kwargs",kwargs)
        # if self.candidateFileNameOriginal:
        #     print("candidateFileNameOriginal",self.candidateFileNameOriginal)
        #     # print("candidateFileNameOriginal",self.candidateFileNameOriginal.file.read())
        #     content_file = ContentFile(self.candidateFileNameOriginal.file.read())
        #     contented_file = convert(content_file)
        #     file_client = ShareFileClient.from_connection_string(
        #         conn_str=os.getenv('connection_string'), 
        #         share_name=os.getenv('share_name'),
        #         file_path=f"demo1.pdf")
            
        #     file_client.upload_file(contented_file)
        # super().save(*args, **kwargs)







# class HelpText(models.Model):
#     Help_Text = models.TextField(max_length=255, blank=True, null=True)
#     Help_Text_ID = models.AutoField(primary_key=True)
#     Help_ID_Name = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         return self.Help_ID_Name

#     class Meta:
#         #managed = False
#         db_table = 'help_text'





# class Repository(models.Model):
#     key = models.AutoField(primary_key=True)
#     objectType = models.CharField(max_length=40, blank=True, null=True)
#     dateStamp = models.DateTimeField()
#     componentGUID = models.CharField(max_length=40, blank=True, null=True)
#     userId = models.CharField(max_length=40, blank=True, null=True)
#     data = models.TextField()
#     securityGroups = models.TextField()

#     def __str__(self):
#         return self.objectType

#     class Meta:
#         #managed = False
#         db_table = 'repository'


# class Status(models.Model):
#     status_name = models.CharField(max_length=50, blank=True, null=True)
#     status_description = models.CharField(
#         max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.status_name

#     class Meta:
#         #managed = False
#         db_table = 'status'


# class Synonym(models.Model):
#     synonym = models.CharField(max_length=128, blank=True, null=True)
#     keywordid = models.IntegerField()

#     def __str__(self):
#         return self.synonym

#     class Meta:
#         #managed = False
#         db_table = 'synonym'


