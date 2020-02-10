from django.contrib import admin
from .models import NewsLetterUserList, SendEmailToNewsLetterUser


# Register your models here.
admin.site.register(NewsLetterUserList)
admin.site.register(SendEmailToNewsLetterUser)



