from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import ProcessFormView
from django.views.generic.base import ContextMixin
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
from django import forms
from .models import * 
from django.core.exceptions import ValidationError

from django import forms


class Count(forms.ModelForm):
	class Meta:
		model = Goods
		fields = ['order_count']
