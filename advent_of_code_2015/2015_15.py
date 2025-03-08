import numpy as np
from itertools import product


ingredients = {
    "Sprinkles": [2, 0, -2, 0, 3],
    "Butterscotch": [0, 5, -3, 0, 3],
    "Chocolate": [0, 0, 5, -1, 8],
    "Candy": [0, -1, 0, 5, 8]
}

A = np.array(list(ingredients.values()))
ingredient_names = list(ingredients.keys())


def calculate_product_score(var_values):
    properties = np.dot(A[:, :4].T, var_values)
    properties = np.maximum(properties, 0)
    calories = np.dot(A[:, 4], var_values)
    # to get part one result, remove the 500 calories constraint
    # if calories == 500:
    #     return np.prod(properties)
    # else:
    #     return 0
    return np.prod(properties)


max_score = 0
best_solution = None
for values in product(range(101), repeat=len(ingredient_names)):
    if sum(values) == 100:
        score = calculate_product_score(values)
        if score > max_score:
            max_score = score
            best_solution = {ingredient_names[i]: values[i] for i in range(len(values))}


print(f"Best solution: {best_solution}")
print(f"Maximum Score: {max_score:.2f}")

