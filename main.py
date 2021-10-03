import requests
import csv

r = requests.get('https://v6.exchangerate-api.com/v6/1fca918a82cf5772aab3ea46/latest/USD')
#print(r.text)
#r = requets.get('https://v6.exchangerate-api.com/v6/1fca918a82cf5772aab3ea46/latest/USD')
c = csv.writer(open("kurs-rates.csv", "w"), lineterminator='\n')

# for item in r['base_code']['conversion_rates'];
# 	c.writerow([item['date']['pretty'], item['tempi']])
# r.json()
