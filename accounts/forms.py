from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from django.contrib.auth.models import Group


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        group_users = Group.objects.get(name='general')
        user.groups.add(group_users)
        
        send_mail(
            subject='Добро пожаловать на наш новостной портал!',
            message=f'{user.username}, вы успешно зарегистрировались!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email],
        )
        return user