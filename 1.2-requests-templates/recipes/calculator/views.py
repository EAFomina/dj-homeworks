from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
    'cheesecake': {
        'печенье, г': 200,
        'сливочное масло, г': 120,
        'крем-чиз, г': 170,
        'жирные сливки 33%, мл': 250,
        'сахарная пудра, г': 60,
        'фисташковая паста, ст.л.': 2,
        'фисташковая паста для верхнего слоя, г': 170,
    },
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipe(request, recipe_name):
    ingredients = DATA.get(recipe_name)
    servings = request.GET.get('servings', None)
    if servings:
        for ingredient in ingredients:
            ingredients[ingredient] *= int(servings)
    context = {
        'recipe': ingredients
    }
    return render(request, 'calculator/index.html', context)