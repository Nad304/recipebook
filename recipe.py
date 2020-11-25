# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 01:16:01 2020

@author: nadin
"""

#this will be a dictionary that holds all the recipies and the ingredients in each

#recipe = {'Cookies':['egg', 'flour', 'brown sugar','baking powder','salt'],'Brownies':['egg', 'flour', 'cocopowder','sugar','baking powder', 'salt']}

#this will giv you all the keys in the dictionary 
#food = recipe.keys()
#['cookies','Brownies']
#to add reipes 
#recipe['new food'] = 'the ingredients '

#if you want all the ingredients of all the foods returned 
#use values() and it will return a list of all the vallues in the dictionary
#x = recipe.values()

#to check if a specified key is present in a dictionart use " in "
#if "Cookies" in recipe:
#    print("Cookies, is already in the cookbook")
    
#updating a recipe
#you can update an ingredient list by writing update
#recipe.update({'Pancake':['egg', 'flour', 'milk', 'vanila extract', 'sugar', 'salt']})

#removing a food out of the recipe book
#use pop()
#recipe.pop('Cookies')
#del recipe['Cookies']

#removing the last inserted item, 
#use, pop.item()

#how to loop through a dictionary 
#to print all key names 
#for food in recipe:
#    print(food)
    #to print the ingredients 
#for ingredients in recipe:
#    print(recipe[ingredients])
    
    
#the projects can have dictionary inside of a dictionary 
#recipebook = {'Lazy Cake':{'condensed milk':'half a can','coco powder':'6 TBS','powdered sugar':'6 TBS'}, 'Coffee Cake':{'maria biscuits':'half a pack','condensed milk':'small cup'}}
#how to access the element 
#print(recipebook['Lazy Cake']['condensed milk'])

#have nested dictionaries food, ingredient and the amount per

recipebook = { 'Latkes':{'potatoes':'1 1/2 pounds','Onion':'1/2','egg': '1','flour':'3 TBS','Salt':'1/8 TBS','pepper':'1/8 TBS','cayenne':'1/16 TBS','oil':'1/8 cup'},
              'Pancake':{'egg':'2', 'milk':'1 cup','vanilla extract':'2 TBS','salt':'a pinch','sugar':'1/4 cup'},
              'Nescafe Cake':{'maria biscuit':'1-2 rolls','dream whip':'2 packs','coffee':'1 cup, lukewarm with 2 TSP of coffee','cream':'1 can','condensed milk':'1 tea cup','coffee grounds':'2 TBS','sugar':'5 TBS'},
              'Lazy Cake':{'maria biscuit':'1-2 rolls','powdered sugar':'6TBS','coco':'6 TBS','butter':'1 stick','condensed milk':'1/2 can'},
              'Okra Stew':{'Okra':'1 packet','beef':'1/4 KG, chunks','tomatoe':'3','peeled tomatoes':'1/2 can','tomato paste':'1 can','onion':'1','tumeric':'1 TBS','cardamom':'2-3','bay leaf':'1','peppercorn':'3','salt':'1 TBS','cinnamon stick':'1','olive oil':'3 TBS','garlic':'5 cloves'},
              'cookies':{'egg': '1','milk':'1 cup','flour':'2 cups','brown sugar':'1 cup'},
              'brownies':{'egg':'1','milk':'1 cup','coco powder':'1/3 cup','flour':'1 cup'}}
#for dish_name,dish_info in recipebook.items():
#    print('\nDish Name:', dish_name)
    
#    for key in dish_info:
#        print(key + ':', dish_info[key])
current_ingredients = ['egg','milk','flour','brown sugar','mayonase','cookies','hot sauce','toast']
#print('Enter ingredient:')
#x = input()
#print('Here are the dishes that use that ingredient: ')
#for dish_name,dish_info in recipebook.items():

#    for key in dish_info:
#        if x == key:
#            y = dish_name
            
#            print (dish_name)
#this code scans the big dictionary and the current_ingredient list
#it checks one by one what ingredient matches exactly with the key
#if it finds a match it repaces the iteam in the current_ingredient list and shows 
#what 
small_dictionary = dict(map(lambda key: (key, recipebook.get(key, None)), current_ingredients))
print(small_dictionary)
#for recipe,ingredients in recipebook.items():
  
#        if ingredient not in current_ingredients:
#            break
#        else:
#            print('You have the ingredients to make: {}'.format(recipebook))