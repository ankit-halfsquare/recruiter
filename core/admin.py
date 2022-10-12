from django.contrib import admin
from .models import *
# Register your models here.


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('project_division', 'positionname', 'desired_keywords','target_start_date','est_completion_date','assigneeid','actual_start_date','active','actual_completion_date','assigner','date_added','comments','statusid')

class CandidateTableAdmin(admin.ModelAdmin):
    readonly_fields=('fileUploadUser','candidateFileName','candidateFileNamePDF','skill_keywords_full','candidateFileContents','date_added','fileUploadDate')
    list_display = ('candidate_id','first_name','last_name','city','state','country','phone','email','active_assignment','candidateFileNameOriginal','fileUploadDate','date_added','skill_keywords_full',)

class HelpTextAdmin(admin.ModelAdmin):
    list_display = ('Help_Text_ID','Help_ID_Name','Help_Text')


class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword_id','text')


class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('key','objectType','dateStamp','componentGUID','userId','data','securityGroups')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name','status_description')


class SynonymAdmin(admin.ModelAdmin):
    list_display = ('synonym','keywordid')


admin.site.register(Assignment,AssignmentAdmin)
admin.site.register(CandidateTable,CandidateTableAdmin)
admin.site.register(Keyword,KeywordAdmin)

admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Position)

# admin.site.register(HelpText,HelpTextAdmin)

# admin.site.register(Repository,RepositoryAdmin)
# admin.site.register(Status,StatusAdmin)
# admin.site.register(Synonym,SynonymAdmin)
