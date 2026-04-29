from django.shortcuts import render

def index(request):
    # ms_index.html を表示
    return render(request, 'homepage/ms_spage0.html')

def spage(request, num):
    # URLの数字に基づき ms_spage1.html などを返す
    template_name = f'homepage/ms_spage{num}.html'
    return render(request, template_name)
