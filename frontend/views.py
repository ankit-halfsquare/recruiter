from django.shortcuts import render
from core.models import CandidateTable,Assignment,Company,Project,Position,Keyword
from .forms import CandidateTableForm


# Create your views here.


def home(request):
    Candidates = CandidateTable.objects.all()
    context = {
        "candidates":Candidates
    }
    return render(request,"frontend/display-candidates.html",context)



def viewCandidate(request,pk):
    candidate = CandidateTable.objects.get(pk=pk)
    context = {
        "candidate":candidate
    }
    return render(request,"frontend/view-candidate.html",context)

def addUpdateCandidate(request,pk):
    candidate = CandidateTable.objects.get(pk=pk)
    form = CandidateTableForm(instance=candidate)
    context = {"form":form}
    return render(request,"frontend/candidate.html",context)


def assignment(request):
    Assignments = Assignment.objects.all()
    context = {
        "assignment":Assignments
    }
    return render(request,"frontend/display-company.html",context)



def company(request):
    Companies = Company.objects.all()
    context = {
        "company":Companies
    }
    return render(request,"frontend/display-company.html",context)


def project(request):
    Projects = Project.objects.all()
    context = {
        "project":Projects
    }
    return render(request,"frontend/display-company.html",context)



def position(request):
    Positions = Position.objects.all()
    context = {
        "position":Positions
    }
    return render(request,"frontend/display-company.html",context)


def keyword(request):
    Keywords = Keyword.objects.all()
    context = {
        "keyword":Keywords
    }
    return render(request,"frontend/display-company.html",context)