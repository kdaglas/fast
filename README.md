# fastFoodfast

This is a food delivery service app for a restaurant that allows customers to make orders of their favorite meals they like.
This app is hosted on https://kdaglas.github.io/fastFoodfast/UI/index.html

## fastFoodfast-api

This api allows the customers to register and login to the app, order for a meal, view a single order made, view all the orders made and update or modify or change a particular order they feel does not meet what they want.

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

when you are done then run the application by typing this command
```
$ python run.py
```

### Final result:

API is being hosted by heroku at:


### Built With

- HTML5 and CSS3
- [Python](https://www.python.org/) - A programming language
- [Flask](https://flask.pocoo.org/) - Python webframework

### Authors

Douglas Kato
