passwd = input ("Write an example for a password to check it's robustness: ")

def check_if_pass_contains(passwd):
    is_passwd_long(passwd)
    is_passwd_lower(passwd)
    is_passwd_upper(passwd)
    has_passwd_numbers(passwd)
    has_passwd_special_characters(passwd)
    return print("password is good")

def is_passwd_lower(passwd):
    for i in range(len(passwd)):
        if passwd[i].islower():
            return True
    raise TypeError("Password missing lowercase letter")

def is_passwd_upper(passwd):
    for i in range(len(passwd)):
        if passwd[i].isupper():
            return True
    raise TypeError("Password missing uppercase letter")

def has_passwd_numbers(passwd):
    for i in range(len(passwd)):
        if passwd[i].isnumeric():
            return True
    raise TypeError("Password missing a numeric letter")


def is_passwd_long(passwd):
    if len(passwd) < 12:
        raise TypeError("Password is to short, it needs to be 12 characters")


def has_passwd_special_characters(passwd):
    for i in range(len(passwd)):
        if not passwd[i].isalnum():
            return False
    raise TypeError("Password missing a special letter")


# def is_passwd_easy_to_guess(passwd):
#     if passwd.startswith("123" or "abcd" or "qwerty") or passwd.endswith("123" or "abcd" or "qwerty"):
#         raise TypeError("Password contains letter combination that is easy to guess")
    
check_if_pass_contains(passwd = passwd)  

#Ønsker å sjekke om den inneholder spesialtegn eller har en annen måte at den har minst 1 av stor og liten bokstav
#Hva kan det være?
# Minst 1 av stor og liten bokstav kan gjøres ved at man sjekker lengden av passordet, iterer over hver character og deretter 
# sjekker om den er lower eller ikke. når vi har gått gjennom hele passordet gir vi en tilbakemelding om det er good eller trenger en lower.
#
#Passord for sjekk: lkjhgfds!@#45 | LKJHGFDS!@#45 | LKJHGFDSTEsT45 | LKJHGFDS#$&FTest | Final: LKJHGFDS#$&FTest56
