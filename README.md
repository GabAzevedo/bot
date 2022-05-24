# Web Scraping with Python

## Description 
The bot in question is the result of python applications aimed at acquiring data from a particular website.

The application consists of automating the acquisition of data and managing the data, thus being able to sort by values, inform evaluations and filter the data as you see fit. 

### Index
* [Description](#Description)
* [Requirements](#Requirements)
* [Apply](#Apply)
* [Deploy](#Deploy)

### Apply

* Clone repository
`git clone https://github.com/GabAzevedo/bot.git`  
* Access project folder in terminal/cmd
`cd bot`
* Create a virtual environment
`python -m venv .venv`
* Access the Virtual Environment
- Linux
`source .venv\Scripts\activate`
- Windows
`.venv/Script/activate`
* Install the dependencies
`pip install -r requirements.txt` 
* Run the server
`uvicorn main:app --reload`

### Example using heroku
* Install the [heroku cli](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli)
* Create an application on heroku
`heroku create -a example-app`
* Send your code
`git push heroku master`

> Example on heroku: https://git.heroku.com/bot-gabriel-carvalho.git




