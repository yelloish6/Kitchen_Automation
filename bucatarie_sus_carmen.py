from build_corpuri_oo import *

mobila = comanda("Carmen Hurdugaciu", 100)

picioare = 100
gen_h = 600
gen_w = 600
gen_d = 300
gap_spate = 50
gap_fata = 50
gen_cant = 0.4
gen_cant_pol = 2
gen_cant_sep = 0.4
gen_gap_front = 2
th_pal = 18

# 500, 150, 1000, 150, 500
ms1 = corp("MS1", gen_h, 500, gen_d, th_pal, gen_cant)
ms1.buildTopBox()
ms1.addPol(1, gen_cant_pol)
ms1.addFront([[100,100]], gen_gap_front, "door")
mobila.append(ms1)

ms2 = corp("MS2", gen_h, 150, gen_d, th_pal, gen_cant)
ms2.buildTopBox()
ms2.addPol(3, gen_cant_pol)
ms2.addFront([[100,100]], gen_gap_front, "door")
mobila.append(ms2)

ms3 = corp("MS3", gen_h, 1000, gen_d, th_pal, gen_cant)
ms3.buildTopBox()
ms3.addPol(1, gen_cant_pol)
ms3.addFront([[100,50],[100,50]], gen_gap_front, "door")
mobila.append(ms3)

ms4 = corp("MS4", gen_h, 150, gen_d, th_pal, gen_cant)
ms4.buildTopBox()
ms4.addPol(3, gen_cant_pol)
ms4.addFront([[100,100]], gen_gap_front, "door")
mobila.append(ms4)

ms5 = corp("MS5", gen_h, 500, gen_d, th_pal, gen_cant)
ms5.buildTopBox()
ms5.addPol(1, gen_cant_pol)
ms5.addFront([[100,100]], gen_gap_front, "door")
mobila.append(ms5)

mobila.print_status()
mobila.export_csv()
mobila.draw(0, 0, 0)