import json
from openpyxl import Workbook

with open("database.json", "r") as json_file:
    database = json.load(json_file)

with open("wallets.txt", 'r', encoding='utf-8-sig') as file:
    wallets = [line.strip() for line in file]

workbook = Workbook()
sheet = workbook.active
sheet.title = "Транзакции"

sheet['A1'] = 'Кошелек'
sheet['B1'] = 'Количество транзакций'

for index, wallet in enumerate(wallets, start=2):
    transactions_count = database.get(wallet, 0)
    sheet[f'A{index}'] = wallet
    sheet[f'B{index}'] = transactions_count

workbook.save("result.xlsx")
