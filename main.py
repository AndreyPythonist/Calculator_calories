set_dishes = [
    {"name": "рис", "protein": 2.7, "carbs": 28, "fats": 0.3, "calories": 130},
    {"name": "гречка", "protein": 4.2, "carbs": 21.3, "fats": 1.1, "calories": 118},
    {"name": "макароны", "protein": 3.6, "carbs": 20, "fats": 0.4, "calories": 98},
    {"name": "говядина", "protein": 20.2, "carbs": 0, "fats": 2.8, "calories": 106},
    {"name": "курица", "protein": 18.2, "carbs": 0, "fats": 18.4, "calories": 130},
    {"name": "свинина", "protein": 19.4, "carbs": 0, "fats": 7.1, "calories": 130}
]


sum_nutrients = {}


def calculate_calories():
    try:
        product, sum = input("Введите колличество в г. и наименование блюда через пробел: ").lower().split()
        sum = int(sum) * 0.01
    except ValueError:
        raise ValueError("Введите два значения через пробел, наименование и грамовку")
    for i in set_dishes:
        if i["name"] == product:
            return {"protein": round(i["protein"] * sum, 2),
                    "carbs": round(i["carbs"] * sum, 2),
                    "fats": round(i["fats"] * sum, 2),
                    "calories": round(i["calories"] * sum, 2)
                    }
    return "Данного продукта нет в списке"


# выводит значения для двух продуктов
for _ in range(2):
    dict_sum = calculate_calories()
    for i in dict_sum:
        if i in sum_nutrients.keys():
            sum_nutrients[i] = dict_sum.get(i) + sum_nutrients.get(i)
        else:
            sum_nutrients[i] = dict_sum.get(i)


print(f"Вы съели белка: {sum_nutrients['protein']}, "
      f"углеводов: {sum_nutrients['carbs']}, "
      f"жиров: {sum_nutrients['fats']}, "
      f"общий калораж {sum_nutrients['calories']}")
