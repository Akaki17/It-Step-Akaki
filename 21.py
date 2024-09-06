import json

with open('movies.json', 'r') as file:
    data = json.load(file)

for movie in data[0]['results']:
    release_year = int(movie['release_date'][:4])

    if release_year > 2000 and 'Crime' in movie['genres']:
        movie['genres'] = ['New_Crime' if genre == 'Crime' else genre for genre in movie['genres']]
        
    elif release_year < 200 and 'Drama' in movie['genres']:
        movie['genres'] = ['Old_Drama' if genre == 'Drama' else genre for genre in movie['genres']]
        
    elif release_year == 2000:
        movie['genres'].append('new_Century')
        
with open('movies.json', 'w') as file:
    json.dump(data, file, indent=4)