# fastFoodfast

[![Build Status](https://travis-ci.org/kdaglas/fastFoodfast.svg?branch=fastFoodfast-api)](https://travis-ci.org/kdaglas/fastFoodfast)
[![Coverage Status](https://coveralls.io/repos/github/kdaglas/fastFoodfast/badge.svg?branch=fastFoodfast-api)](https://coveralls.io/github/kdaglas/fastFoodfast?branch=fastFoodfast-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/fb24e124bc0e05e50948/maintainability)](https://codeclimate.com/github/kdaglas/fastFoodfast/maintainability)

This is a food delivery service app for a restaurant that allows customers to make orders of their favorite meals they like. This app is hosted on: 
- [www.fastFoodfast.com](https://kdaglas.github.io/fastFoodfast/UI/index.html)

## fastFoodfast-api

This api allows the customers to register and login to the app, order for a meal, view a single order made, view all the orders made and update or modify or change a particular order they feel does not meet what they want. API is being hosted by heroku at: 
- [www.fastFoodfast-api.com](https://douglas-fastfoodfast.herokuapp.com/api/v1/orders)

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

### Getting Started

Clone the project to your computer either by downloading the zip or using git.
To use git, run the code below:
```
    git clone https://github.com/kdaglas/fast.git
```

Go into the folder, create a virtual environment, activate it and then use a pip command to install the requirements necessary for the app to function. Below are the steps to take:
```
    $ cd fastFoodfast-api
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
 POST | /api/v1/orders | Place an order
 GET | /api/v1/orders | Get all orders
 GET | /api/v1/orders/<orderId> | Fetch a specific order
 PUT | /api/v1/orders/<orderId> | Update the status of an order

### Built With

- HTML5 and CSS3
- [Python](https://www.python.org/) - A programming language
- [Flask](https://flask.pocoo.org/) - Python webframework

### Authors

Douglas Kato
