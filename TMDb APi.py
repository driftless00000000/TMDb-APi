#!/usr/bin/env python
# coding: utf-8

# TMDb 1.1
# Send Feedback
# Find the 'id' of the movie "Andhadhun" using TMDb API.
# Output Format:
# Print the id of the movie.

# In[8]:


import requests

apiKey = 'ffafe1f2b141d9a9fcae15771fe46db1'
header = {}
params={'api_key':apiKey,'page':i,'region':'IN','year':2018}
for i in range(1,10):
    res = requests.get('https://api.themoviedb.org/3/discover/movie',params=params) 
    data=res.json()
    for i in data['results']:
        if 'Andhadhun' in i['title']:
            print(i['id'])
            break

TMDb 1.2

Fetch the company id company 'Marvel Studios' using TMDb. Print the id.
# In[12]:


import requests
apiKey = 'ffafe1f2b141d9a9fcae15771fe46db1'
res = requests.get('https://api.themoviedb.org/3/search/company',params={'api_key':apiKey,'page':1,'query':'Marvel Studios'}) 
data=res.json()
print(data['results'][0]['id'])

TMDb 1.3

Find the vote count and vote average of the movie "3 Idiots" using the TMDb API
Output format: Vote Count , Vote Average
# In[ ]:


import requests
apiKey = 'ffafe1f2b141d9a9fcae15771fe46db1'
for i in range(1,10):
    res = requests.get('https://api.themoviedb.org/3/discover/movie',params={'api_key':apiKey,'page':i,'region':'IN','year':2009}) 
    data=res.json()
    for i in data['results']:
        if '3 Idiots' in i['title']:
            print(i['vote_count'],i['vote_average'])
            break

TMDb 1.4

Fetch the names of top 5 similar movies to 'Inception' from the TMDb API.
Note
While fetching the movie id, use the "original_title" field not the "title". Because the "title" field may contain duplicate values.

Output Format:
Print the name of the movies in a new line.
movie_name_1
movie_name_2
and so on
# In[ ]:


import requests
apiKey = 'ffafe1f2b141d9a9fcae15771fe46db1'
for i in range(1,10):
    res = requests.get('https://api.themoviedb.org/3/discover/movie',params={'api_key':apiKey,'page':i,'region':'IN','year':2009}) 
    data=res.json()
    for i in data['results']:
        if '3 Idiots' in i['title']:
            print(i['vote_count'],i['vote_average'])
            break

TMDb 1.5

Fetch the top rated english movies in the US region using the TMDb API. From the result, print the first 10 movies which have original language as english. Also print their genres.
Note: Do not use the search/movies API for finding genres.

Output Format:
movie_name_1 - genre_1, genre_2 ....
and so on..
# In[ ]:


import requests
apiKey = 'ffafe1f2b141d9a9fcae15771fe46db1'
for i in range(1,10):
    res = requests.get('https://api.themoviedb.org/3/discover/movie',params={'api_key':apiKey,'page':i,'region':'IN','year':2009}) 
    data=res.json()
    for i in data['results']:
        if '3 Idiots' in i['title']:
            print(i['vote_count'],i['vote_average'])
            break

TMDb 2.1

Find the name and birthplace of the present most popular person according to TMDb API.

Output Format:
id
name - birthplace
# In[ ]:


import requests
api_key = "e226f4a5f5bace766952aa0d17182959" 
api_link = "https://api.themoviedb.org/3" 
params = {'api_key':api_key}
header = {'Accept': 'application/json'} 
response = requests.get(api_link + "/person/popular", headers = header, params=params)
data = response.json()
id_of_most_popular = data.get('results')[0].get('id') 
print(id_of_most_popular)
name_of_most_popular = data.get('results')[0].get('name') 
response2 = requests.get(api_link + "/person/" + str(id_of_most_popular), headers = header, params=params)
data2 = response2.json() 
print(name_of_most_popular,"-", data2.get("place_of_birth"))

TMDb 2.2

Fetch the Instagram and Twitter handle of Indian Actress "Alia Bhatt" from the TMDb API.

Output Format
Print the Instagram and Twitter IDs space separated.
instagram_id twitter_id
# In[ ]:


import requests
api_key = "e226f4a5f5bace766952aa0d17182959" 
api_link = "https://api.themoviedb.org/3"
params = {'query':"Alia Bhatt" , 'api_key':api_key}
header = {'Accept': 'application/json'} 
response = requests.get(api_link + '/search/person', headers = header, params = params) 
data = response.json()
id = data.get('results')[0].get('id')
params2 = {'api_key':api_key}
response2 = requests.get(api_link + "/person/"+ str(id) +"/external_ids" , headers = header, params = params2) 
data2 = response2.json()
print(data2.get("instagram_id"), data2.get("twitter_id"))

TMDb 2.3

Fetch the names of the character played by Tom Cruise in the movies:
Top Gun
Mission: Impossible - Fallout
Minority Report
Edge of Tomorrow

Output Format:
Print the names of the characters played by Tom Cruise line separated, in the respective order given in question.
# In[ ]:


