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


# Konsistens i returverdier
# Noen funksjoner returnerer True, noen returnerer False, noen returnerer ingenting og bare kaster feil. Tenk på om dette gir et tydelig og forutsigbart API.

# Navngivning vs faktisk logikk
# Sjekk om funksjonsnavnene matcher nøyaktig det de gjør (f.eks. “has” vs “is”, og hva True/False faktisk betyr).

# Flytkontroll / lesbarhet
# Tenk på om kontrollflyten er lett å følge:
# “hva skjer først, hva kan feile, hva betyr det at vi kommer helt til slutten?”

# Ansvar per funksjon
# Hver funksjon gjør én sjekk – bra.
# Tenk på om noen av dem også implisitt gjør mer enn én ting (f.eks. både sjekker og bestemmer konsekvens).

# Normalisering av input
# Tenk på om passordet bør behandles “som det er”, eller om du mentalt vil sammenligne på en normalisert form (case, whitespace, osv.).

# Dekningsgrad på ‘lett å gjette’
# Tenk på hvor grensen går for hva som er “enkelt å gjette”:
# faste strenger, reverserte strenger, overlapp, deltreff.

# Brukeropplevelse vs sikkerhet
# Tenk på hvor mye informasjon du vil gi tilbake ved feil (én regel av gangen vs samlet).

# Testbarhet
# Tenk på hvor lett det er å skrive tester for hver regel isolert, og for helheten.

# Rekkefølge på sjekker
# Tenk på om rekkefølgen er tilfeldig, logisk, eller bevisst (billige sjekker først, strengere senere).