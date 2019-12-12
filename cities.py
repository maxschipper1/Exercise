cities = ["madrid", "stockholm", "Tokyo", "Berlin"]

def contains (list, city):
    for a in list:
        if a == city:
            contain = True
    if contain == True:
        return True
    else:
        return False
            
print(contains(cities, "stockholm"))
