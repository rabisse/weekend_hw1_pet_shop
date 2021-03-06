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

#####OPTIONAL#####

# def customer_can_afford_pet(customer, new_pet):
#     can_afford = False
#     if customer["cash"] >= new_pet["price"]:
#         can_afford = True
#     return can_afford

def customer_can_afford_pet(customer, new_pet):
    return customer["cash"] >= new_pet["price"]

#####INTEGRATION#####
# check for pet
# check for sufficient funds
# add customer cash to total cash
# add pet to customer
# remove pet by name
# increase pets sold


def sell_pet_to_customer(shop, pet, customer):
    if pet == None:
        return
    if customer_can_afford_pet(customer, pet):
        add_or_remove_cash(shop, pet["price"])
        remove_customer_cash(customer, pet["price"])
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(shop, pet["name"])
        increase_pets_sold(shop, 1)


