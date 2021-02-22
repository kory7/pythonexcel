import pylightxl as xl

db = xl.readxl(fn='coches.xlsx')
print(db.ws_names)
