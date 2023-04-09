import requests
import os   # We add 'requests' and 'os' package. We will use this package in our code.
# The pre-written codes in these packages will help us.
meal_types = ['breakfast', 'lunch', 'dinner', 'snack', 'teatime']
diet_types = ['balanced', '	high-fiber', 'high-protein', 'low-carb', 'low-fat', 'low-sodium']
#  We wrote the 2 arrays here so that the user knows the options to enter.


def recipe_search(ingredient, not_ingredient, meal_type, diet_type, time, calories):
    #  We have 6 parameters in this function.(ingredient, not_ingredient, meal_type, diet_type, time, calories)
    #  We get app_id and app_key from edamam account.
    app_id = '29e05562'                           # input('Enter your app id:')
    app_key = 'c0b6129424d18da5bbec7611588594b4'  # input('Enter your app key:')
    # From 11 to 23, the data in the variables is added to url_string if the data in variables  is not equal 'none'
    url_string = 'https://api.edamam.com/api/recipes/v2?type=public&q='
    url_string += ingredient
    if not_ingredient != 'none':
        url_string += '&excluded=' + not_ingredient
    if meal_type != 'none':
        url_string += '&MealType=' + meal_type
    if diet_type != 'none':
        url_string += '&Diet=' + diet_type
    if time != 'none':
        url_string += '&Time=' + time
    if calories != 'none':
        url_string += '&Calories=' + calories
    url_string += '&app_id=' + app_id + '&app_key=' + app_key + '&random=false'
    #  According to the data we entered, our url (Uniform Resource Locator) address was created.
    result = requests.get(url_string)
    # With the help of requests.get(url_string), the data we want from the site is transferred to result.
    data = result.json()
    # With the help of .json()  function, the information in the result is transferred to
    # the data(the name of the variable).
    return data['hits']
    #  Where data(the name of the variable) returns the information under 'hits' to
    #  recipe_search(ingredient, not_ingredient, meal_type, diet_type, time, calories)


def run():  # This code starts running from the run function.
    question = input('Do you want to search for a recipe? y/n ')
    # The user is prompted to enter whether she/he wants to search for a recipe or not.
    # If user wants to search recipe then the code continues with if condition.
    # If user doesn't want to search recipe then the code continues with question_1 (line 64).
    # We assume the user wants to search for recipe.
    if question == 'y':  # If condition is true then we go inside if condition.
        ingredient = input('What would you like an ingredient in recipes? ')
        #  We ask the user to enter the ingredient  want in the recipe.
        question_2 = input('Are you allergic to any food? y/n ')
        #  We ask the user if he/she is allergic to any ingredient.
        if question_2 == 'y':  # If the user has allergies the if condition works or
            # if not then else condition works. We assume the user has an allergies.
            not_ingredient = input('What would not you like an ingredient in recipes? ')  # We get data from the user.
        else:
            not_ingredient = 'none'

        question_3 = input('Do you want to specify the meal type? y/n ')
        # This way other if and else conditions work based on input. if the user says 'y',
        # the program asks for specific meal types.
        # The user can choose between the preferences written on the list meal_types.
        # if not the program will go the else statement and meal_type = 'none'
        if question_3 == 'y':
            meal_type = input('What is your meal type? ')
        else:
            meal_type = 'none'

        question_4 = input('Are you on a diet? y/n ')  # The user can choose between diet types if they type 'y'.
        # The diet types are in the list named diet_types . if not the program will go the else statement.
        if question_4 == 'y':
            diet_type = input('What is your diet type? ')
        else:
            diet_type = 'none'

        question_5 = input('Do you want to limit recipe time? y/n ')  # The user has the option to put in a time limit
        # for how long they want to spend in the kitchen, by typing 'y'.
        # if not the program will go the else statement.Where '%2D' means hyphen.
        # This information is given to us in https://developer.edamam.com/edamam-docs-recipe-api .
        # This sign allows us to get a recipe between two time (min-max).
        # The transformations of other characters are also here.  https://www.w3schools.com/tags/ref_urlencode.asp
        if question_5 == 'y':   # https://www.w3schools.com/tags/ref_urlencode.asp
            time = input('What is the minimum amount of time you want to cook? ') + '%2D' +\
                   input('What is the maximum amount of time you want to cook? ')
        else:
            time = 'none'

        question_6 = input('Do you want to limit calories? y/n ')
        if question_6 == 'y':
            calories = input('What is the minimum amount of calories you want to recipe? ') + '%2D' + \
                       input('What is the maximum amount of calories you want to recipe? ')
        else:
            calories = 'none'

        results = recipe_search(ingredient, not_ingredient, meal_type, diet_type, time, calories)
        # The results that will appear are the items
        # that the function recipe_search will return with all the variables answered by the user.

        if os.path.exists("recipe_book.txt") and os.path.isfile("recipe_book.txt"):
            # os.path.exists("recipe_book.txt") checks if the file already exists.
            # If recipe_book.txt  doesn't exist it creates.
            # os.path.isfile() method in Python is used to check whether
            # the specified path is an existing regular file or not.
            os.remove("recipe_book.txt")      # This row deletes the contents of the file.
        for result in results:
            recipe = result['recipe']
            print(recipe['label'], '\n', recipe['url'], '\n', recipe['ingredientLines'])
            # For loop prints the 'label' ,'url' and 'ingredientLines' information of the recipe to the output.
            # Skips a line before printing 'url' and 'ingredientLines' with the help of '\n' .
            with open('recipe_book.txt', 'a+') as recipes_file:
                # The a+ mode opens the file for both reading and appending.
                # The file pointer in this mode is placed at the end of the file if it already exists in the system.
                # The file opens in the append mode. If the file does not exist, then it is created for writing.
                save = recipe['label'] + '\n' + recipe['url'] + '\n'
                # 'label' and 'url'  information is transferred to variable save  and printed to file
                recipes_file.write(save)

    question_1 = input('Do you want to enter a new recipe in your recipe book? y/n ')
    # The user has the option to put in their own recipe, in a txt file called my_recipe_book.
    if question_1 == 'y':

        with open('my_recipe_book.txt', 'a+') as my_recipe_book_file:
            # If the user wants to create her own recipe book, a new file named my_recipe_book   is opened.
            recipe_name = str(input('Enter your recipe name : ')) + '\n'  # Get recipe name from user.
            upper = str(recipe_name.upper())  # Recipe name is converted to upper case if written in lower case.
            my_recipe_book_file.write(upper)  # Recipe name prints to file.
            my_recipe_book_file.write('Ingredients :' + '\n')
            # Ingredients is written to the file and one line is skipped.
            ingredients_count = int(input('How many ingredients are there in your recipe? : '))
            # The user is asked how many materials to enter.

            for x in range(ingredients_count):  # Each item is requested to be entered one by one and prints to file.
                ingredients = input('Enter your recipe^s ingredients : ') + '\n'
                my_recipe_book_file.write(ingredients)

            end_step = int(input('How many steps are there in your recipe? : '))
            # In the same way, the number of recipe steps is requested and entered one by one.
            i = 0
            for x in range(end_step):
                i += 1
                my_recipe_book_file.write('STEP' + str(i) + ':')  # Each step is specified with the i variable.
                steps = input('Enter your recipe^s step: ') + '\n'
                my_recipe_book_file.write(steps)


run()
