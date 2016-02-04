# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import RegexValidator
import datetime
from captcha.fields import CaptchaField

#Create your models here.
class UserManager(BaseUserManager):

	def create_user(self, username, email, password=None):
		if not email:
			raise ValueError(_('You must set email '))
		if not username:
			raise ValueError(_('User must have username'))
		
		user = self.model( username=username, 
			email=self.normalize_email(email),
			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password):
		user = self.create_user(username=username, email=email, password=password)
		user.is_admin = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')

	username = models.CharField(('Логин'), unique=True, max_length=30, validators=[alphanumeric])

	email = models.EmailField(
		('Email'),
		max_length=255,
		unique=True,
		db_index=True
		)
	avatar = models.ImageField(
		('Avatar'),
		blank=True,
		upload_to='user/avatar',
		default='user/default.jpg'
		)
	firstname = models.CharField(
		('Имя'),
		max_length=40,
		blank=True,
		)
	lastname = models.CharField(
		('Фамилия'),
		max_length=40,
		blank=True,
		)
	date_of_birth = models.DateField(
		('Дата рождения'),
		null=True,
		blank=True,
		)
	about_user = models.TextField(
		('О себе'),
		blank=True,
		)
	is_admin = models.BooleanField(
		('Superuser'),
		default=False
		)
	#phone = models.IntegerField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
	date_joined = models.DateTimeField(default=datetime.datetime.now, null=False)
	

	@property
	def is_staff(self):
	    return self.is_admin

	def get_short_name(self):
		return self.email

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = UserManager()

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'
	