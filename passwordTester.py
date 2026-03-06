passwd = input ("Write an example for a password to check it's robustness: ")

not_allowed = ["123", "qwerty", "abc", "ABC", "QWERTY", "321"]

def check_if_pass_contains(passwd):
    is_passwd_long(passwd)
    is_passwd_lower(passwd)
    is_passwd_upper(passwd)
    has_passwd_numbers(passwd)
    has_passwd_special_characters(passwd)
    is_passwd_easy_to_guess(passwd)
    return print("password is good")

def is_passwd_lower(passwd):
    for i in range(len(passwd)):
        if passwd[i].islower():
            return True
    raise ValueError("Password missing lowercase letter")

def is_passwd_upper(passwd):
    for i in range(len(passwd)):
        if passwd[i].isupper():
            return True
    raise ValueError("Password missing uppercase letter")

def has_passwd_numbers(passwd):
    for i in range(len(passwd)):
        if passwd[i].isnumeric():
            return True
    raise ValueError("Password missing a numeric letter")

def is_passwd_long(passwd):
    if len(passwd) < 12:
        raise ValueError("Password is to short, it needs to be 12 characters")

def has_passwd_special_characters(passwd):
    for i in range(len(passwd)):
        if not passwd[i].isalnum():
            return False
    raise ValueError("Password missing a special letter")

def is_passwd_easy_to_guess(passwd):
    for elem in not_allowed:
        if elem in passwd:
            raise ValueError("Password contains a sequence that is easy to guess")
        
check_if_pass_contains(passwd = passwd)  

