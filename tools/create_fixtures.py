import json
from collections import Counter


def disassemble_title(json_obj):
    lst = json_obj['fields']['title'].split('-')
    lst2 = lst[1].split('.')
    json_obj['fields']['owner'] = [lst[-1], lst2[0]]
    json_obj['fields']['narrow_tag'] = lst[0].lower()
    return json_obj

def aces_guns_correct_wide_tag(json_obj):
    if json_obj['fields']['narrow_tag'] == 'AcesGuns':
        json_obj['fields']['wide_tag'] = 'Cinema'
    return json_obj

def create_customers(json_obj):
    return tuple(json_obj['fields']['owner'])

def serialize_customers(tup):
    return {"model": "cinemas.customer",
            "fields": {
                "iso": tup[1],
                "name": tup[0],
                }
            }

def update_slug(json_obj):
    lst = json_obj['fields']['title'].split('-')
    st = lst[0] + '-' + lst[1].split('.')[-1]
    if '.' in st:
        st = st.split('.')
        st = ''.join(st)
    json_obj['fields']['slug_field'] = st.lower()
    return json_obj

def update2_slug(json_obj):
    json_obj['fields']['slug_field'] = json_obj['fields']['slug_field'] + json_obj['fields']['uniqueid'][-13:]
    return json_obj

def update_slug_key(json_obj):
    json_obj['fields']['slug'] = json_obj['fields'].pop('slug_field')



def main():

    cinema_file = r'..\scc2_legacy\cinemas\fixtures\cinemas7.json'
    customer_file = r'..\scc2_legacy\cinemas\fixtures\customers.json'

    with open(cinema_file, 'r') as f:
        cinema_json_obj = json.load(f)

    # for j in cinema_json_obj:
    #     aces_guns_correct_wide_tag(j)
    #
    # for j in cinema_json_obj:
    #     disassemble_title(j)

    # customers_list = [create_customers(i) for i in cinema_json_obj]
    #
    # customers_list_serialize = [serialize_customers(i) for i in set(customers_list)]

    # for j in cinema_json_obj:
    #     update_slug(j)

    # for j in cinema_json_obj:
    #     update2_slug(j)

    # for j in cinema_json_obj:
    #     update_slug_key(j)
    #
    # with open(r'..\scc2_legacy\cinemas\fixtures\cinemas7.json', 'w') as f:
    #     json.dump(cinema_json_obj, f, indent=2)


if __name__=='__main__':
    main()