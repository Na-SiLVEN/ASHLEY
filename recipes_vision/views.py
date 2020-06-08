from django.shortcuts import render
from django.template import RequestContext
# from models import Post
import pymongo
from pymongo import MongoClient
from pymongo.read_preferences import ReadPreference

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient["WebCrawler"]
mycol = mydb["Recipes"]

# Create your views here.
def v_vision(request): 
	return render(request,'vision.html',{'data':'vision.html'})

# def v_database(request):
#     return render(request,'database.html',{'data':'database.html'})

def v_database(request):
    recipes_list = []
    for x in mycol.find():
        recipes_list.append(x)
    return render(request,'table.html',{'data':recipes_list})

def v_DBquery(request):
    query_list = []
    query = { "material": { "$regex":""} }
    for x in mycol.find(query):
        query_list.append(x)
    print (query_list)
    return render(request,'table.html',{'data':query_list})
    
    
   
    
