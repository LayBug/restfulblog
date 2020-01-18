from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    list_display = [
            'username',
            'first_name',
            'email',
            'password',
            ]


admin.site.register(get_user_model(), CustomUserAdmin)

