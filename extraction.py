import bson
from bson.objectid import ObjectId
from bson.raw_bson import RawBSONDocument
from listformation import extract as ext
import itertools as it
import json

from pymongo import MongoClient
client=MongoClient("mongodb+srv://IMDBUser:IMDBUser@cluster0-gzof1.azure.mongodb.net/test?retryWrites=true&w=majority")
db=client.get_database('IMDBDatabase')
movies=db.IMDBMovies
movies.count_documents({})
# print(movies.count_documents({}))
final_list=[]
movie_info={}
to_json={}  
for(a,b,c,d,e) in it.zip_longest(ext.m,ext.y,ext.r,ext.sp,ext.s):
    movie_info['movie']=a
    movie_info['Year']=b
    movie_info['Runtime']=c
    movie_info['Genre']=d
    movie_info['Rating']=e
    final_list.append(movie_info.copy())
with open('uploadable.json', 'w') as json_file:
    json.dump(final_list, json_file)
    
with open('uploadable.json','r+') as up:
    data_read=json.load(up)

movies.delete_many({})
movies.insert_many(data_read)
# print(final_list)