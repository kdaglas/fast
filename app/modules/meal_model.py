from app.database.dbfuncs import DatabaseFunctions

'''Object classes for the meal model'''
all_meals = []

class Meal():
    
    def __init__(self, thetype, food, price, description):
        '''Initialising the order class'''
        self.thetype = thetype
        self.food = food
        self.price = price
        self.description = description
    
    
    @staticmethod
    def adding_meal(thetype, food, price, description):
        '''this method returns a dictionary format of the meal class'''
        DatabaseFunctions.add_new_meal(
            thetype = thetype,
            food = food,
            price = price,
            description = description
        )

    
    @classmethod
    def get_all_meals(cls):
        '''this method returns the added meals'''
        return DatabaseFunctions.get_all_meals()

    
    @classmethod
    def get_one_meal(cls, mealId):
        '''This method returns the one meal'''
        if int(mealId) > 0:
            if len(all_meals) > 0:
                for meal in all_meals:
                    if meal.get('mealId') == int(mealId):
                        return meal
                return {"message": "meal doesnot exist"}
            return {"message": "No meal has been registered yet"}
        return {"message": "Meal id has to bigger than zero"}
        
    
    @classmethod
    def update_order(cls, mealId, price):
        '''this method return the edited order'''
        for meal in all_meals:
            if meal.get('mealId') == int(mealId):
                meal['price'] = price
                return meal
        return {'There is an error': 'No meal Found'}
