# yummy-recipes
[![Build Status](https://travis-ci.org/dennisja/yummy-recipes.svg?branch=create_user)](https://travis-ci.org/dennisja/yummy-recipes)

Meet yummy recipes, my challenge during the Andela Bootcamp. Its inspired by the fact that keeping track of awesome food recipes is a need for many individuals who love to cook and eat good food. With it you will be able to create, save, share and keep track of those recipes, the one that matter. I'm shy to say that it might not be able to read your minds, or your social networks to see the recipes you cherish. But it will get you covered without worrying about moving with a big notebook to remember those recipes if you have your smart device.

## Features Currently Implementated
- `Registration` A user can create an account
- `Login` A user can login to maage his/her recipes
- `Manage a reciepe` A user can view, edit, delete, and create a recipe

## Requirements
The applicaton was tested on python 3.6

## Installation
### First clone this repository
```
$ git clone https://github.com/dennisja/yummy-recipes.git
$ cd yummy-recipes
```
### Create virtual environment and install it
```
$ virtualenv venv
$ source venv/bin/activate
If you are a windows user.The **source venv/bin/activate** maynot work so
- if you are using the command prompt  use ** cd venv/scripts and then run activate**
- if you are using a cygwin or git bash terinal then run ** source venv/scripts/activate **
```
### Install all the necessary dependencies
```
pip install -r requirements.txt
```
## Running the application.
Browse to the application root folder (yummy) and run the command below.

python run.py

## Appearance of some pages
### Home page when a user is not logged in
![Home Page when logged out](https://github.com/dennisja/yummy-recipes/blob/master/Designs/finished_pages/yummy_home.PNG "Home Page")

### Home page when user logs in
![Home Page when logged in](https://github.com/dennisja/yummy-recipes/blob/master/Designs/finished_pages/yummy_home_on_login.PNG "Home Page when user logs in")

### Add recipe page view
![Home Page when logged in](https://github.com/dennisja/yummy-recipes/blob/master/Designs/finished_pages/add_a_recipe.PNG "Home Page when user logs in")
