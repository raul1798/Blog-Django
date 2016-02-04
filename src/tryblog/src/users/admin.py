# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser


# Register your models here.
class UserAdmin(UserAdmin):

    list_display = [
        'email',
        'firstname',
        'lastname',
        'date_of_birth',
        'username',
        'is_admin',
        'date_joined',
    ]

    list_filter = ('is_admin',)

    fieldsets = (
                (None, {'fields': ('username', 'email', 'password')}),
                ('Personal info', {
                 'fields': (
                     'avatar',
                     'date_of_birth',
                     'firstname',
                     'lastname',
                     'date_joined',
                 )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'date_of_birth',
                'email',
                'password1',
                'password2',
                'date_joined',
            )}
         ),
    )

    ordering = ('email',)
    filter_horizontal = ()

# Регистрация нашей модели
admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)