from django.contrib import admin
from django.utils.html import format_html
from .models import *
# from easy_select2 import select2_modelform
# Register your models here.



class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('project_division', 'positionname', 'desired_keywords','target_start_date','est_completion_date','assigneeid','actual_start_date','active','actual_completion_date','assigner','date_added','comments','statusid')


# CandidateTableForm = select2_modelform(CandidateTable, attrs={'width': '250px'})

class CandidateTableAdmin(admin.ModelAdmin):
    # form = CandidateTableForm
    readonly_fields=('fileUploadUser','candidateFileName','candidateFileNamePDF','date_added','fileUploadDate')
    list_display = ('skill_keywords_found','first_name','last_name','city','state','country','phone','email','active_assignment','candidateFileNameOriginal','fileUploadDate','date_added',)
    list_display_links = ('first_name','last_name','skill_keywords_found',)
    list_filter = (('skill_keywords_full',admin.EmptyFieldListFilter),'active','city','state','date_added')

    def skill_keywords_found(self,obj):
        return format_html(f'<h4 style="color:green" >{obj.skill_keywords_full}</h4>')

        
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
admin.site.register(PowerSearch)
admin.site.register(CandidateStatus)
admin.site.register(CandidatePriority)
admin.site.register(CandidateSkillLevel)
admin.site.register(PlatformOrReferral)
admin.site.register(CandidateResumeTemplates)



# admin.site.register(HelpText,HelpTextAdmin)

# admin.site.register(Repository,RepositoryAdmin)
# admin.site.register(Status,StatusAdmin)
# admin.site.register(Synonym,SynonymAdmin)
