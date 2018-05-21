import dota2api
import requests

api = dota2api.Initialise('TOKEN')
match = api.get_match_details(match_id=1000193456)
# print(match)

hist = api.get_heroes()
list_of_maps = hist['heroes']
heroes_info = list_of_maps[23]
for x in list_of_maps:
    name = x['localized_name']
    url = x['url_large_portrait']
    resp = requests.get(url)
    b = resp.content

    file_name = 'portraits/portrait_' + name + '.png'
    fobj = open(file_name, "wb") 
    fobj.write(b) 
    fobj.close() 

