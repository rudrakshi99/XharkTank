# XharkTank

SharkTank is a panel of potential investors, termed as "Sharks", who listen to entrepreneurs pitch ideas for a business or product they wish to develop. These self-made multi-millionaires judge the business concepts and products pitched and then decide whether to invest their own money to help market and mentor each contestant.

## Product Flows

These are the mandatory product flows that are expected while building the backend for the XharkTank application

1. Entrepreneurs will post Pitch by providing these inputs

- Name of the entrepreneur posting the pitch
- Title of the pitch
- Business Idea for the Product they wish to develop
- Ask Expected Amount for investment
- Percentage of Equity to be diluted

2. Investors will view all the latest pitches posted to date

- If the entrepreneurs post a new pitch, that would also get listed. 

3. Investors will make a counteroffer to the pitch by providing these inputs

- Unique Id of the Pitch made by the entrepreneur
- Name of the investor making a counteroffer
- Amount ready to invest in the idea
- Ask Percentage of Equity for a company

# Demo Video

<a href="https://www.youtube.com/watch?v=q8gE4icwmsw"> <img src="https://user-images.githubusercontent.com/55245862/205116045-5d1ae28d-c885-4216-8660-83998cbc9dc1.png" alt="Demo Video" height='250' width='430'/> </a>


## Technology Stack to be used:

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/> <img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/> <img src="https://img.shields.io/badge/sqlite-0B96B2?style=for-the-badge&logo=sqlite&logoColor=white"/>

[![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/14143990/2s8Yt1rUoy)

- **Backend**: Django Rest Framework
- **IDE**: VS Code
- **API Testing & Documentation:** Postman
- **Version Control**: Git and GitHub
- **Database**: SQLite

## Important Links :

### Frontend
* [Entrepreneurs Link](http://xharktank.crio.do/pitches/?author=sonirudrakshi99&url=http%3A%2F%2Frudrakshijss.pythonanywhere.com)
* [Investor Link](http://xharktank.crio.do/invest/?author=sonirudrakshi99&url=http%3A%2F%2Frudrakshijss.pythonanywhere.com)

### Backend
* [Link](http://rudrakshijss.pythonanywhere.com/)

### Backend Setup Instructions

- Fork and Clone the repo using

```
$ git clone https://github.com/rudrakshi99/XharkTank.git
```

- Setup Virtual environment

```
$ python3 -m venv env
```

- Activate the virtual environment

```
$ source env/bin/activate
```

- Install dependencies using

```
$ pip3 install -r requirements.txt
```

- Make migrations using

```
$ python3 manage.py makemigrations
```

- Migrate Database

```
$ python3 manage.py migrate
```

- Create a superuser

```
$ python3 manage.py createsuperuser
```

- Run server using

```
$ python3 manage.py runserver
```
# License :memo:

This project follows the [MIT License](https://choosealicense.com/licenses/mit/).

## If you liked the project don't forget to star 🌟 and fork 🍽 the project.

<h2 align="center">Made with ❤ by Rudrakshi</h2>

[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
