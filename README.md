# TD4

## Exercise 1: Working Directory

1. Create an empty working directory called “td4”
```
mkdir td4
```
```
cd td4
```
2. Initialize a Git repository in it.
```
git init
```
3. Install the Linux python3-pip package using your Linux package manager.
```
sudo yum install python3-pip
```
4. Install the VirtualEnv Python package using pip3.
```
pip3 install VirtualEnv
```
5. Create a Python virtual environment called “.env”. Do you see the change in your working directory ?
```
virtualenv -p python3 .env
ls -a
```
A New folder (hidden) .env has been created.

6. Activate your virtual environment. Do you see the change in your prompt ?
```
source .env/bin/activate
```
We can see a (.env) in the prompt

7. List the Python packages installed in your virtual environment.
```
pip freeze
```
8. Does Git want you to commit something ? Do you think it is a good thing ?

No. It is not a good idea because evry packages installes will be saved.

9. Create a .gitignore file to tell Git which files should be untracked.
```
vim .gitignore
```
10. Does Git want you to commit something ? Do you think it is a good thing this time ?

Git want me to commit the .gitignore now. It is a goode thing .

11. Do your first commit and check that Git is happy now
```
git add .
git commit -m ".gitignore added"
```

## Exercice 2: Python script

1. Install the Python package Requests using pip.
```
pip3 install Requests
```
2. Create a Python script that returns the list of all place ids in Derbyshire.
```
vim python.py
```
```
import requests

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Derbyshire,GB",
    "appid": "77726e0a958212777b35fb68222b834b"
}

response = requests.get(url, params=params)

place_ids = [place["id"] for place in response.json()["sys"]["country"]]

print(place_ids)
```
3. Commit your changes in Git
```
git add .
git commit -m "python script""
```

## Exercice 3: Python Module

1. Create a Python module with a get_manor_ids function that takes a place id as parameter and returns the list of manors.
```
nano getmanor.py
```
```
import requests

def get_manor_ids(placeId):
        res = requests.get('https://opendomesday.org/api/1.0/place'+str(placeId))
        data = res.json()
        if 'manors' in data.keys():
                return data['manors']
        else:
                return []
 ```
 
 2. Check that calling your module does not produce any output
 ```
 python getmanor.py
 ```
 Any output.
 
 3. To test your module, open a python interpreter and call your function with the first place id from Derbyshire.
```
python
import getmanor
getmanor.get_manor_ids(2651555)
exit()
```
4. Add a if __name__ == ’__main__’ : block with your previous test, at the end of your module, to make it usable as a script.
```
nano getmanor.py
```
```
if __name__ == '__main__':
    place_id = 2653753 # Derby, UK
    manors = get_manor_ids(place_id)
    print(f"Manor IDs in Derby: {manors}")
```
5. Check that calling your module now does produce an output.
```
python getmanor.py
```
6. Commit your changes in Git
```
git add .
git commit -m "module get manor added"
```

