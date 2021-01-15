# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, change_in_cash):
    shop["admin"]["total_cash"] = shop["admin"]["total_cash"] + change_in_cash

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, num_pets_sold):
    shop["admin"]["pets_sold"] = shop["admin"]["pets_sold"] + num_pets_sold

def get_stock_count(shop):
    return len(shop["pets"])


def get_pets_by_breed(shop, breed):
   # pets_list = shop["pets"]
    breed_list = []
    for pet in shop["pets"]:
        if breed == pet["breed"]:
            breed_list.append(pet)

    return breed_list


# def get_pets_by_breed(shop, breed):
#     breed_list = []
#     pet_list = [shop["pets"]]
#     for pet in pet_list:
#         if breed == pet_list["breed"]:
#             breed_list.append(pet)

#     return breed_list



