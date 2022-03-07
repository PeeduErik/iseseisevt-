# Peedu Erik Pajo
# Iseseisevtöö
# 03.03.2022

#emaili tükeldamine ja kontroll
import re

email = input("Sisesta oma email: ").strip()
n = "^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    
if re.search(n, email):
    kasutaja = email[:email.index("@")]
    server = email[email.index("@")+1:email.index(".")]
    domeen = email[email.index("."):]
    print(f"Tere {kasutaja}, sinu email on {server} serveris ja domeeniks on sul {domeen}")
else:
    print(f"Tere, seda emaili ei saa kasutada")
    




