from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'А могли бы и не подписываться...',
        'SadLaboka@yandex.ru',
        [user_email],
        fail_silently=False
    )
