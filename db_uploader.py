import os
import django
import csv
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starbucks.settings')
django.setup()

from product.models import Menu, Category, Drink, Allergy, Nutrition, AllergyDrink

CSV_PATH_PRODUCTS = './starbucks.csv'


with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)

    menu_name = None
    category_name = []
    allergy_name = set()
    nutrition_id = 1
    for row in data_reader:

        #insert table menu
        if row[0] != menu_name:
            menu_name = row[0]
#            #Menu.objects.create(name = menu_name)
#        else:
#            continue

        #insert table category
#        if row[1] in category_name:
#            continue
#        else:
#            category_name.append(row[1])
#            menu_id = Menu.objects.get(name=menu_name).id
#            Category.objects.create(name=row[1], menu_id=menu_id)

        #insert table allergy
#        allergies = row[4].split('/')
#        for allergy in allergies:
#            allergy_names = allergy.strip(' ')
#            if allergy_names == '':
#                continue
#            else:
#                allergy_name.add(allergy_names)
#    for allergy in allergy_name:
#        Allergy.objects.create(name=allergy)

        #insert table drink
#        menu_id = Menu.objects.get(name=menu_name).id
#        category_name = row[1]
#        category_id = Category.objects.get(name=category_name).id
#        Drink.objects.create(name=row[2], menu_id=menu_id, category_id=category_id)

#        nutritions = row[3].split(',')
#        Nutrition.objects.create(
#            one_serving_kcal = nutritions[0],
#            sodium_mg = nutritions[1],
#            saturated_fat_g = nutritions[2],
#            sugars_g = nutritions[3],
#            protein_g = nutritions[4],
#            caffeine_mg = nutritions[5]
#        )
        drink_id = drink.objects.get(name=row[2]).id
#        drink = Drink.objects.get(id=nutrition_id)
#        drink.nutrition_id = nutrition_id
#        drink.save()
#        nutrition_id += 1

        #insert table allergies_drinks
        drink_id = Drink.objects.get(name=row[2]).id
        allergies = row[4].split('/')
        for allergy in allergies:
            allergy_name = allergy.strip(' ')
            if allergy_name == '':
                continue
            else:
                allergy_id = Allergy.objects.get(name=allergy_name).id
                AllergyDrink.objects.create(allergy_id = allergy_id, drink_id = drink_id)
