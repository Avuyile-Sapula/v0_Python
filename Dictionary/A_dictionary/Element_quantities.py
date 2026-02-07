def element_quantities(quantities):
    result = []
    for element, count in quantities.items():
        result.extend([element] * count)
    return result

quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']


