"""Phone inventory."""


def phone_brand_and_models(all_phones: str):
    """
    Create a list of structured information about brands and models.

    For each different phone brand in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the brand (string),
    the second element is a list of models for the given brand (list of strings).

    No duplicate brands or models should be in the output.

    The order of the brands and models should be the same as in the input list (first appearance).

    "Honor Magic5,IPhone 11,IPhone 12,Google Pixel,Samsung Galaxy S22,IPhone 13,IPhone 13,Google Pixel2" => [[
    'Honor', ['Magic5']], ['IPhone', ['11', '12', '13']], ['Google', ['Pixel', 'Pixel2']], ['Samsung', ['Galaxy S22']]]
    """
    all_phones_list = all_phones.split(",")
    brand_model_dict = {}

    for phone_name in all_phones_list:
        parts = phone_name.strip().split(' ')
        if len(parts) >= 2:
            brand = parts[0]
            models = ' '.join(parts[1:])

            if brand not in brand_model_dict:
                brand_model_dict[brand] = [models]
            else:
                if models not in brand_model_dict[brand]:
                    brand_model_dict[brand].append(models)

    output_list = [[brand, models] for brand, models in brand_model_dict.items()]

    return output_list


def add_phones(phone_list, all_phones) -> list:
    """
    Add phones from the list into the existing phone list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated phones (as in all the previous functions).
    The task is to add phones from the string into the list.

    Hint: This and phone_brand_and_models are very similar functions. Try to use one inside another.

    [['IPhone', ['11']], ['Google', ['Pixel']]] and "IPhone 12,Samsung Galaxy S22,IPhone 11"

        =>

    [['IPhone', ['11', '12']], ['Google', ['Pixel']], ['Samsung', ['Galaxy S22']]]
    """
    new_phones_list = phone_brand_and_models(all_phones)

    for new_brand, new_models in new_phones_list:
        brand_exists = False
        for existing_brand, existing_models in phone_list:
            if new_brand == existing_brand:
                for model in new_models:
                    if model not in existing_models:
                        existing_models.append(model)
                brand_exists = True
                break

        if not brand_exists:
            phone_list.append([new_brand, new_models])

    return phone_list


def number_of_phones(all_phones: str) -> list:
    """
    Create a list of tuples with brand quantities.

    The result is a list of tuples.
    Each tuple is in the form: (brand_name: str, quantity: int).
    The order of the tuples (brands) is the same as the first appearance in the list.
    """
    if len(all_phones) < 1:
        return []

    list_of_phones = all_phones.strip().split(',')
    quantity_dict = {}

    for phone in list_of_phones:
        phone_parts = phone.split(" ")
        brand = phone_parts[0]

        if brand in quantity_dict:
            quantity_dict[brand] += 1
        else:
            quantity_dict[brand] = 1

    return [(brand, quantity) for brand, quantity in quantity_dict.items()]


def phone_list_as_string(phone_list: list) -> str:
    """
    Create a list of phones.

    The input list is in the same format as the result of phone_brand_and_models function.
    The order of the elements in the string is the same as in the list.
    [['IPhone', ['11']], ['Google', ['Pixel']]] =>
    "IPhone 11,Google Pixel"
    """
    phones = []

    for brand, models in phone_list:
        brand = brand + " "
        for model in models:
            phones.append(brand + model)

    phones_string = ",".join(phones)

    return phones_string


print(phone_brand_and_models("Honor Magic5,Google Pixel2,Google Pixel6,IPhone 7,Google Pixel,Google Pixel,IPhone 14"))
# [['Honor', ['Magic5']], ['Google', ['Pixel2', 'Pixel6', 'Pixel']], ['IPhone', ['7', '14']]]

print(phone_brand_and_models("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))  # [['Google', ['Pixel']]]
print(phone_brand_and_models(""))  # []

print(add_phones([['IPhone', ['11']], ['Google', ['Pixel']]], "IPhone 12,Samsung Galaxy S22,IPhone 11"))
# [['IPhone', ['11', '12']], ['Google', ['Pixel']], ['Samsung', ['Galaxy S22']]]

print(number_of_phones("IPhone 11,Google Pixel,Honor Magic5,IPhone 12"))  # [('IPhone', 2), ('Google', 1), ('Honor', 1)]

print(number_of_phones("HTC one,HTC one,HTC one,HTC one"))  # [('HTC', 4)]

print(number_of_phones(""))  # []

print(phone_list_as_string([['IPhone', ['11']], ['Google', ['Pixel']]]))  # "IPhone 11,Google Pixel"
