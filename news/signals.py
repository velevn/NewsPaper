from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

from .models import PostCategory

@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, sender, **kwargs):
    if kwargs['action'] == 'post_add':
        subscriber_email=[]

        for category in instance.postCategory.all():
            subscriber_email += User.objects.filter(subscription__category= category).values_list('email', flat=True)

        subject = f'Новый пост {instance.postCategory}'

        text_content = (
            f'Товар: {instance.titlePost}\n'
            f'Ссылка : http://127.0.0.1:8000{instance.get_absolute_url()}'
        )
        
        html_content = (
            f'Товар: {instance.titlePost}<br>'
            f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
            f'Ссылка </a>'
        )
        
        for email in subscriber_email:
            msg = EmailMultiAlternatives(subject, text_content, None, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()