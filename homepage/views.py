import json
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


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

            if not name or not email or not message:
                return JsonResponse({'status': 'error', 'message': 'Missing required fields.'}, status=400)

            email_body = f"名前: {name}\nメールアドレス: {email}\n\n件名: {subject}\n\n【本文】: {message}"
            
            send_mail(
                subject=f"[お問い合わせ] {subject}",
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECIPIENT_EMAIL],
                fail_silently=False,
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Contact form error: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message':'Invalid method'}, status=405)
    
logger = logging.getLogger(__name__)

@csrf_exempt
def ses_bounce_webhook(request):
    if request.method == 'POST':
        try:
            notification = json.loads(request.body)
            
            # 1. AWS SNS の購読確認（初回設定時に必要）
            if notification.get('Type') == 'SubscriptionConfirmation':
                subscribe_url = notification.get('SubscribeURL')
                # 購読確認のURLにリクエストを投げて認証を完了させる
                requests.get(subscribe_url)
                logger.info("SNS Subscription Confirmed")
                return HttpResponse('OK')

            # 2. 実際の通知処理（Notification）
            if notification.get('Type') == 'Notification':
                message = json.loads(notification.get('Message'))
                
                # SESの通知タイプが Bounce かチェック
                if message.get('notificationType') == 'Bounce':
                    bounce = message.get('bounce')
                    bounce_recipients = bounce.get('bouncedRecipients', [])
                    
                    for recipient in bounce_recipients:
                        bounced_email = recipient.get('emailAddress')
                        logger.error(f"【警告】メールがバウンスしました。宛先不明: {bounced_email}")
                        # ここでDBのフラグを更新したり、システム管理者に通知を飛ばす処理を記述
                        #先頭に　import requests
                return HttpResponse('OK')
                
        except Exception as e:
            logger.error(f"SNS Webhook Error: {str(e)}")
            return HttpResponse('Internal Error', status=500)

    return HttpResponse('Method Not Allowed', status=405)
