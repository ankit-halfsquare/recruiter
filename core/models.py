from django.db import models

# Create your models here.

class Company(models.Model):
    status_name = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'company'
        verbose_name_plural = "companies"


class Project(models.Model):
    status_name = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'project'


class Position(models.Model):
    status_name = models.CharField(max_length=50, blank=True, null=True)
    class Meta: 
        db_table = 'position'


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
        managed = False
        db_table = 'assignment'


class CandidateTable(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    history = models.CharField(max_length=500, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    active_assignment = models.CharField(max_length=50, blank=True, null=True)
    adder = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    fk_ra_company = models.CharField(max_length=255, blank=True, null=True)
    fk_ra_project = models.CharField(max_length=255, blank=True, null=True)
    fk_ra_position = models.CharField(max_length=255, blank=True, null=True)
    skill_keywords = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    candidateFileName = models.CharField(max_length=255, blank=True, null=True)
    candidateFileContents = models.TextField(blank=True, null=True)
    candidateFileNameOriginal = models.CharField(
        max_length=255, blank=True, null=True)
    candidateFileNamePDF = models.CharField(
        max_length=255, blank=True, null=True)
    fileUploadDate = models.DateTimeField(blank=True, null=True)
    candidateFileNameOriginalFull = models.CharField(max_length=255, null=True, blank=True)
    fileUploadUser = models.CharField(max_length=255, null=True, blank=True)
    archive = models.IntegerField(null=True, blank=True)
    skill_keywords_full = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        managed = False
        db_table = 'candidate_tbl'
        verbose_name_plural = "candidates"


class HelpText(models.Model):
    Help_Text = models.TextField(max_length=255, blank=True, null=True)
    Help_Text_ID = models.AutoField(primary_key=True)
    Help_ID_Name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.Help_ID_Name

    class Meta:
        managed = False
        db_table = 'help_text'


class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        managed = False
        db_table = 'keyword'


class Repository(models.Model):
    key = models.AutoField(primary_key=True)
    objectType = models.CharField(max_length=40, blank=True, null=True)
    dateStamp = models.DateTimeField()
    componentGUID = models.CharField(max_length=40, blank=True, null=True)
    userId = models.CharField(max_length=40, blank=True, null=True)
    data = models.TextField()
    securityGroups = models.TextField()

    def __str__(self):
        return self.objectType

    class Meta:
        managed = False
        db_table = 'repository'


class Status(models.Model):
    status_name = models.CharField(max_length=50, blank=True, null=True)
    status_description = models.CharField(
        max_length=255, blank=True, null=True)

    def __str__(self):
        return self.status_name

    class Meta:
        managed = False
        db_table = 'status'


class Synonym(models.Model):
    synonym = models.CharField(max_length=128, blank=True, null=True)
    keywordid = models.IntegerField()

    def __str__(self):
        return self.synonym

    class Meta:
        managed = False
        db_table = 'synonym'
