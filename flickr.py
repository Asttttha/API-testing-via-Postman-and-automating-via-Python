import requests

api_key = '#'

endpoint_url= 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=#&tags=cat&format=json&nojsoncallback=1'

response = requests.get(endpoint_url)

if response.status_code == 200:
    data=response.json()
    first_photo_title = data['photos']['photo'][0]['title']
    print("Title of first item ", first_photo_title)
else:
    print("There were some errors")

