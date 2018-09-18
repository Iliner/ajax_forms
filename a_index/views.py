from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Goods, Photo
from django.views.generic import FormView
from .forms import Count
# Create your views here.





# class GoodListView(ListView):
# 	"""
# 	Класс удобный для вывода СПИСКА чего либа 
# 	"""

# 	template_name = 'a_index/list_goods.html'
# 	paginate_by = 1


# 	def get_queryset(self): 
# 		"""
# 		Этот метод вызврощает спичсок 
# 		записей которые будут выводиться 
# 		на экран 
# 		""" 

# 		return Goods.objects.all().order_by('code')


class JoinFormView(FormView, ListView):
	form_class = Count
	template_name  = 'a_index/list_goods.html'
	success_url = '/form-success/'
	paginate_by = 1

	def form_invalid(self, form):
		response = super(JoinFormView, self).form_invalid(form)
		if self.request.is_ajax():
			return JsonResponse(form.errors, status=400)
		else:
			return response

	def form_valid(self, form):
		response = super(JoinFormView, self).form_valid(form)
		if self.request.is_ajax():
			print(form.cleaned_data)
			data = {
				'message': "Successfully submitted form data."
				}
			return JsonResponse(data)
		else:
			return response

	def get_queryset(self): 
		"""
		Этот метод вызврощает спичсок 
		записей которые будут выводиться 
		на экран 
		""" 

		return Goods.objects.all().order_by('code')