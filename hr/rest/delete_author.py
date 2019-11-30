import requests

id = input("Enter author id :")
resp = requests.delete(f"http://localhost:8000/hr/rest/authors/{id}")
if resp.status_code == 204:
    print("Author was deleted successfully!")
else:
    print("Sorry! Author not found!")
