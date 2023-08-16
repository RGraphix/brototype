from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def print_hello(request):


   movie_data={
    'movies':[
        {'title':'godfather','year':1990,
        'summary':'tretipojtierjgjkljtierjterjktlkerj',
        'success':True
        },


    {'title':'godfather','year':1990,'summary':'tretipojtierjgjkljtierjterjktlkerj','success':True},
    {'title':'car','year':2000,'summary':'tretipojtierjgjkljtierjterjktlkerj','success':True},
    {'title':'kuthara','year':2015,'summary':'tretipojtierjgjkljtierjterjktlkerj','success':False},
    {'title':'premam','year':2021,'summary':'tretipojtierjgjkljtierjterjktlkerj','success':True},
    
   ]}
   return render(request,'index.html',movie_data)
