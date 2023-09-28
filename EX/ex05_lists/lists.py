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


def filter_search_result(all_phones, search):
    """Return list of search matching phones."""
    if search != "":
        result_list = []
        case_insensitive_search = search.lower()
        for phone in list_of_phones(all_phones):
            if case_insensitive_search in phone.lower():
                result_list.append(phone)

        return result_list
    else:
        return []


def search_by_brand(all_phones: str, search: str) -> list:
    """Return list of results based on the searched brad."""
    brands = phone_brands(all_phones)
    case_insensitive_search = search.lower()
    searched_brand = ""
    for brand in brands:
        if case_insensitive_search == brand.lower():
            searched_brand = brand

    return filter_search_result(all_phones, searched_brand)


def search_by_model(all_phones: str, search: str) -> list:
    """Return list of results based on the searched model."""
    models = phone_models(all_phones)
    case_insensitive_search = search.lower()
    searched_model = ""
    for model in models:
        if " " in model:
            list_model = model.split(" ")
            for item in list_model:
                if case_insensitive_search == item.lower():
                    searched_model = case_insensitive_search
                    break
        else:
            if case_insensitive_search == model.lower():
                searched_model = model

    return filter_search_result(all_phones, searched_model)


print(list_of_phones("Google Pixel,Honor Magic5,Google Pixel"))  # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
print(phone_brands(
    "Google Pixel,Honor Magic5,Google Pix,Honor Magic6,IPhone 12,Samsung S10,Honor Magic,IPhone 11"))  # ['Google',
# 'Honor', 'IPhone', 'Samsung']
print(phone_brands("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))  # ['Google']
print(phone_brands(""))  # []
print(phone_models("IPhone 14,Google Pixel,Honor Magic5,IPhone 14 Pro"))  # ['14', 'Pixel', 'Magic5']
print(search_by_brand("Google Pixel, Iphone 11 Pro", 'Google'))  # ['Google Pixel']
print(search_by_model("Google Pixel, Iphone 11 Pro", "Pixel"))  # ['Google Pixel']
print(search_by_brand("Google Pixel, GOOGLE Pixel, GooGle Pixel, GooGLE Pixel2, google Pixel 2022, Samsa Pixel", "Google"))  # 'Google Pixel', 'GOOGLE Pixel', 'GooGle Pixel', 'GooGLE Pixel2', 'google Pixel 2022']
print(search_by_model("Google Pixel, GOOGLE Pixel, GooGle Pixel, GooGLE Pixel2, google Pixel 2022, Samsa Pixel", "Pixel"))  # 'Google Pixel', 'GOOGLE Pixel', 'GooGle Pixel', 'GooGLE Pixel2', 'google Pixel 2022']
print(search_by_model('Google Pixel 2021, Google Pixel 2022', "pixel"))  # ['Google Pixel 2021', 'Google Pixel 2022']
