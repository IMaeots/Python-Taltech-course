"""Phone inventory."""


def invalid_input_check(all_phones: str) -> bool:
    """Return True if list has more than one character else False."""
    return len(all_phones) < 1


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    """
    if invalid_input_check(all_phones):
        return []

    return all_phones.split(',')


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google", "Honor"]
    """
    if invalid_input_check(all_phones):
        return []

    phone_brands_list = []
    for i in list_of_phones(all_phones):
        brand = i.split(" ")[0]
        if brand in phone_brands_list:
            continue
        else:
            phone_brands_list.append(brand)

    return phone_brands_list


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).

    "Honor Magic5,Google Pixel,Honor Magic4" => ['Magic5', 'Pixel', 'Magic4']
    """
    if invalid_input_check(all_phones):
        return []

    phone_models_list = []
    for i in list_of_phones(all_phones):
        model = i.split(" ")[1:]
        if model in phone_models_list:
            continue
        else:
            phone_models_list.append(model)

    return phone_models_list


def search_by_brand(all_phones: str, search: str) -> list:
    brands = phone_brands(all_phones)
    for i in brands:
        if search.lower() in i.lower():
            return i

    return []


def search_by_model(all_phones: str, search: str) -> list:
    models = phone_models(all_phones)
    case_insensitive_search = search.lower()
    for model in models:
        for list_model in model:
            for i in range(len(list_model)):
                if case_insensitive_search == list_model[i].lower():
                    return list_model

    return []


print(list_of_phones("Google Pixel,Honor Magic5,Google Pixel"))  # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
print(phone_brands("Google Pixel,Honor Magic5,Google Pix,Honor Magic6,IPhone 12,Samsung S10,Honor Magic,IPhone 11"))  # ['Google', 'Honor', 'IPhone', 'Samsung']
print(phone_brands("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))  # ['Google']
print(phone_brands(""))  # []
print(phone_models("IPhone 14,Google Pixel,Honor Magic5,IPhone 14"))  # ['14', 'Pixel', 'Magic5']
