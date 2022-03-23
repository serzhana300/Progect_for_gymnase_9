import random
import string

alf_en = [i for i in string.ascii_letters]
alf_num = [str(i) for i in range(9)]


def password_generate():
    passw = ''
    for i in range(8):
        passw += random.choice(alf_en + alf_num)
    return passw


def verif_date(n):
    if len(str(n)) < 2:
        return f'0{n}'
    else:
        return n


def check_edits(l, p):
    if len(l) and len(p):
        return True
    else:
        return False