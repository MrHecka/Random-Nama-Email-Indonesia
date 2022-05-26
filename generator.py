import requests as r
from lxml import html
import random, os, clipboard


a = r.get("http://ninjaname.horseridersupply.com/indonesian_name.php")

get = html.fromstring(a.content)

nama = get.xpath('/html/body/div/div[2]/div[2]/div[1]/div[4]/text()')

os.system('cls')

print("========RANDOMIZE NAMA + EMAIL BY HECKAYO========")
print("")


for x in nama:
    ran = random.randint(0, len(nama))
    filter = nama[ran]
    nama = filter[2:len(filter)]
    emailnum = random.randint(0,99)
    namaemail = ''.join(c.lower() for c in nama if not c.isspace())
    print("Nama : " + nama)
    print(f"Email : {namaemail}{emailnum}@gmail.com")
    clipboard.copy(f"{namaemail}{emailnum}@gmail.com")
    print("")
    print("Email Berhasil Di Copy!")
    break






