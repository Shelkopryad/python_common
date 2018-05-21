import dota2api

api = dota2api.Initialise('TOKEN')
match = api.get_match_details(match_id=1000193456)
# print(match)

hist = api.get_heroes()
list_of_maps = hist['heroes']
maps = list_of_maps[23]
print(maps)