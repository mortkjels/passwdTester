# passwd = input ("Write an example for a password, not one your about to use, to check it's robustness: ")

from flask import Flask, request, render_template, jsonify, redirect, url_for

not_allowed = ["123", "qwerty", "abc", "ABC", "QWERTY", "321", "1234567890@aB"]

score = 0

def check_if_pass_contains(passwd, score = score):
    score = is_passwd_long(passwd, score)
    score = is_passwd_lower(passwd, score)
    score = is_passwd_upper(passwd, score)
    score = has_passwd_numbers(passwd, score)
    score = has_passwd_special_characters(passwd, score)
    score = is_passwd_easy_to_guess(passwd, score)
    return print(f'Your password suggestion got a score credit of; {score}')

def is_passwd_lower(passwd,score):
    for i in range(len(passwd)):
        if passwd[i].islower():
            score += 12
            return score
    raise ValueError("Password missing lowercase letter")

def is_passwd_upper(passwd, score):
    for i in range(len(passwd)):
        if passwd[i].isupper():
            score += 13
            return score
    raise ValueError("Password missing uppercase letter")

def has_passwd_numbers(passwd, score):
    for i in range(len(passwd)):
        if passwd[i].isnumeric():
            score += 15
            return score
    raise ValueError("Password missing a numeric letter")

def is_passwd_long(passwd, score):
    if len(passwd) > 12:
        score += 30
        return score
    else: 
        raise ValueError("Password is to short, it needs to be 12 characters")

def has_passwd_special_characters(passwd, score):
    for i in range(len(passwd)):
        if not passwd[i].isalnum():
            score += 15
            return score
    raise ValueError("Password missing a special letter")

def is_passwd_easy_to_guess(passwd, score):
    for elem in not_allowed:
        if elem in passwd:
            raise ValueError("Password contains a sequence that is easy to guess")
        else: 
            score += 15
            return score
        
check_if_pass_contains(passwd = passwd, score = score)  

