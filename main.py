import json
import os
import pwinput
import csv
from prettytable import PrettyTable

def clears():
    input("\nKlik Enter untuk kembali ke menu...")
    os.system("cls" if os.name == "nt" else "clear")
    
def readjson(jsfile):
    with open (jsfile, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def readcsv(csvfile):
    with open (csvfile) as cf:
        cdata = csv.reader(cf, delimiter=",")
    return cdata