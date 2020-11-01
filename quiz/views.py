from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
from django.core.paginator import EmptyPage, InvalidPage, Paginator
lst = []
answers = Questions.objects.all()
anslist = []
for i in answers:
    anslist.append(i.answer)
def index(request):
    obj = Questions.objects.all()
    count = Questions.objects.all().count()
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page =1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):
        
        questions=paginator.page(paginator.num_pages)
            
    return render(request,'index.html',{'obj':obj,'questions':questions,'count':count})
def result(request):
    score =0
    for i in range(len(lst)):
        if lst[i]== anslist[i] :
            score +=1
        else:
            score +=0
    return render(request,'result.html',{'score':score})
       

def save_ans(request):
    ans = request.GET['ans']
    lst.append(ans)
def welcome(request):
    lst.clear()
    return render(request,'welcome.html')
