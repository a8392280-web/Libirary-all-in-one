from app.fetch.movies_info_fetcher import search_anime_movies,get_anime_info
from app.fetch.series_info_fetcher import search_anime_series,get_anime_info



series = search_anime_series("Naruto")
for m in series:
    print(f"{m["title"] }: {m["type"]}",m["id"])

p=get_anime_info(20)
print(p)

# import requests

# MAL_CLIENT_ID = "40a4ef5842876ffb373d1077a922d2ad"

# def get_anime_info(anime_id):
#     url = f"https://api.myanimelist.net/v2/anime/{anime_id}"
#     headers = {"X-MAL-CLIENT-ID": MAL_CLIENT_ID}
#     params = {
#         "fields": "id,title,main_picture,media_type,num_episodes,start_date,genres,studios,synopsis,alternative_titles,end_date,mean"
#     }

#     response = requests.get(url, headers=headers, params=params, timeout=10)
    
#     print("Status code:", response.status_code)
#     if response.status_code != 200:
#         print("Response:", response.text)
#         return "no"
    
#     data = response.json()
#     return data

# # Test
# anime = get_anime_info(4437)
# print(anime)
