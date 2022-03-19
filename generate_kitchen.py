from build_corpuri_oo import *
import csv

input_file = 'input_Mirona_3.csv'

rules = {
    'gros_pal': 18,
    'gros_front': 18,
    'gros_blat': 40,
    'cant': 0.4,
    'cant_pol': 2,
    'cant_sep': 0.4,
    'gap_front': 2,
}

with open(input_file, newline='') as csvfile:
    param_comanda = {}
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    index = 100
    plan = []
    for row in reader:
        if row[0] != "comanda":
            param_comanda[row[0]] = row[1]
        else:
            index = reader.line_num
            break
    for row in reader:
        if reader.line_num > index:
            plan.append(row)

print(param_comanda)

mobila = comanda(param_comanda["nume_client"], param_comanda["discount manopera"])

for line in plan:
    if line[0] == "new_corp":
        corp = {
            "label":line[1],
            "h": line[2],
            "w": line[3],
            "d": line[4],
            "w_pal": rules["gros_pal"],
            "cant": rules["cant"]
        }
        print(corp)
        if (line[2] == "") and ((line[5] != "buildTopBox") or (line[5] != "buildTopCorner") or (line[5] != "buildTower")):
            corp['h'] = param_comanda["h_base"]
        #c = corp(line[1],line[2],line[3],line[4],rules["gros_pal"],rules["cant"])
        #mobila.append(c)
