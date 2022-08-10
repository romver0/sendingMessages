from django.conf import settings
from django.core.mail import send_mail, BadHeaderError, send_mass_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

# from Email.settings import DEFAULT_FROM_EMAIL,RECIPIENTS_EMAIL
from sendemail.forms import ContactFormOne, ContactFormMany


# def contact_view(request):
#     # если метод GET, вернём форму
#     if request.method == 'GET':
#         form = ContactForm()
#     # если метод POST, проверим форму и отправим письмо
#     elif request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # очещенные данные
#             subject = form.cleaned_data['subject']
#             # subject='Важно!'
#             # message='Тебе понравилось моё портфолио,можешь написать мне на эту почту и мы с тобой всё обговорим!'
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             many_email = form.cleaned_data['many_email']
#             emails = many_email.split(',')
#
#             try:
#                 subject = subject
#                 message = message
#                 host_email = settings.EMAIL_HOST_USER
#
#                 # send_mail(f'{subject}', f'{message}', settings.EMAIL_HOST_USER, [f'{from_email}'])
#                 send_mail(f'{subject}', f'----- от {from_email} -----\n\n{message}', settings.EMAIL_HOST_USER,
#                           [host_email, ])
#
#                 data = (
#                     (f'{subject}', f'{message}', 'romadjango2023@mail.ru', emails),
#                 )
#                 print('data = ', data)
#                 send_mass_mail(data)
#
#                 # Массовые  рассылки
#                 # datatuple = (
#                 #     ('Subject', 'Message.', 'romadjango2023@mail.ru', ['volkoven70@mail.ru', 'roma_zverev2002@mail.ru', 'lenazv71@mail.ru', 'ilya.cherniy13@mail.ru']),
#                 # )
#                 # send_mass_mail(datatuple)
#
#             # плохой ответ заголовка
#             except BadHeaderError:
#                 return HttpResponse('Ошибка в теме письма!Подсуетись,чтоб сделать нормально!')
#             return redirect('success')
#     else:
#         return HttpResponse('Неверный запрос.')
#     return render(request, 'email.html', {'form': form})


def sendingUserView(request):
    # если метод GET, вернём форму
    if request.method == 'GET':
        form = ContactFormOne()
    # если метод POST, проверим форму и отправим письмо
    elif request.method == 'POST':
        form = ContactFormOne(request.POST)
        if form.is_valid():
            # очещенные данные
            subject = form.cleaned_data['subject']
            # subject='Важно!'
            # message='Тебе понравилось моё портфолио,можешь написать мне на эту почту и мы с тобой всё обговорим!'
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                subject = subject
                message = message
                host_email = settings.EMAIL_HOST_USER

                # send_mail(f'{subject}', f'{message}', settings.EMAIL_HOST_USER, [f'{from_email}'])
                send_mail(f'{subject}', f'----- от {from_email} -----\n\n{message}', settings.EMAIL_HOST_USER,
                          [host_email, ])
                send_mail(f'{subject}', f'----- сообщение дошло до {host_email} -----\n\nВаше сообщение\n\n{message}', settings.EMAIL_HOST_USER,
                          [from_email, ])

            # плохой ответ заголовка
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма!Подсуетись,чтоб сделать нормально!')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'email.html', {'form': form})


def sendingUsersView(request):
    # если метод GET, вернём форму
    if request.method == 'GET':
        form = ContactFormMany()
    # если метод POST, проверим форму и отправим письмо
    elif request.method == 'POST':
        form = ContactFormMany(request.POST)
        if form.is_valid():
            # очещенные данные
            subject = form.cleaned_data['subject']
            # subject='Важно!'
            # message='Тебе понравилось моё портфолио,можешь написать мне на эту почту и мы с тобой всё обговорим!'
            message = form.cleaned_data['message']
            many_email = form.cleaned_data['many_email']
            emails = many_email.split(',')

            try:
                subject = subject
                message = message
                host_email = settings.EMAIL_HOST_USER
                data = (
                    (f'{subject}', f'{message}', 'romadjango2023@mail.ru', emails),
                )
                send_mass_mail(data)
                # Массовые  рассылки
                # datatuple = (
                #     ('Subject', 'Message.', 'romadjango2023@mail.ru', ['volkoven70@mail.ru', 'roma_zverev2002@mail.ru', 'lenazv71@mail.ru', 'ilya.cherniy13@mail.ru']),
                # )
                # send_mass_mail(datatuple)
            # плохой ответ заголовка
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма!Подсуетись,чтоб сделать нормально!')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'email.html', {'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')


def home_view(request):
    return render(request, 'home.html')
