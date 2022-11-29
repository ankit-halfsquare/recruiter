import imp
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.core.files.storage import default_storage

from django.db.models import Q
from functools import reduce
from operator import or_,and_



from core.models import CandidateTable,Assignment,Company,Project,Position,Keyword,PowerSearch,CandidateResumeTemplates
from core.api.v093.serializers import CandidateTableSerializer

from .forms import CandidateTableForm,TemplateForm

# from core.filters import CandidateFilter

from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import Http404, HttpResponseRedirect


class LogoutRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().dispatch(request, *args, **kwargs)


class CustomeLoginView(LogoutRequiredMixin,LoginView):
    pass

# Create your views here.

def addCandidate(request):
    if request.method == "POST":
        # print("post",request.POST)
        # print("FILES",request.FILES)
        candidateForm = CandidateTableForm(request.POST, request.FILES)
        if candidateForm.is_valid(): 
            candidate = candidateForm.save()
            return HttpResponseRedirect(reverse('v-0.9.3/edit-candidate',args=(candidate.candidate_id,)))

    return render(request,"v-0.9.3/frontend/add-candidate.html")

@login_required(login_url='/accounts/login/')
def candidates(request):
    return render(request,"v-0.9.3/frontend/candidates.html")



@login_required(login_url='/accounts/login/')
def searchCandidate(request):
    # f = CandidateFilter(request.GET, queryset=CandidateFilter.objects.all())
    return render(request,"v-0.9.3/frontend/search-form.html")



@login_required(login_url='/accounts/login/')
def candidate(request,pk=None):
    return render(request,"v-0.9.3/frontend/candidates.html")

    # if pk:
    #     pass

    # def strtolst(obj):
    #     if obj and "," in obj:
    #         return obj.split(",")
    #     return [obj] if obj else []

    # queryprms = request.GET

    # skills = queryprms.get('skills',"")
    # city = queryprms.get('city',"")
    # exclude = queryprms.get('exclude',"")

    # if queryprms.get('search'):
    #     searchname = queryprms.get('search')
       
    #     query = f"?skills={skills}&city={city}&exclude={exclude}"
    #     PowerSearch.objects.create(name=searchname,query=query)
     
    # if skills or city or exclude:
    #     skills = strtolst(skills) 
    #     city = strtolst(city) 
    #     exclude = strtolst(exclude) 
        
    #     q_object1 = reduce(or_, (Q(skill_keywords_full__icontains=key) for key in skills)) if skills else Q(skill_keywords_full__icontains = "")
    #     q_object2 = reduce(or_, (Q(city__icontains=key) for key in city)) if city else Q(city__icontains = "")
    #     q_object3 = reduce(or_, (~Q(skill_keywords_full__icontains=key) for key in exclude)) if exclude else ~Q(skill_keywords_full__icontains = "dummyValue")
        
    #     q = (Q(q_object1) &Q(q_object2) & Q(q_object3))
    #     Candidates = CandidateTable.objects.filter(q)
    # else:
    #     Candidates = CandidateTable.objects.all()


    # powerSearch = PowerSearch.objects.all()
    # context = {
    #     "candidates": Candidates,
    #     "powerSearch":powerSearch,
    #     "dummy":"summy"
    # }
    return render(request,"v-0.9.3/frontend/candidates.html",context)


@login_required(login_url='/accounts/login/')
def viewCandidate(request,pk):
    print("viewCandidate")
    candidate = CandidateTable.objects.get(pk=pk)
    print("candidate",candidate)
    form = CandidateTableForm(instance=candidate)
    context = {
        "candidate":candidate,
        "form":form
    }
    print("return")
    return render(request,"v-0.9.3/frontend/view-candidate.html",context)


@login_required(login_url='/accounts/login/')
def addUpdateCandidate(request,pk=None):
    if request.method == "POST":
        if pk:
            obj = CandidateTable.objects.get(pk=pk)
            candidateForm = CandidateTableForm(obj,data=request.POST)
            if candidateForm.is_valid():
                candidateForm.save()   
        else:
            candidateForm = CandidateTableForm(request.POST, request.FILES)
            if candidateForm.is_valid():  
                candidateForm.save() 
        
        return redirect('home')

    if pk:
        candidate = CandidateTable.objects.get(pk=pk)
        form = CandidateTableForm(instance=candidate)
    else:
        form = CandidateTableForm()
    context = {"form":form}
    return render(request,"v-0.9.3/frontend/candidate.html",context)

    # file = request.FILES['candidateFileNameOriginal']
    # default_storage.save(file.name, file)




def test(request):
    form = CandidateTableForm()
    context = {"form":form}
    return render(request,"v-0.9.3/frontend/test.html",context)


@login_required(login_url='/accounts/login/')
def project(request):
    return render(request,"v-0.9.3/frontend/project.html")


##v-0.9.3 views

@login_required(login_url='/accounts/login/')
def status(request):
    return render(request,"v-0.9.3/frontend/status.html")


@login_required(login_url='/accounts/login/')
def skillLevel(request):
    return render(request,"v-0.9.3/frontend/skill-level.html")

@login_required(login_url='/accounts/login/')
def priority(request):
    return render(request,"v-0.9.3/frontend/priority.html")


@login_required(login_url='/accounts/login/')
def platformOrReferral(request):
    return render(request,"v-0.9.3/frontend/platform-referral.html")



@login_required(login_url='/accounts/login/')
def template(request): 
    pk = request.GET['id']
    candidateObj = CandidateTable.objects.get(pk=pk)
    
    if candidateObj.template:
        form = CandidateTableForm(instance=candidateObj)
    else:
        template = CandidateResumeTemplates.objects.get(pk=1)
        form = TemplateForm(instance=template)
    context = {
        "form":form,
        "id":pk, 
        "resume":request.GET['resume']
    } 
    return render(request,"v-0.9.3/frontend/template.html",context)





