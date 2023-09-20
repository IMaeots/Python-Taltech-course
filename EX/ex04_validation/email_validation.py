"""Email validation."""


# Write your functions here
def has_at_symbol(email: str):
    for i in email:
        if i == "@":
            return True

    return False


def is_valid_username(email: str):
    email_parts = email.split("@")
    if len(email_parts) > 2:
        return False
    else:
        for i in email_parts[0]:
            if not i.isalnum():
                if i == ".":
                    continue
                else:
                    return False

        return True


def find_domain(email: str):
    return email.split("@")[-1]


def is_valid_domain(email: str):
    domain = find_domain(email)
    dot_count = 0
    count = 0
    for i in domain:
        count += 1
        if not i.isalpha():
            if i == "." and dot_count == 0:
                dot_count = 1
                if count < 3 or count > 10:
                    return False
                else:
                    count = 0
            else:
                return False
    if count < 2 or count > 5:
        return False
    elif dot_count == 1:
        return True
    else:
        return False


def is_valid_email_address(email: str):
    return has_at_symbol(email) and is_valid_username(email) \
        and is_valid_domain(email)


def create_email_address(domain: str, username: str):
    email = f"{username}@{domain}"
    if is_valid_email_address(email):
        return email
    else:
        return "Cannot create a valid email address using the given parameters!"


if __name__ == '__main__':
    print("Email has the @ symbol:")
    print(has_at_symbol("joonas.kivi@gmail.com"))  # -> True
    print(has_at_symbol("joonas.kivigmail.com"))  # -> False

    print("\nUsername has no special symbols:")
    print(is_valid_username("martalumi@taltech.ee"))  # -> True
    print(is_valid_username("marta.lumi@taltech.ee"))  # -> True
    print(is_valid_username("marta lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta&lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta@lumi@taltech.ee"))  # -> False

    print("\nFind the email domain name:")
    print(find_domain("karla.karu@saku.ee"))  # -> saku.ee
    print(find_domain("karla.karu@taltech.ee"))  # -> taltech.ee
    print(find_domain("karla.karu@yahoo.com"))  # -> yahoo.com
    print(find_domain("karla@karu@yahoo.com"))  # -> yahoo.com

    print("\nCheck if the domain is correct:")
    print(is_valid_domain("pihkva.pihvid@ttu.ee"))  # -> True
    print(is_valid_domain("metsatoll@&gmail.com"))  # -> False
    print(is_valid_domain("ewewewew@i.u.i.u.ewww"))  # -> False
    print(is_valid_domain("pannkook@m.oos"))  # -> False

    print("\nIs the email valid:")
    print(is_valid_email_address("DARJA.darja@gmail.com"))  # -> True
    print(is_valid_email_address("DARJA=darjamail.com"))  # -> False

    print("\nCreate your own email address:")
    print(create_email_address("hot.ee", "vana.ema"))  # -> vana.ema@hot.ee
    print(create_email_address("jaani.org", "lennakuurma"))  # -> lennakuurma@jaani.org
    print(create_email_address("koobas.com",
                               "karu&pojad"))  # -> Cannot create a valid email address using the given parameters!
