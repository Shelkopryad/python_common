import dota2api
import requests

api = dota2api.Initialise('TOKEN')
match = api.get_match_details(match_id=1000193456)
# print(match)

hist = api.get_heroes()
list_of_maps = hist['heroes']
hi = list_of_maps[15]
# print(hi)
for x in list_of_maps:
    name = x['localized_name']
    url = x['url_vertical_portrait']
    resp = requests.get(url)
    b = resp.content

    file_name = 'portraits/portrait_' + name + '.png'
    file_ex = open(file_name,'w+')
    file_ex.close()
    fobj = open(file_name, "wb") 
    fobj.write(b) 
    fobj.close()

