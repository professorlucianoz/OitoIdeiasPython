from imdb import IMDb

ia = IMDb()

search = ia.get_top250_movies()

# print(search)

for i in range(10):
    print(search[i])