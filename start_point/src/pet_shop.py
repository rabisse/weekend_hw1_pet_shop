# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, change_in_cash):
    shop["admin"]["total_cash"] += change_in_cash

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, num_pets_sold):
    shop["admin"]["pets_sold"] += num_pets_sold

def get_stock_count(shop):
    return len(shop["pets"])


def get_pets_by_breed(shop, breed):
    breed_list = []
    for pet in shop["pets"]:
        if breed == pet["breed"]:
            breed_list.append(pet)
    return breed_list


def find_pet_by_name(shop, name):
    found_pet = None
    for pet in shop["pets"]:
        if name == pet["name"]:
            found_pet = pet
    return found_pet

############################
def remove_pet_by_name(shop, name):
    pets = shop["pets"]
    for index, pet in enumerate(pets):
        if name == pet["name"]:
            del pets[index]


def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, less_cash):
    customer["cash"] -= less_cash


def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)



