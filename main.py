import requests
import json


print(" _______         __           __   _______ __               ")
print("|   _   |.--.--.|  |--.--.--.|  |_|   _   |  |--.---.-.----.")
print("|       ||  |  ||    <|  |  ||   _|       |    <|  _  |   _|")
print("|___|___||___  ||__|__|_____||____|___|___|__|__|___._|__| ")
print("         |_____|                                           ")

binn = input("Bini Giriniz : ")

r = requests.get("https://lookup.binlist.net/" + binn)
cikis = json.loads(r.text)

kart = cikis["scheme"]
kartturu = cikis["type"]
kartulke = cikis["country"]["name"]
kartbanka = cikis["bank"]["name"]

veri = {
    "Kart Şeması":kart,
    "Kart Türü":kartturu,
    "Kartın Ülkesi":kartulke,
    "Kartın Bankası":kartbanka

}

print(veri)

