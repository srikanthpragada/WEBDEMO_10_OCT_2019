import requests

resp = requests.get("http://localhost:8000/hr/rest/authors/")
if resp.status_code == 200:
    authors = resp.json()
    for author in authors:
         print(author['id'], author['name'])
else:
    print("Sorry! Could not get details of Authors!")
