# fastFoodfast

[![Build Status](https://travis-ci.org/kdaglas/fastFoodfast.svg?branch=ft-fastFoodfast-db-160870594)](https://travis-ci.org/kdaglas/fastFoodfast)
[![Coverage Status](https://coveralls.io/repos/github/kdaglas/fastFoodfast/badge.svg?branch=ft-fastFoodfast-db-160870594)](https://coveralls.io/github/kdaglas/fastFoodfast?branch=ft-fastFoodfast-db-160870594)
[![Maintainability](https://api.codeclimate.com/v1/badges/fb24e124bc0e05e50948/maintainability)](https://codeclimate.com/github/kdaglas/fastFoodfast/maintainability)

This is a food delivery service app for a restaurant that allows customers to make orders of their favorite meals they like. This app is hosted on: 
- [www.fastFoodfast.com](https://kdaglas.github.io/fastFoodfast/UI/index.html)

## fastFoodfast-api

The api allows the customers to post and get data from the app through API end points that are creating a connection of the client with the database. An customer can register and login to the app, order for a meal, view a single order made, view all the orders made, view their order history, update or modify or change a particular order they feel does not meet what they want and also view the menu with all the available meals. Whereas an administrator can login to the app, get the menu of the meals and add a food option to the menu.API is being hosted by heroku at: 
- [www.fastFoodfast-api2.com](https://douglas-fastfoodfast-db.herokuapp.com/api/v2/auth/signup)

### Prerequisites

- Use a web browser preferrably Chrome.
- You need to have Python3 installed on your computer. To install it go to:
  Python [https://www.python.org/]
Note: Python needs to be installed globally (not in the virtual environment)

### Features

- Register a customer
- Login a customer who already has an account
- Enable a customer to make an order
- Enable a customer to view contents of their order
- Enable a customer to view all orders made
- Enable a customer to view a history of the ordered meals
- Enable a customer to update, modify or change an order

- Login an admin who is the super user
- Enable an admin to get and view the menu of the meals
- Enable an admin to a food option to the menu

### Getting Started

Clone the project to your computer either by downloading the zip or using git.
To use git, run the code below:
```
    git clone https://github.com/kdaglas/fastFoodfast.git
```

Install postgreSQL on your machine, you can get it from here: [Postgres download](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
After downloading it, install it and lauch the Postgres shell where you can create a database by typing this in the shell
```
    '''this is for your actual database'''
    CREATE DATABASE fastfoodfast;

    '''this is for your tests database'''
    CREATE DATABASE testdb;
```

Go into the folder, create a virtual environment, activate it and then use a pip command to install the requirements necessary for the app to function. Below are the steps to take:
```
    $ cd fastFoodfast-db
    $ virtualenv envn <or any name of your choice>

    <!-- for ubuntu use this command-->
    $ source envn/bin/activate

    <!-- for windows use this command-->
    $ envn\bin\activate

    $ pip install -r requirements.txt
```

When this is done then run the application by typing this command
```
$ python run.py
```

You can use Postman to checkout the functionality of the api endpoints, you can download here:
- [Postman](https://www.getpostman.com/apps) - An API testing tool for developers

Use this data as dummy data for you to check for the functionality of the APIs you:
 ```
 For placing an order
    {
        'customerId' : "12345",
        'thetype' : "breakfast",
        'food' : "milk and bread",
        'price' : "2000",
        'quantity' : "2"
    }

For updating the staus of an order 
    {
        'customerId' : "12345",
        'thetype' : "breakfast",
        'food' : "milk and bread",
        'price' : "2000",
        'quantity' : "2",
        'status' : "completed"
    }
```

### Tests

To run tests, make sure that pytest or nose is installed. you can run that command to install them
```
    $ pip install -r requirements.txt
```
Then run these commands to begin testing the API
```
    $ nosetests

    <!-- or -->
    $ pytest
```

### Endpoints to make an order, view all orders, view a specific order and update an order status.

 HTTP Method | End point | Action
-------|-------|-------
 POST | /api/v2/register | Register a customer
 POST | /api/v2/login | Login a customer
 POST | /api/v2/meals | Add a food option to the menu
 GET | /api/v2/meals | Get the menu for all the meals
 POST | /api/v2/orders | Place an order
 GET | /api/v2/orders | Get all orders
 GET | /api/v2/orders | View order history for a particular customer
 GET | /api/v2/orders/<orderId> | Fetch a specific order
 PUT | /api/v2/orders/<orderId> | Update the status of an order

### Built With

- HTML5 and CSS3
- [Python](https://www.python.org/) - A programming language
- [Flask](https://flask.pocoo.org/) - Python webframework

### Authors

Douglas Kato
