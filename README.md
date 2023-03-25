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

