
nume_client = "Mirona Urs"
discount_manopera = 100

# definitii bucatarie
#	2490 inaltime totala pana in tavan
#	faianta tavan 700?
#	faianta de jos 1650

h_bucatarie = 2240  # inaltimea maxima a mobilei, lasata cu 10mm mai jos sa avem overlap cu faianta
h_faianta_top = 1650
h_faianta_base = 850
d_base = 600  # adancime blat jos
h_MsV_min = 850 #TODO de verificat daca incape MsV sub blat
h_MsV_max = 870

# definitii mobila

#Grosimi
th_pal = 18
th_front = 18
blat = 38

frezare_fronturi = "Gri Deschis Ultramat A71/P"
materail_pal = "W908ST2 - pal alb perlat"

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

corpuri = [
    # 0:buildBaseCorner: 1:eticheta, 2:inaltime, 3:latime, 4:adancime, 5:tip cant, 6:orientare_colt
    ["buildBaseCorner", "J1", gen_h_base, 750 - 50, 1088 - 50, gen_cant, "left"],

    # 0:buildBaseBox: 1:eticheta, 2:inaltime, 3:latime, 4:adancime, 5:tip cant, 6:nr_polite, 7:acoperire_fronturi, 8:tip_front, 9:sertare
    ["buildBaseBox", "J2", gen_h_base, gen_w, gen_d_base, gen_cant, 1, [[100,100]], "door", []],
    ["buildBaseBox", "J3", gen_h_base, 450,   gen_d_base, gen_cant, 1, [[100,100]], "door", []],
    ["buildBaseBox", "J4", gen_h_base, gen_w, gen_d_base, gen_cant, 0, [[20, 100], [40, 100], [40, 100]], "drawer", ["M","D","D"]],
    ["buildSinkBox", "J5", gen_h_base, 1000,  gen_d_base, gen_cant, 0, [[100,50],[100,50]], "door", []],
    ["buildMsVBox",  "J6", gen_h_base, gen_w, gen_d_base, gen_cant],
    ["buildBaseBox", "J7", gen_h_base, 300,   gen_d_base, gen_cant, 0, [[100,100]], "door", "joly"],

    # 0:buildTowerBox: 1:eticheta, 2:inaltime, 3:latime, 4:adancime, 5:tip cant, 6:nr_polite, 7:[gap1, gap2, gap3, gap_heat], 8:[front/gap] 9:sertare
    ["buildTower", "T1", gen_h_tower, 600, gen_d_tower, gen_cant, 1, [gen_h_base - 2 * th_pal, 590, 380, 40], [1, 0, 0, 1], []],

    # 0:buildTopBox: 1:eticheta, 2:inaltime, 3:latime, 4:adancime, 5:tip cant, 6:nr_polite, 7:acoperire_fronturi, 8:tip_front
    ["buildTopBox", "S1", gen_h_top, 585, gen_d_top, gen_cant, 1, [[100, 100]], "door", []],

    # 0:buildTopCorner: 1:eticheta, 2:inaltime, 3:latime, 4:adancime, 5:tip cant, 6:orientare_colt
    ["buildTopCorner", "S2", gen_h_top, 750, 488, gen_cant, "left"],

    # 0:buildTopBox: 1:eticheta, 2:inaltime, 3:latime, 4:adancime, 5:tip cant, 6:nr_polite, 7:acoperire_fronturi, 8:tip_front
    ["buildTopBox", "S3", gen_h_top - 40, gen_w, gen_d_top, gen_cant, 0, [[100, 50], [100, 50]], "door"],
    ["buildTopBox", "S4", gen_h_top, 450, gen_d_top, gen_cant, 1, [[100, 100]], "door"],
    ["buildTopBox", "S5", gen_h_top, gen_w, gen_d_top, gen_cant, 1, [[100, 50], [100, 50]], "door"],
    ["buildTopBox", "S6", round(gen_h_top / 2), 1000,   gen_d_top, gen_cant, 0, [[100, 100]], "door"],
    ["buildTopBox", "S7", gen_h_top, gen_w,  gen_d_top, gen_cant, 1, [[100, 50], [100, 50]], "door"],
    ["buildTopBox", "S8", gen_h_top, 300,  gen_d_top, gen_cant, 1, [[100, 100]], "door"],

    # 0:buildBaseBox: 1:eticheta, 2:inaltime, 3:latime, 4:adancime, 5:tip cant, 6:nr_polite, 7:fronturi, 8:tip_front, 9:sertare
    ["buildBaseBox", "I1", gen_h_base,  450, 400, gen_cant, 1, [[100,100]], "door", []],
    ["buildSinkBox", "I2", gen_h_base, 1000, 400, gen_cant, 1, [[100,50],[100,50]], "door", []],
    ["buildBaseBox", "I3", gen_h_base,  450, 400, gen_cant, 1, [[100,100]], "door", []],
    ["buildBaseBox", "I4", gen_h_base,  450, 400, gen_cant, 0, [[100,66]], "door", "wine", [5, "left"]],
    ["buildBaseBox", "I5", gen_h_base, 1000, 400, gen_cant, 1, [[100,50],[100,50]], "door", []],
    ["buildBaseBox", "I6", gen_h_base,  450, 400, gen_cant, 0, [[100,66]], "door", "wine", [5, "left"]]

]


#i1.addFrontManual(gen_h_base, 800 + 18)
#i3.addFrontManual(gen_h_base, 800 + 18)
