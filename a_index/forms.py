from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import ProcessFormView
from django.views.generic.base import ContextMixin
from django.core.validators import MinValueValidator
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
from django import forms
from .models import * 
from django.core.exceptions import ValidationError

from django.forms.models import modelformset_factory
from django import forms


# class Count(forms.ModelForm):
# 	class Meta:
# 		model = Goods
# 		fields = ['order_count']
# 	order_count = forms.IntegerField(initial = 'order_count', label = False, min_value=0, max_value=100, validators=[MinValueValidator('0')], widget=forms.NumberInput(attrs={'style': 'width: 55px'}))



# GoodFormset = modelformset_factory(Goods)

class CountEdit(forms.ModelForm):
	class Meta:
		model = Goods
		fields = ['order_count']
	order_count = forms.IntegerField(label = False, min_value=0, max_value=100, validators=[MinValueValidator('0')], widget=forms.NumberInput(attrs={'style': 'width: 55px'}))



class Count(forms.Form):
	order_count = forms.IntegerField(initial = 'order_count', label = False, min_value=0, max_value=100, validators=[MinValueValidator('0')], widget=forms.NumberInput(attrs={'style': 'width: 55px'}))
	

# CountFormset = modelformset_factory(Goods, form=Count)
 