import requests
api_key = "b0a53d521764ab3bc5732e74a5cc06c9"
api_link = "https://api.themoviedb.org/3"
params = {'api_key':api_key,'query':'Tom Cruise'}
header = {'Accept': 'application/json'}
response2 = requests.get(api_link + "/person/"+str(500)+"/movie_credits", headers = header, params=params)
data=response2.json()
for result in data['cast']:
    if result['title']=='Top Gun':
        print(result['character'],)
for result in data['cast']:
    if result['title']=='Mission: Impossible - Fallout':
        print(result['character'])
for result in data['cast']:
    if result['title']=='Minority Report':
        print(result['character'])
for result in data['cast']:
    if result['title']=='Edge of Tomorrow':
        print(result['character'])

TMDb 3.1

Fetch the overview of the TV Show "FRIENDS" using TMDb API.

Output Format:
Print the Overview.
# In[ ]:


import requests
api_key = "e226f4a5f5bace766952aa0d17182959" 
api_link = "https://api.themoviedb.org/3"
params = {'query':"Friends" , 'api_key':api_key}
header = {'Accept': 'application/json'} 
response = requests.get(api_link + "/search/tv/", headers = header, params = params)
data = response.json()
results = data.get('results')
for result in results:
    if result.get('name') == 'Friends':
        print(result.get('overview'))

TMDb 3.2

Fetch the name and air date of S06E05 of the TV Show 'The Big Bang Theory' from TMDb API.

Output Format:
episode_name - air_date
# In[ ]:


import requests as rq
api_key = 'e226f4a5f5bace766952aa0d17182959'
api_link = 'https://api.themoviedb.org/3'
header = {'Accept':'application/json'}
params = {'query':'The Big Bang Theory','api_key':api_key}
r = rq.get(api_link + '/search/tv',headers = header, params = params)
data = r.json()
res = data.get('results')
id = res[0]['id']
sn = 6
se = 5
params2 = {'api_key':api_key}
r2 = rq.get(api_link + '/tv/'+str(id)+'/season/' + str(sn) +'/episode/' + str(se),headers = header,params=params2)
data = r2.json()
print(data['name'],'-',data['air_date'])

TMDb 3.3

Fetch the trending TV Shows for the week from the TMDb API and print the taglines of the top 5 shows. If there is no tagline, print 'Empty' instead

Output Format:
Print the taglines in new line.
# In[ ]:


import requests 
api_key = "e226f4a5f5bace766952aa0d17182959" 
api_link = "https://api.themoviedb.org/3" 
params = {'api_key':api_key} 
header = {'Accept': 'application/json'} 
response = requests.get(api_link + "/trending/tv/week", headers = header, params = params) 
data = response.json() 
results = data.get("results") 
ids=[] 
for result in results[:5]: 
    ids.append(result.get("id")) 
    
for id in ids: 
    response2 = requests.get(api_link + "/tv/" + str(id) , headers = header, params = params) 
    data2 = response2.json() 
    if (data2.get("tagline")) != "": 
        print(data2.get("tagline")) 
    else: 
        print('Empty')

TMDb 3.4

Print the names of all the TV shows to be aired today whose original language is english.

Output Format:
Print the name of each TV show in a new line.
# In[ ]:


import requests as rq
page_num = 1
api_key = 'e226f4a5f5bace766952aa0d17182959'
api_link = 'https://api.themoviedb.org/3'
header = {'Accept':'application/json'}
params = {'language':'en','api_key':api_key}
r = rq.get(api_link+'/tv/airing_today/',headers = header,params = params)
data = r.json()
# print(data)
res = data['results']
page_num = data.get('total_pages')
# print(page_num)
for i in range(1,page_num + 1):
    params = {'language':"en",'api_key':api_key,'page':i}
    r = rq.get(api_link+'/tv/airing_today/',headers = header,params = params)
    data = r.json()
    results = data.get('results')
    for r in results:
        if r['original_language'] == 'en':
            print(r['name'])

TMDb 3.5

Count the number of males and females in the cast of "Money Heist" using the TMDb API.

Output Format:
Print the count of male and female space separated.
male_count female_count
# In[ ]:


import requests
api_key = "e226f4a5f5bace766952aa0d17182959" 
api_link = "https://api.themoviedb.org/3" 
params = {'query':'Money Heist','api_key':api_key} 
header = {'Accept': 'application/json'} 
response = requests.get(api_link + '/search/tv/', headers = header, params = params) 
data = response.json() 
result=data.get('results')
for i in result:
    if i.get('name')=='Money Heist':
        id=i.get('id')    
params1={'id':id,'api_key':api_key}
response1 = requests.get(api_link + '/tv/' + str(id) + '/credits', headers = header, params = params1) 
data1 = response1.json() 
cast=data1.get('cast')
count_male=0
count_female=0
for c in cast:
    if c.get('gender')==1:
        count_female+=1
    if c.get('gender')==2:
        count_male+=1
print(count_male,count_female)

