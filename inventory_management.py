from typing import List, Dict

def create_inventory(input_list:List):
    inventory = {}

    for item in input_list:
        if item not in inventory.keys():
            inventory[item] = 0
        inventory[item] += 1
    return inventory

def add_item(dict: Dict, item_list: List):
    for item in item_list:
        if item not in inventory_dict.keys():
            inventory_dict[item] = 0
        inventory_dict[item] += 1
    return dict

def decrement_items(dict: Dict, item_list: List):
    for item in item_list:
        if item in dict.keys():
            dict[item] -= 1
            if dict[item] < 0:
                dict[item] = 0
    return dict

def remove_item(dict: Dict, item:str):
    if item in inventory_dict.keys():
        del inventory_dict[item]
    return dict

def list_inventory(dict: Dict):
    result = []
    for item, count in inventory_dict.items():
        if count > 0:
            result.append((item, count))
    return result


