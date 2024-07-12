# base reference
# https://www.section.io/engineering-education/spotify-python-part-1/


import spotipy
from spotipy.oauth2 import SpotifyOAuth

ID = open("./REFERENCES/client_ID.txt", "r").read()
SECRET = open("./REFERENCES/client_secret.txt", "r").read()


scope = "user-read-currently-playing"
# https://developer.spotify.com/documentation/web-api/concepts/scopes

client = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
            client_id=ID, 
            client_secret= SECRET, 
            scope=scope, 
            redirect_uri= 'http://localhost:8080'
        )
    )

print(client,"\n\n",type(client))

client_result = client.currently_playing()

print(client_result)

# results = sp.current_user_recently_played()

# sp.

# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])