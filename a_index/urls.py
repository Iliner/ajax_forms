"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from a_index.views import *

urlpatterns = [
	url(r'^main/$', JoinFormView.as_view(),  name='index'),
	url(r'^main_view/$', index,  name='index_view'),
	url(r'^join/', JoinFormView.as_view()),
	url(r'^main_view/count/add$', add_view, name='add_count'),
	url(r'good/(?:(?P<code>\d+)/)$', GoodDetailView.as_view(), name='good_page'),
]
