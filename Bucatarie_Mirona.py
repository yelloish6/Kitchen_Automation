from build_corpuri_oo import *

# definitii bucatarie
#	2490 inaltime totala pana in tavan
#	faianta tavan 700?
#	faianta de jos 1650

h_bucatarie = 2240  # inaltimea maxima a mobilei, lasata cu 10mm mai jos sa avem overlap cu faianta
h_faianta_top = 1650
h_faianta_base = 850
d_base = 600  # adancime blat jos

# definitii mobila
blat = 38
picioare = 100
gen_w = 600
gap_spate = 50  # inca nefolosit
gap_fata = 50  # inca nefolosit
gen_cant = 0.4
gen_cant_pol = 2
gen_cant_sep = 0.4
gen_gap_front = 2

# top
gen_h_top = 600
gen_d_top = 300  # 300 plus 4 ca sa incapa intaritura in spatele hotei plus suruburile

# base
gen_h_base = 870 - blat - picioare
gen_d_base = d_base - 50 - 50  # adancime totala, minus 5cm in fata, minus 5cm in spate

# tower
gen_h_tower = h_bucatarie - picioare
gen_d_tower = gen_d_base + 50

mobila = comanda("Mirona Urs", 100)
mobila.__setattr__("frezare", "Gri Deschis Ultramat A71/P")

j1 = corp("J1", gen_h_base, 750 - 50, 1088 - 50, 18, gen_cant)
j1.buildBaseCorner(150 + 50, 490 + 50, "left", 18)
mobila.append(j1)

j2 = corp("J2", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j2.buildBaseBox()
j2.addPol(1, gen_cant_pol)
j2.addFront([[100, 100]], 2, "drawer")
mobila.append(j2)

j3 = corp("J3", gen_h_base, 450, gen_d_base, 18, gen_cant)
j3.buildBaseBox()
j3.addPol(1, 2)
j3.addFront([[100, 100]], 2, "door")
mobila.append(j3)

j4 = corp("J4", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j4.buildBaseBox()
j4.addTandemBox("M")
j4.addTandemBox("D")
j4.addTandemBox("D")
j4.addFront([[20, 100], [40, 100], [40, 100]], 2, "drawer")
mobila.append(j4)

j5 = corp("J5", gen_h_base, 1000, gen_d_base, 18, gen_cant)
j5.buildSinkBox()
j5.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(j5)

j5 = corp("J5", gen_h_base, gen_w, gen_d_base, 18, gen_cant)
j5.buildMsVBox()
mobila.append(j5)

j6 = corp("j6", gen_h_base, 300, gen_d_base, 18, gen_cant)
j6.buildJolyBox()
j6.addFront([[100, 100]], 2, "door")
mobila.append(j6)

t1 = corp("T1", gen_h_tower, 600, gen_d_tower, 18, gen_cant)
t1.buildTower(gen_h_base - 2 * t1.pal_width, 590, 380, 40)
# t1.addFront([[100,100]],2,"door")
t1.addPol(1, gen_cant_pol)
t1.addFrontManual(gen_h_base - 4, gen_w - 4)
t1.addFrontManual(gen_h_tower - 4 - (3 * 2) - 390 - 595, gen_w - 4)

mobila.append(t1)

s1 = corp("s1", gen_h_top, 585, gen_d_top, 18, gen_cant)
s1.buildTopBox()
s1.addPol(1, gen_cant_pol)
s1.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(s1)

s2 = corp("s2", gen_h_top, 750, 488, 18, gen_cant)
s2.buildTopCorner(450, 188, "left", 18)
mobila.append(s2)

s3 = corp("s3", gen_h_top - 40, gen_w, gen_d_top, 18, gen_cant)
s3.buildTopBox()
s3.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(s3)

s4 = corp("s4", gen_h_top, 450, gen_d_top, 18, gen_cant)
s4.buildTopBox()
s4.addPol(1, gen_cant_pol)
s4.addFront([[100, 100]], 2, "door")
mobila.append(s4)

s5 = corp("s5", gen_h_top, gen_w, gen_d_top, 18, gen_cant)
s5.buildTopBox()
s5.addPol(1, gen_cant_pol)
s5.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(s5)

s6 = corp("s6", round(gen_h_top / 2), 1000, gen_d_top, 18, gen_cant)
s6.buildTopBox()
s6.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(s6)

s7 = corp("s7", gen_h_top, gen_w, gen_d_top, 18, gen_cant)
s7.buildTopBox()
s7.addPol(1, gen_cant_pol)
s7.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(s7)

s8 = corp("s8", gen_h_top, 300, gen_d_top, 18, gen_cant)
s8.buildTopBox()
s8.addPol(1, gen_cant_pol)
s8.addFront([[100, 100]], 2, "door")
mobila.append(s8)

i1 = corp("I1", gen_h_base, 450, 400, 18, gen_cant)
i1.buildBaseBox()
i1.addPol(1, gen_cant_pol)
i1.addFront([[100, 100]], 2, "door")
i1.addFrontManual(gen_h_base, 800 + 18)
mobila.append(i1)

i2 = corp("I2", gen_h_base, 1000, 400, 18, gen_cant)
i2.buildSinkBox()
i2.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(i2)

i3 = corp("I3", gen_h_base, 450, 400, 18, gen_cant)
i3.buildBaseBox()
i3.addPol(1, gen_cant_pol)
i3.addFront([[100, 100]], 2, "door")
i1.addFrontManual(gen_h_base, 800 + 18)
mobila.append(i3)

i4 = corp("I4", gen_h_base, 450, 400, 18, gen_cant)
i4.buildBaseBox()
i4.addWineShelf(5, "left", gen_cant_sep)
i4.addFront([[100, 66]], 2, "door")
mobila.append(i4)

i5 = corp("I5", gen_h_base, 1000, 400, 18, gen_cant)
i5.buildBaseBox()
i5.addFront([[100, 50], [100, 50]], 2, "door")
mobila.append(i5)

i6 = corp("I6", gen_h_base, 450, 400, 18, gen_cant)
i6.buildBaseBox()
i6.addWineShelf(5, "right", gen_cant_sep)
i6.addFront([[100, 66]], 2, "door")
mobila.append(i6)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)

# verificari
if h_bucatarie - gen_h_top < h_faianta_top:
    print("Verificare inaltime fainata sus: OK", "Suprapunere corp suspendat faianta: ",
          -h_bucatarie + gen_h_top + h_faianta_top, "mm")
else:
    print("Verificare inaltime fainata sus: ERROR", "Distanta corp suspendat faianta: ",
          h_bucatarie - gen_h_top - h_faianta_top, "mm")

if gen_h_base + picioare + blat > h_faianta_base:
    print("Verificare inaltime fainata jos: OK", "Suprapunere blat si faianta jos",
          gen_h_base + picioare + blat - h_faianta_base, "mm")
else:
    print("Verificare inaltime fainata jos: ERROR", "Distanta intre blat si faianta:",
          h_faianta_base - gen_h_base + picioare + blat, "mm")

print("Verificare distanta de la blat la corpurile suspendate (recomandare min. 600): ",
      h_bucatarie - gen_h_top - blat - gen_h_base - picioare, "mm")


