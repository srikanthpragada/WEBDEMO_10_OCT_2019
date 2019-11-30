import requests

name = input("Enter name :")
email = input("Enter email : ")
mobile = input("Enter mobile : ")
profile = input("Enter profile : ")
data = {'name': name, 'email': email, 'mobile': mobile, 'profile': profile}

resp = requests.post("http://localhost:8000/hr/rest/authors/", data)
if resp.status_code == 200:
    print("Author added successfully!")
else:
    print("Sorry! Could not add Author!")
