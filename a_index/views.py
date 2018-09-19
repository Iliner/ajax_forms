from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Goods, Photo
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from .forms import Count, CountEdit
from django.core.paginator import Paginator, InvalidPage
from django.shortcuts import redirect




def index(request):
	goods = Goods.objects.all()
	if request.method == 'POST':
		form = Count(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			return render(request, 'a_index/list_goods_view.html', {'goods': goods})
	form = Count(initial={'order_count': 2}) 
	return render(request, 'a_index/list_goods_view.html', {'goods': goods, 'form': form})



def add_view(request):
	if request.method == 'POST':
		print(request.POST['count'], request.POST['code'])
		good = Goods.objects.get(code=request.POST['code'])
		good.order_count = request.POST['count']
		good.save()
	return HttpResponse('')




class JoinFormView(FormView, ListView):
	form_class = Count
	template_name  = 'a_index/list_goods.html'
	success_url = '/form-success/'
	paginate_by = 2

	def get_initial(self):
		"""
		Returns the initial data to use for forms on this view.
		"""

		initial = super(JoinFormView, self).get_initial()
		return initial

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







class GoodDetailView(DetailView, FormView):
	"""Ищет объект по pk
	если его нет то ищет по pk_url_kwargs
	"""
	template_name =  'a_index/good_page.html'
	model = Goods
	context_object_name = 'good'
	form_class = Count
	pk_url_kwargs = 'code'

	def get_initial(self):
		"""
		Returns the initial data to use for forms on this view.
		"""

		initial = super(GoodDetailView, self).get_initial()
		initial['order_count'] = Goods.objects.get(code=self.kwargs['code']).order_count

		return initial


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

	def get_object(self):
		"""Возвращает единственный объект, отображаемый этим представлением. 
		Если queryset предусмотрено, этот запрос будет использоваться как источник объектов; 
		в противном случае get_queryset(). get_object()ищет pk_url_kwargаргумент в аргументах представления; 
		если этот аргумент найден, этот метод выполняет поиск на основе первичного ключа с использованием этого значения. 
		Если этот аргумент не найден, он ищет slug_url_kwargаргумент и выполняет поиск в slug с помощью slug_field.
		"""

		return Goods.objects.get(code=self.kwargs['code'])

