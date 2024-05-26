# Import requests package so we can interact with APIs.
import requests


def recipe_search(ingredient):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = '6f7ba7a2'
    app_key = 'cbc39e6681d92b748fbf921348af034e'
    # Make request to API using get amd add in the app_id and app+key variables. q is the query which matches the
    # user's ingredient input/choice
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    # Parse the JSON response into a dictionary and assign to variable called data
    data = result.json()
    # The recipes are returned within 'hits'
    return data['hits']


def run():
    # Ask user to enter an ingredient which can be queried in the API call
    ingredient = input('Enter an ingredient: ')
    # Ask user if they are vegetarian (simple y/n, with scope to improve)
    dietary_choice = input('Are you vegetarian? y/n: ')
    # Call the recipe-search function with the inputted ingredient as the argument and assign to variable results
    results = recipe_search(ingredient)
    # Handle if user is NOT a vegetarian below
    if dietary_choice == 'n':
        # We want to write all recipes in a separate file ,so we first need to open a new file
        with open('omnivore_recipes.txt', 'w+') as recipe_file:
            for result in results:
                recipe = result['recipe']
                print(f'This is the recipe name: {recipe['label']}')
                print(f'This is the recipe uri: {recipe['uri']}')

                recipe_file.write('Recipe Name: ' + str(recipe['label']) + '\n')
                recipe_file.write('Recipe URI: ' + str(recipe['uri']) + '\n')
                #         # print(result['recipe'].keys())
                # List of the ingredients required
                ingredients_list = result['recipe']['ingredients']
                # Declare and empty list and assign to a new variable called simple_ingredients_list
                simple_ingredients_list = []
                # Use a for loop to iterate through the ingredient's list and only pull out the text value
                # Append to the simple_ingredients_list
                for ingredient in ingredients_list:
                    simple_ingredients_list.append(ingredient['text'])
                # Write the simplified ingredients list to the recipe file
                recipe_file.write('Ingredients List: ' + str(simple_ingredients_list) + '\n' + '\n')
                print(f'Simple Ingredients list: {simple_ingredients_list}')

            recipe_file.write('*** Thank you for using our recipe search, we hope you enjoy the recipes provided :) ***')
    else:
        # Loop through recipe result, if healthLabels contains 'Vegetarian' then include the recipe
        # We used print statement when debugging to make sure our code was progressing to the next stage
        print('Made it to the vege section')
        with open('vegetarian_recipes.txt', 'w+') as recipe_file:
            for result in results:
                # print('for loop time')
                recipe = result['recipe']
                if 'Vegetarian' in recipe['healthLabels']:
                    print(f'This is the recipe name: {recipe['label']}')
                    recipe_file.write('Recipe Name: ' + str(recipe['label']) + '\n')
                    recipe_file.write('Recipe URI: ' + str(recipe['uri']) + '\n')
                    ingredients_list = result['recipe']['ingredients']
                    simple_ingredients_list = []
                    for ingredient in ingredients_list:
                        simple_ingredients_list.append(ingredient['text'])
                        # Write the simplified ingredients list to the recipe file
                    recipe_file.write('Ingredients List: ' + str(simple_ingredients_list) + '\n' + '\n')

            recipe_file.write(
                '*** Thank you for using our recipe search, we hope you enjoy the recipes provided :) ***')

run()
