"""Email validation."""


def has_at_symbol(email: str):
    """Look for symbol in email."""
    for i in email:
        if i == "@":
            return True

    return False


"""Check username correctness."""
def is_valid_username(email: str):
    """Check username correctness."""
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
    """Find the domain part of email."""
    return email.split("@")[-1]


def is_valid_domain(email: str):
    """Evaluate the correctness of domain name."""
    domain = find_domain(email)

    dot_count = 0
    alpha_count = 0
    for char in domain:
        if char == ".":
            dot_count += 1
            if dot_count > 1:
                return False
            elif alpha_count < 3 or alpha_count > 10:
                return False
            else:
                alpha_count = 0
        elif not char.isalpha():
            return False
        else:
            alpha_count += 1

    if alpha_count < 2 or alpha_count > 5:
        return False

    return dot_count == 1


def is_valid_email_address(email: str):
    """Evaluate the correctness of email."""
    return has_at_symbol(email) and is_valid_username(email) \
        and is_valid_domain(email)


def create_email_address(domain: str, username: str):
    """Try to create an email."""
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
