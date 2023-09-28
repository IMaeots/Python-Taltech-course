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
        model = " ".join(i.split(" ")[1:])
        if model in phone_models_list:
            continue
        else:
            phone_models_list.append(model)

    return phone_models_list


def search_by_brand(all_phones: str, search: str) -> list:
    """Return list of results based on the searched brad."""
    brands = phone_brands(all_phones)
    searched_brand = ""
    for i in brands:
        if search.lower() in i.lower():
            searched_brand = i

    if searched_brand != "":
        result_list = []
        for phone in list_of_phones(all_phones):
            if searched_brand in phone:
                result_list.append(phone)

        return result_list
    else:
        return []


def search_by_model(all_phones: str, search: str) -> list:
    """Return list of results based on the searched model."""
    models = phone_models(all_phones)
    case_insensitive_search = search.lower()
    searched_model = ""
    for model in models:
        for list_model in model:
            for i in range(len(list_model)):
                if case_insensitive_search == list_model[i].lower():
                    searched_model = model

    if searched_model != "":
        result_list = []
        for phone in list_of_phones(all_phones):
            if searched_model in phone:
                result_list.append(phone)

        return result_list
    else:
        return []


print(list_of_phones("Google Pixel,Honor Magic5,Google Pixel"))  # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
print(phone_brands(
    "Google Pixel,Honor Magic5,Google Pix,Honor Magic6,IPhone 12,Samsung S10,Honor Magic,IPhone 11"))  # ['Google', 'Honor', 'IPhone', 'Samsung']
print(phone_brands("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))  # ['Google']
print(phone_brands(""))  # []
print(phone_models("IPhone 14,Google Pixel,Honor Magic5,IPhone 14 Pro"))  # ['14', 'Pixel', 'Magic5']
print(search_by_brand("Google Pixel, Iphone 11 Pro", 'Google'))  # ['Google Pixel']
