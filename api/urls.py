from django.urls import path, register_converter
from . import converters, views

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.TwoDigitMonthConverter, 'mm')
register_converter(converters.TwoDigitDateConverter, 'dd')

urlpatterns = [
    path('articles/', views.articles, name='home'),
    path('articles/<yyyy:year>/', views.articles),
    path('articles/<yyyy:year>/<mm:month>/', views.articles),
    path('articles/<yyyy:year>/<mm:month>/<dd:date>/', views.articles),
    path('articles/<yyyy:year>/<mm:month>/<dd:date>/<str:aid>', views.articles),
    path('articles/by/<str:category>/', views.category_articles, name='home'),
    path('article/', views.article, name='article'),
    path('article/<str:postid>/', views.article, name='article'),
]
