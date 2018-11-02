import xml.etree.ElementTree as ET
import json
import glob
import re
import os


def get_paths(glob_pth):
    row_list_paths = glob.iglob(glob_pth, recursive=True)
    return [p for p in row_list_paths if 'old' not in p]



def get_customer_info(local_pth):
    local_pth_lst = local_pth.split(os.sep)[-4:-1]
    return local_pth_lst

def get_cinema_info(cinema_path):
    pass


def serialize_customer(list_obj):
    return {
        "model": "cinemas.customer",
        "fields": {
            "iso": list_obj[:2],
            "name": list_obj[3:]
         }
    }

def serialize_cinema(list_obj, dict_obj):
    return {
        "model": "cinemas.cinema",
        "fields": {
            "owner": [
                list_obj[1][:2],
                list_obj[1][3:]
            ],
        "title": dict_obj,
        "uniqueid": dict_obj,
        "ownervalue": dict_obj,
        "creation": dict_obj
        }
    }



def get_cinema_fields(path):
    pass



def main():

    global_path = r'..\parse_db\*\*\*\**\Cinema.xml'
    list_of_customers = list(set([get_customer_info(p)[-2] for p in get_paths(global_path)]))
    list_of_customers_dicts = [serialize_customer(i) for i in list_of_customers]

    list_of_cinemas = []

    # print(list_of_customers_dicts)
    # with open(r'..\scc2_legacy\cinemas\fixtures\customers.json', 'w') as file:
    #     json.dump(list_of_customers_dicts, file, indent=2)



if __name__ == '__main__':
    main()