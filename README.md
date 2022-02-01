# FlaskRestAPI

#### This is used to get the ratings of particular restaurant in any location
> This data is not fetched and self made so it has not covered many locations **for now**


> The idea behind making this API is to use it for creating an application where users can get restaurant ratings of any restaurants they want. And the data which will help for showcasing the restaurant details is this API

Building Rest API using flask which has two endpoints 
- Client - provides users id, name, city, place
- Place  - provides place id, name, rating


## Getting Started
These instructions will get you this project running on your local device.
* Python 3.9 (tested on)
* Flask 2.0.2 (tested on)
You can check your flask version using ```flask --version```

***

## Installation
* Fork this repository(optional if not contributing)
* Clone this repository
* create a virtual environment and activate it
* Install the requirements ```pip install -r requirements.txt```
* Run the python Api_app.py (run like any other python file) once the server is on and running hop on to [Home](http://127.0.0.1:5000) 

  
Note- Debug mode is on *for now*

## Build 

```pip install -e .```

---
## Update
1) Get can be fetched for both endpoints.Client: **[Client](http://127.0.0.1:5000/client)**  Place: **[Place](http://127.0.0.1:5000/place)** 
2) Post available for both client's and place's endpoint.
3) Tested on Postman and the tests right now contains only the json file of the entire collection of testing.
