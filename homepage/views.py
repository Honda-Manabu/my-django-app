from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

def ms_index(request):
    return render(request, 'homepage/ms_index.html')

def ms_cmtys(request):
    return render(request, 'homepage/ms_cmtys.html')

def ms_contact(request):
    return render(request, 'homepage/ms_contact.html')

def ms_link(request):
    return render(request, 'homepage/ms_link.html')

def ms_tastcho(request):
    return render(request, 'homepage/ms_tastcho.html')

def index(request):
    # ms_index.html を表示
    return render(request, 'homepage/ms_index.html', {
        'is_about_me_section': False  # 新メニューのみ表示
    })

def spage(request, num):
    # URLの数字に基づき ms_spage1.html などを返す
    template_name = f'homepage/ms_spage{num}.html'
    is_about_me = True if num >= 0 else False

    context = {
        'num': num,
        'is_about_me_section': is_about_me,
    }
    return render(request, template_name, context)


def contact_view(request):
    return render(request, 'homepage/ms_contact.html')

def contact_send(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject', 'No Subject')
            message = data.get('message')

            full_message = f"From: {name} <{email}>\n\n{message}"
            
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'invalid method'}, status=400)
    

