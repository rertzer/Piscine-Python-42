# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rertzer <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 15:34:03 by rertzer           #+#    #+#              #
#    Updated: 2022/12/05 17:00:24 by rertzer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


cookbook = {
        "sandwich" : {
            "ingredients"   : ["ham", "bread", "cheese", "tomatoes"],
                    "meal"  : "lunch",
                "prep_time" : 10
        },
        "cake" : {
            "ingredients"   : ["flour", "sugar", "eggs"],
                    "meal"  : "dessert",
                "prep_time" : 60
        },
        "salad" : {
            "ingredients"   : ["arugula", "tomatoes", "roquette"],
                    "meal"  : "lunch",
                "prep_time" : 15
        }
}

def print_all():
    for r in cookbook:
        print(r)

def print_recipe(r):
    print("Recipe for ", r)
    details = cookbook.get(r)
    print("Ingredients list:", details["ingredients"])
    print("To be eaten for:", details["meal"], ".")
    print("Takes ", details["prep_time"], " minutes of cooking.")

def delete_recipe(r):
    cookbook.pop(r)

def create_recipe():
    recipe = {
    }
    name = str(input("Enter a name :"))
    ingredients = str(input("Enter ingredients :")).split()
    meal = str(input("Enter meal type :"))
    time = int(input("Enter prep time :"))
    recipe.update({"ingredients": ingredients})
    recipe.update({"meal" : meal})
    recipe.update({"prep_time" : time})
    cookbook.update({name: recipe})

again = True
while again:
    print("\nWelcome to The Cookbook\n Available options:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    choice = int(input("Your choice: "))

    if choice == 1:
        create_recipe()
    elif choice == 2:
        recipe = str(input("Delete recipe: "))
        delete_recipe(recipe)
    elif choice == 3:
        recipe = str(input("Enter a recipe: "))
        print_recipe(recipe)
    elif choice == 4:
        print_all()
    elif choice == 5:
        again = False
