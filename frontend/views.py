from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.files.storage import default_storage

from django.db.models import Q
from functools import reduce
from operator import or_,and_



from core.models import CandidateTable,Assignment,Company,Project,Position,Keyword,PowerSearch
from .forms import CandidateTableForm

# from core.filters import CandidateFilter

from django.contrib.auth.decorators import login_required


# Create your views here.




@login_required(login_url='/accounts/login/')
def searchCandidate(request):
    # f = CandidateFilter(request.GET, queryset=CandidateFilter.objects.all())
    return render(request,"frontend/search-form.html")



@login_required(login_url='/accounts/login/')
def home(request):

    def strtolst(obj):
        if obj and "," in obj:
            return obj.split(",")
        return [obj] if obj else []

    queryprms = request.GET

    skills = queryprms.get('skills',"")
    city = queryprms.get('city',"")
    exclude = queryprms.get('exclude',"") 

    if queryprms.get('search'):
        searchname = queryprms.get('search')
       
        query = f"?skills={skills}&city={city}&exclude={exclude}"
        PowerSearch.objects.create(name=searchname,query=query)
     
    if skills or city or exclude:
        skills = strtolst(skills) 
        city = strtolst(city) 
        exclude = strtolst(exclude) 
        
        q_object1 = reduce(or_, (Q(skill_keywords_full__icontains=key) for key in skills)) if skills else Q(skill_keywords_full__icontains = "")
        q_object2 = reduce(or_, (Q(city__icontains=key) for key in city)) if city else Q(city__icontains = "")
        q_object3 = reduce(or_, (~Q(skill_keywords_full__icontains=key) for key in exclude)) if exclude else ~Q(skill_keywords_full__icontains = "dummyValue")
        
        q = (Q(q_object1) &Q(q_object2) & Q(q_object3))
        Candidates = CandidateTable.objects.filter(q)
    else:
        Candidates = CandidateTable.objects.all()

    powerSearch = PowerSearch.objects.all()
    context = {
        "candidates":Candidates,
        "powerSearch":powerSearch
    }
    return render(request,"frontend/display-candidates.html",context)


@login_required(login_url='/accounts/login/')
def viewCandidate(request,pk):
    candidate = CandidateTable.objects.get(pk=pk)
    context = {
        "candidate":candidate
    }
    return render(request,"frontend/view-candidate.html",context)


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
    return render(request,"frontend/candidate.html",context)

    # file = request.FILES['candidateFileNameOriginal']
    # default_storage.save(file.name, file)


@login_required(login_url='/accounts/login/')
def assignment(request):
    Assignments = Assignment.objects.all()
    context = {
        "assignment":Assignments
    }
    return render(request,"frontend/display-company.html",context)



@login_required(login_url='/accounts/login/')
def company(request):
    Companies = Company.objects.all()
    context = {
        "company":Companies
    }
    return render(request,"frontend/display-company.html",context)


@login_required(login_url='/accounts/login/')
def project(request):
    Projects = Project.objects.all()
    context = {
        "project":Projects
    }
    return render(request,"frontend/display-company.html",context)



@login_required(login_url='/accounts/login/')
def position(request):
    Positions = Position.objects.all()
    context = {
        "position":Positions
    }
    return render(request,"frontend/display-company.html",context)


@login_required(login_url='/accounts/login/')
def keyword(request):
    Keywords = Keyword.objects.all()
    context = {
        "keyword":Keywords
    }
    return render(request,"frontend/display-company.html",context)


