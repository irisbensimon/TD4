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


9. Create a .gitignore file to tell Git which files should be untracked.
