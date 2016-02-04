# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from users.models import CustomUser
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django import forms
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
@login_required
def article(request):
	
	args = {}
	args.update(csrf(request))
	args['form'] = ArticleForm()
	args['profile'] = CustomUser.objects.get(pk = request.user.pk)
	args['author'] = Article()
	args['article'] = Article.objects.all()

	if request.POST :
		args['form'] = ArticleForm(request.POST or None)
		if args['form'].is_valid():
			obj = args['form'].save(commit=False)
			obj.author = args['profile']
			obj.save()
		return redirect(reverse(all_articles))

	return render(request, 'article.html', args)

#Лист всех вопросов с пагинацией
def all_articles(request):
	
	articles_list = Article.objects.all().order_by('date').reverse()
	paginator = Paginator(articles_list, 10)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	
	return render(request, 'all_articles.html', {
				'articles':articles})


def get_article(request, article_pk):

	args = {}
	args.update(csrf(request))
	args['article'] = Article.objects.get(pk=article_pk)
	
	return render(request, 'get_article.html', args)


class ContactForm(forms.Form):	
	subject = forms.CharField(max_length = 100, min_length = 5)
	sender = forms.EmailField()
	message = forms.CharField(widget = forms.Textarea)
	copy = forms.BooleanField(required = False)

def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']

			recipients = ['raul1798@rambler.ru']
			#Если пользователь захотел получить копию себе, добавляем его в список получателей
			if copy:
				recipients.append(sender)
			try:
				send_mail(subject, message, '123@gmail.com', recipients, fail_silently=False)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'contactView.html', {'form' : form})
