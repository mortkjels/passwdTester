from flask import Flask, request, render_template, jsonify, redirect, url_for

not_allowed = ["123", "qwerty", "abc", "ABC", "QWERTY", "321", "1234567890@aB"]

score = 0

failure = []

def check_if_pass_contains(passwd, score = score):
    score = is_passwd_long(passwd, score)
    score = is_passwd_lower(passwd, score)
    score = is_passwd_upper(passwd, score)
    score = has_passwd_numbers(passwd, score)
    score = has_passwd_special_characters(passwd, score)
    score = is_passwd_easy_to_guess(passwd, score)
    print(failure)
    return print(f'Your password suggestion got a score credit of; {score}')

# Funksjoner som utfører ulike kriterier som er nødvendig for optimal passordgenerering. 
def is_passwd_lower(passwd,score):
    if any(char.islower() for char in passwd):
        score += 12
    else:
        feil1 = "Missing lower letters"
        failure.append(feil1)
    return score

def is_passwd_upper(passwd, score):
    if any(char.isupper() for char in passwd):
        score += 13
    else:
        feil2 = "Missing upper letters"
        failure.append(feil2)
    return score

def has_passwd_numbers(passwd, score):
    if any(char.isdigit() for char in passwd):
        score += 15
    else:
        feil3 = "Missing numbers"
        failure.append(feil3)
    return score
def is_passwd_long(passwd, score):
    if len(passwd) > 12:
        score += 30
    else:
        feil4 = "Password to short"
        failure.append(feil4)
    return score

def has_passwd_special_characters(passwd, score):
    if any(not char.isalnum() for char in passwd):
        score += 15
    else:
        feil5 = "Missing special letters"
        failure.append(feil5)
    return score 

def is_passwd_easy_to_guess(passwd, score):
    if passwd in not_allowed:
        feil6 = "Combination is too easy"
        failure.append(feil6)
    else:
        score += 14
    return score

#Server initialiseringen. 
app = Flask(__name__)

@app.route('/') #Ruten til hjemmesiden
def home():
    return render_template('Homepage.html')

@app.route('/check_password', methods = ['POST'])
def password_check(): #funksjonen for passordsjekk, henter passordet, kjører det gjennom sjekkene. 
    data = request.get_json()
    pwdcheck = data.get('password')
    check_if_pass_contains(pwdcheck)
    return pwdcheck #ikke slik jeg skal håndtere response. Skal være i et json format, ikke bare retunere strengen


if __name__ == '__main__':
    app.run(port=8250, debug=True) #porten serveren skal gjøre på. 