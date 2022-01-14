# documentatie
# documentatie
import csv
import math
from export_stl import *


class placa_pal:
    def __init__(self, label, L, l, w_pal, cant_L1, cant_L2, cant_l1, cant_l2):
        self.label = label
        self.length = L
        self.width = l
        self.thick = w_pal
        self.cant = [cant_L1, cant_L2, cant_l1, cant_l2]
        self.obs = ""
        self.position = [self.label, self.length, self.width, self.thick, 0, 0, 0]  # pozitia placii in corp

        length_cant04 = 0
        length_cant2 = 0
        for i in range(2):
            if self.cant[i] == 0.4:
                length_cant04 = length_cant04 + self.length
            if self.cant[i] == 2:
                length_cant2 = length_cant2 + self.length
            if self.cant[i + 2] == 0.4:
                length_cant04 = length_cant04 + self.width
            if self.cant[i + 2] == 2:
                length_cant2 = length_cant2 + self.width
        self.cant_length = [['0.4', length_cant04], ['2', length_cant2]]

    def getPlaca(self):
        return [["pal", self.label, self.length, self.width, self.thick] + self.cant + [self.obs]]

    def getPlacaOO(self):
        return self

    def addObs(self, text):
        self.obs = self.obs + text

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def rotate(self, axis):
        # axis = "x"/"y"/"z"
        initX = self.position[1]
        initY = self.position[2]
        initZ = self.position[3]
        if axis == "x":
            self.position[1] = initX
            self.position[2] = initZ
            self.position[3] = initY
        elif axis == "y":
            self.position[1] = initZ
            self.position[2] = initY
            self.position[3] = initX
        elif axis == "z":
            self.position[1] = initY
            self.position[2] = initX
            self.position[3] = initZ
        else:
            self.position[1] = initX
            self.position[2] = initY
            self.position[3] = initZ

    def move(self, axis, offset):
        if axis == "x":
            self.position[4] = self.position[4] + offset
        if axis == "y":
            self.position[5] = self.position[5] + offset
        if axis == "z":
            self.position[6] = self.position[6] + offset

    def exportCAD(self, file_name, ox, oy, oz):
        exportStl(file_name, self.label, self.length, self.width, self.thick, ox, oy, oz)


class corp:
    def __init__(self, label, height, width, depth, w_pal, w_cant):
        self.label = label
        self.height = height
        self.width = width
        self.depth = depth
        self.pal_width = w_pal
        self.cant_lab = w_cant
        self.cant = round(w_cant)
        self.pal = []
        self.palOO = []
        self.pfl = []
        self.front = []
        self.blat = 0
        self.acc = []
        self.sep_space_h = self.height - (2 * self.pal_width)
        self.sep_space_w = self.width - (2 * self.pal_width)
        self.sep_max_depth = depth - self.cant
        self.sep_prev = ""
        self.arch = []  # matricea de arhitectura care contine elementele corpului orientate si cu offset
        self.position = [0, 0, 0]  # TODO de folosit pozitia corpului
        self.cant_length = [['0.4', 0], ['2', 0]]

    ##############
    # ADD ELEMENTS#
    ##############
    def addPal(self, label, L, l, w_pal, cant_L1, cant_L2, cant_l1, cant_l2):
        placa = placa_pal(label, L, l, w_pal, cant_L1, cant_L2, cant_l1, cant_l2)
        self.pal = self.pal + placa.getPlaca()
        self.palOO.append(placa)
        self.arch.append(placa.__getattribute__("position"))
        self.cant_length[0][1] = self.cant_length[0][1] + placa.cant_length[0][1]
        self.cant_length[1][1] = self.cant_length[1][1] + placa.cant_length[1][1]

    def addPalObject(self, placa):
        self.pal = self.pal + placa.getPlaca()
        self.palOO.append(placa)
        self.arch.append(placa.__getattribute__("position"))
        self.cant_length[0][1] = self.cant_length[0][1] + placa.cant_length[0][1]
        self.cant_length[1][1] = self.cant_length[1][1] + placa.cant_length[1][1]

    def remPal(self, label):
        remLab = self.label + label
        corp = self.pal
        remIndex = []
        for i in range(len(self.pal)):
            if remLab in self.pal[i]:
                remIndex.append(i)
        for i in range(len(remIndex)):
            self.pal.pop(remIndex[i])
            self.palOO.pop(remIndex[i])
            self.arch.pop(remIndex[i])

    # TODO de scazut cantul cand se scoate o placa de pal

    def addLeg(self, leg_width, placa_cant):
        # adauga o placa orizontala in interiorul corpului, de o latime specificata si cant pe lungimi (TRUE/FLASE)
        if placa_cant:
            placa = placa_pal(self.label + ".leg", self.width - (2 * self.pal_width), leg_width, self.pal_width,
                              self.cant_lab, self.cant_lab, "", "")
        else:
            placa = placa_pal(self.label + ".leg", self.width - (2 * self.pal_width), leg_width, self.pal_width, "", "",
                              "", "")
        self.addPalObject(placa)
        self.addAcces("surub", 4)

    def addPFL(self):
        self.pfl = self.pfl + [["pfl", self.label + ".pfl", self.height - 4, self.width - 4]]
        self.addAcces("surub PFL", 2 * round(self.height / 150) + 2 * round(self.width / 150))

    def addBlat(self, m_blat):
        self.blat = self.blat + m_blat

    def addAcces(self, name, buc):
        found = False
        for i in range(len(self.acc)):
            acc_current = self.acc[i]
            if (name == acc_current[2]):
                acc_current[3] = acc_current[3] + buc
                found = True
        if not found:
            self.acc = self.acc + [["accesoriu", self.label, name, buc]]

    def addPol(self, nr, cant):
        # orient = "h" sau "v"
        # cant = grosime cant
        # TODO: adancimea trebe scazuta cu grosimea cantului si inca nu merge corect
        pol_lung = self.width - (2 * self.pal_width)
        pol_lat = (self.depth - 20)
        for i in range(nr):
            pol = placa_pal(self.label + ".pol", pol_lung, pol_lat, self.pal_width, cant, "", "", "")
            pol.move("x", self.pal_width)
            pol.move("z", round(self.height / (nr + 1)) * (i + 1))
            pol.move("y", 20)
            self.addPalObject(pol)

            self.addAcces("bolt polita", 4)
            self.addAcces("surub PFL", 2)

    def addSeparator(self, orient, sep_cant):

        sep_cant_thk = round(sep_cant)
        if (orient == "h"):
            sep_l = self.sep_space_w
            sep_w = self.sep_max_depth
            sep = placa_pal(self.label + ".sep" + ".h", sep_l, sep_w, self.pal_width, sep_cant, "", "", "")
            self.addPalObject(sep)
            # self.addPal(self.label + ".sep" + ".h", sep_l, sep_w, self.pal_width, sep_cant, "", "", "")

            self.sep_space_h = round((self.sep_space_h - self.pal_width) / 2)
            if self.sep_prev == "v" or "":
                self.sep_max_depth = self.sep_max_depth - sep_cant_thk
                self.sep_prev = "h"
            self.addAcces("surub", 4)
            sep.move("x", self.pal_width)
            sep.move("z", round(self.sep_space_h))
        if orient == "v":
            sep_l = self.sep_space_h
            sep_w = self.sep_max_depth
            sep = placa_pal(self.label + ".sep" + ".v", sep_l, sep_w, self.pal_width, sep_cant, "", "", "")
            self.addPalObject(sep)

            self.sep_space_w = round((self.sep_space_w - self.pal_width) / 2)
            # self.addPal(self.label + ".sep" + ".v", sep_l, sep_w, self.pal_width, sep_cant, "", "", "")
            if self.sep_prev == "h" or "":
                self.sep_max_depth = self.sep_max_depth - sep_cant_thk
                self.sep_prev = "v"

            sep.rotate("y")
            sep.move("x", self.pal_width + round(self.sep_space_w))
            self.addAcces("surub", 4)

    def addWineShelf(self, goluri, left_right, cant):
        offset_z = round((self.height - ((goluri + 1) * self.pal_width)) / goluri)
        if left_right == "left":
            self.addSepV(self.height - (2 * self.pal_width), offset_z, 0, cant)
            for x in range(goluri - 1):
                self.addSepH(offset_z, 0, (offset_z * (x + 1)) + (self.pal_width * (x)), cant)
        if left_right == "right":
            self.addSepV(self.height - (2 * self.pal_width), self.width - offset_z - (3 * self.pal_width), 0, cant)
            for x in range(goluri - 1):
                self.addSepH(offset_z, self.width - offset_z - (2 * self.pal_width),
                             (offset_z * (x + 1)) + (self.pal_width * x), cant)
        if offset_z < 90:
            print("ERROR: nu incap sticlele de vin in " + self.label)

    def addSepV(self, height, offset_x, offset_z, sep_cant):
        sep_l = height
        sep_w = self.depth
        sep = placa_pal(self.label + ".sep" + ".v", sep_l, sep_w, self.pal_width, sep_cant, "", "", "")
        self.addPalObject(sep)
        self.sep_space_w = round((self.sep_space_w - self.pal_width) / 2)

        sep.rotate("y")
        sep.move("x", self.pal_width + offset_x)
        sep.move("z", self.pal_width + offset_z)
        self.addAcces("surub", 4)

    def addSepH(self, width, offset_x, offset_z, sep_cant):
        sep_l = width
        sep_w = self.depth
        sep = placa_pal(self.label + ".sep" + ".h", sep_l, sep_w, self.pal_width, sep_cant, "", "", "")
        self.addPalObject(sep)
        self.sep_space_w = round((self.sep_space_w - self.pal_width) / 2)

        sep.move("x", self.pal_width + offset_x)
        sep.move("z", self.pal_width + offset_z)
        self.addAcces("surub", 4)

    def addFront(self, split_list, front_gap, tip):
        # add fronts based on front split list: [[front1_%height,front1_%width][front2_%height,front2_%width]], ex 2 usi 	   verticale [[100,50][100,50]],
        # front_gap = distanta in mm intre usi si de la margine
        # tip de front: "door" "drawer" "cover"
        h_tot = self.height - front_gap
        w_tot = self.width - front_gap
        for i in range(len(split_list)):
            split = split_list[i]
            h = (h_tot * split[0] / 100) - front_gap
            w = (w_tot * split[1] / 100) - front_gap
            self.front = self.front + [["front", self.label + "_" + str(i + 1), h, w]]
            if (tip == "door"):
                if ((h * w) > 280000):
                    self.addAcces("balama aplicata", 3)
                    self.addAcces("amortizor", 2)
                    self.addAcces("surub 3.5x16", 12)
                else:
                    self.addAcces("balama aplicata", 2)
                    self.addAcces("amortizor", 1)
                    self.addAcces("surub 3.5x16", 8)
                self.addAcces("maner", 1)
            elif (tip == "cover"):
                self.addAcces("surub intre corpuri", math.ceil(h * w / 40000))
            elif (tip == "drawer"):
                self.addAcces("maner", 1)

    def addFrontLateral(self):
        self.front = self.front + [["front", self.label + ".lat", self.height, self.depth]]

    def addFrontManual(self, height, width):
        self.front = self.front + [["front", self.label + ".man", height, width]]

    def addTandemBox(self, tip):
        fund_label = self.label + ".ser.jos"
        spate_label = self.label + ".ser.sp"
        fund_lung = int(self.width - (2 * self.pal_width) - (37.5 * 2))
        spate_lung = self.width - 2 * 18 - 87
        fund_lat = self.depth - 20
        if tip == "M":
            spate_lat = 68
        elif tip == "D":
            spate_lat = 183
        self.addPal(fund_label, fund_lung, fund_lat, 16, "", "", "", "")
        self.addPal(spate_label, spate_lung, spate_lat, 16, self.cant_lab, "", "", "")
        self.addAcces("tandembox " + tip, 1)
        self.addAcces("surub 3.5x16", 18)

    def addSertar(self, sert_h, offset):
        # sertar de tacamuri de 100, sertare adanci de 200

        gap_glisiera = 13
        height_offset = offset
        sert_pal_width = self.pal_width
        sert_lat = self.width - (2 * self.pal_width) - (2 * gap_glisiera)
        sert_depth = self.depth - gap_glisiera

        long1 = placa_pal(self.label + ".ser.long", sert_depth, sert_h, sert_pal_width, self.cant_lab, "", "", "")
        long1.rotate("x")
        long1.rotate("z")
        long1.move("x", self.pal_width + gap_glisiera)
        long1.move("z", height_offset)
        self.addPalObject(long1)

        lat1 = placa_pal(self.label + ".ser.lat", sert_lat - (2 * sert_pal_width), sert_h, sert_pal_width,
                         self.cant_lab, "", "", "")
        lat1.rotate("x")
        lat1.move("x", self.pal_width + sert_pal_width + gap_glisiera + 1)
        lat1.move("z", height_offset)
        self.addPalObject(lat1)

        lat2 = placa_pal(self.label + ".ser.lat", sert_lat - (2 * sert_pal_width), sert_h, sert_pal_width,
                         self.cant_lab, "", "", "")
        lat2.rotate("x")
        lat2.move("x", self.pal_width + sert_pal_width + gap_glisiera + 1)
        lat2.move("y", long1.length - lat2.thick)
        lat2.move("z", height_offset)
        self.addPalObject(lat2)

        long2 = placa_pal(self.label + ".ser.long", sert_depth, sert_h, sert_pal_width, self.cant_lab, "", "", "")
        long2.rotate("x")
        long2.rotate("z")
        long2.move("x", self.pal_width + lat1.thick + gap_glisiera + lat2.length + 2)
        long2.move("z", height_offset)
        self.addPalObject(long2)

        # self.addPal(self.label + ".ser.lat", sert_lat - (2 * self.pal_width), sert_h,self.pal_width, self.cant_lab, "", "", "")
        # self.addPal(self.label + ".ser.lat", sert_lat - (2 * self.pal_width), sert_h,self.pal_width, self.cant_lab, "", "", "")
        # self.addPal(self.label + ".ser.long", sert_depth, sert_h, self.pal_width, self.cant_lab, "", "", "")
        # self.addPal(self.label + ".ser.long", sert_depth, sert_h, self.pal_width, self.cant_lab, "", "", "")
        self.pfl = self.pfl + [["pfl", self.label + ".ser.pfl", sert_lat - 4, sert_depth - 4]]
        self.addAcces("pereche glisiera " + str(self.depth) + " mm", 1)
        self.addAcces("surub 3.5x16", 12)
        self.addAcces("surub", 8)
        self.addAcces("surub PFL", 2 * round(sert_lat / 100) + 2 * round(sert_depth / 100))

    ################
    # BUILD CORPURI#
    ################

    def buildBaseCorner(self, cut_width, cut_depth, l_r, front_thick):
        #    o---------width----------|   o------width-----------
        #    |                        |   |                     |
        #    |     l_r="left"         |   |    l_r="right"      |
        #    |                        |   |                     |
        #    depth                    |   |                     depth
        #    |        ----cut_width----   --- cut_width--       |
        #    |        |                                 |       |
        #    |        cut_depth                  cut_depth      |
        #    |        |                                 |       |
        #    ----------                                 ---------
        # include PFL si fronturi
        jos = placa_pal(self.label + ".jos", self.width, self.depth, self.pal_width, "", "", "", "")
        if l_r == "left":
            jos.addObs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                       str(self.width) + ":" + str(self.depth - cut_depth) + ":" + str(cut_width) + "(cant " + str(
                self.cant_lab) + "):" + str(cut_depth) +
                       "(cant " + str(self.cant_lab) + "):" + str(self.width - cut_width) + ":" + str(self.depth))
        elif l_r == "right":
            jos.addObs(str("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                           str(self.width) + ":" + str(self.depth) + ":" + str(self.width - cut_width) + ":" + str(
                cut_depth) + "(cant " + str(self.cant_lab) + "):" +
                           str(cut_width) + "(cant " + str(self.cant_lab) + "):" + str(self.depth - cut_depth)))
        else:
            print("ERROR: Undefined orientation (only 'left' or 'right' possible!")
        self.addPalObject(jos)
        jos.move("y", -cut_depth)
        lat1 = placa_pal(self.label + ".lat1", self.depth - cut_depth, self.height - self.pal_width, self.pal_width,
                         self.cant_lab, "", "", "")
        self.addPalObject(lat1)
        lat1.rotate("x")
        lat1.move("z", self.pal_width)
        lat1.move("y", -cut_depth)

        lat2 = placa_pal(self.label + ".lat2", self.width - cut_width, self.height - self.pal_width, self.pal_width,
                         self.cant_lab, "", "", "")
        self.addPalObject(lat2)
        lat2.rotate("x")
        lat2.rotate("z")
        lat2.move("z", self.pal_width)
        lat2.move("x", jos.length - self.pal_width)
        lat2.move("y", cut_depth)
        lat2.move("y", -cut_depth)

        spate = placa_pal(self.label + ".spate", self.depth - self.pal_width, self.height - self.pal_width,
                          self.pal_width, "", "", "", "")
        self.addPalObject(spate)
        spate.rotate("x")
        spate.rotate("z")
        spate.move("z", self.pal_width)
        spate.move("y", self.pal_width)
        spate.move("y", -cut_depth)

        leg1 = placa_pal(self.label + ".leg", self.width - (2 * self.pal_width), 100, self.pal_width, self.cant_lab, "",
                         "", "")
        self.addPalObject(leg1)
        leg1.move("z", self.height - self.pal_width)
        leg1.move("x", self.pal_width)
        leg1.move("y", self.depth - leg1.width)
        leg1.move("y", -cut_depth)

        leg2 = placa_pal(self.label + ".leg", self.width - (2 * self.pal_width), 100, self.pal_width, self.cant_lab, "",
                         "", "")
        self.addPalObject(leg2)
        leg2.rotate("x")
        leg2.move("z", self.height - leg2.width)
        leg2.move("y", cut_depth)
        leg2.move("x", self.pal_width)
        leg2.move("y", -cut_depth)

        leg3 = placa_pal(self.label + ".leg", cut_depth - self.pal_width, 100, self.pal_width, self.cant_lab, "", "",
                         "")
        self.addPalObject(leg3)
        leg3.rotate("x")
        leg3.rotate("z")
        leg3.move("z", self.height - leg3.width)
        leg3.move("x", self.width - cut_width - self.pal_width)
        leg3.move("y", self.pal_width)
        leg3.move("y", -cut_depth)

        pol = placa_pal(self.label + ".pol", self.width - (2 * self.pal_width), self.depth - (1 * self.pal_width),
                        self.pal_width, "", "", "", "")
        if l_r == "left":
            pol.addObs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                       str(self.width - (2 * self.pal_width)) + ":" +
                       str(self.depth - cut_depth - 20) + ":" +
                       str(cut_width - self.pal_width + 20) + "(cant " + str(self.cant_lab) + "):" +
                       str(cut_depth - self.pal_width + 20) + "(cant " + str(self.cant_lab) + "):" +
                       str(self.width - cut_width - self.pal_width - 20) + ":" +
                       str(self.depth - self.pal_width))
        elif l_r == "right":
            pol.addObs("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                       str(self.width - (2 * self.pal_width)) + ":" +
                       str(self.depth - self.pal_width) + ":" +
                       str(self.width - cut_width - self.pal_width - 20) + ":" +
                       str(cut_depth - self.pal_width + 20) + "(cant " + str(self.cant_lab) + "):" +
                       str(cut_width - self.pal_width + 20) + "(cant " + str(self.cant_lab) + "):" +
                       str(self.depth - cut_depth - 20) + ":")
        else:
            print("ERROR: Undefined orientation (only 'left' or 'right' possible!")

        self.addPalObject(pol)
        pol.move("x", self.pal_width)
        pol.move("y", self.pal_width)
        pol.move("z", int((self.height - self.pal_width) / 2))
        pol.move("y", -cut_depth)

        self.front = self.front + [["front", self.label + "_1", self.height - 4, cut_depth - 3 - front_thick]]
        self.front = self.front + [["front", self.label + "_2", self.height - 4, cut_width - 3 - front_thick]]

        self.addPFL()

        self.addAcces("balama usa franta", 2)
        self.addAcces("balama 170 deg", 2)
        self.addAcces("surub 3.5x16", 4 * 4)  # pentru balamale
        self.addAcces("picioare", 6)
        self.addAcces("clema plinta", 3)
        self.addAcces("surub 3.5x16", 3 * 4)  # pentru picioare
        self.addAcces("surub blat", 4)
        self.addAcces("L", 2)
        self.addAcces("surub", 19)
        self.addAcces("plinta", (cut_width + cut_depth) / 1000)
        self.addAcces("sipca apa", (self.width + self.depth) / 1000)
        self.addBlat((self.width + self.depth) / 1000)

    def buildTopCorner(self, cut_width, cut_depth, l_r, front_thick):
        #    *******width**************
        #    *                        *
        #    *                        *
        #    *                        *
        #    depth                    *
        #    *        ***cut_width*****
        #    *        *
        #    *        cut_depth
        #    **********

        jos = placa_pal(self.label + ".jos", self.width - self.pal_width, self.depth - self.pal_width, self.pal_width,
                        "", "", "", "")
        if l_r == "left":
            jos.addObs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                       str(self.width - self.pal_width) + ":" +
                       str(self.depth - cut_depth) + ":" +
                       str(cut_width - self.pal_width) + "(cant " + str(self.cant_lab) + "):" +
                       str(cut_depth - self.pal_width) + "(cant " + str(self.cant_lab) + "):" +
                       str(self.width - cut_width) + ":" +
                       str(self.depth - self.pal_width))
        elif l_r == "right":
            jos.addObs("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                       str(self.width - self.pal_width) + ":" +
                       str(self.depth - self.pal_width) + ":" +
                       str(self.width - cut_width) + ":" +
                       str(cut_depth - self.pal_width) + "(cant " + str(self.cant_lab) + "):" +
                       str(cut_width - self.pal_width) + "(cant " + str(self.cant_lab) + "):" +
                       str(self.depth - cut_depth) + ":")
        else:
            print("ERROR: Undefined orientation (only 'left' or 'right' possible!")

        self.addPalObject(jos)
        jos.move("y", self.pal_width)
        jos.move("y", -cut_depth)

        sus = placa_pal(self.label + ".sus", self.width - self.pal_width, self.depth - self.pal_width, self.pal_width,
                        "", "", "", "")
        if l_r == "left":
            sus.addObs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                       str(self.width - self.pal_width) + ":" +
                       str(self.depth - cut_depth) + ":" +
                       str(cut_width - self.pal_width) + "(cant " + str(self.cant_lab) + "):" +
                       str(cut_depth - self.pal_width) + "(cant " + str(self.cant_lab) + "):" +
                       str(self.width - cut_width) + ":" +
                       str(self.depth - self.pal_width))
        elif l_r == "right":
            sus.addObs("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                       str(self.width - self.pal_width) + ":" +
                       str(self.depth - self.pal_width) + ":" +
                       str(self.width - cut_width) + ":" +
                       str(cut_depth - self.pal_width) + "(cant " + str(self.cant_lab) + "):" +
                       str(cut_width - self.pal_width) + "(cant " + str(self.cant_lab) + "):" +
                       str(self.depth - cut_depth) + ":")
        else:
            print("ERROR: Undefined orientation (only 'left' or 'right' possible!")

        self.addPalObject(sus)
        sus.move("y", self.pal_width)
        sus.move("z", self.height - self.pal_width)
        sus.move("y", -cut_depth)

        pol = placa_pal(self.label + ".pol", self.width - (2 * self.pal_width), self.depth - (1 * self.pal_width),
                        self.pal_width, "", "", "", "")
        if l_r == "left":
            pol.addObs("decupaj colt stanga. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                       str(self.width - (2 * self.pal_width)) + ":" +
                       str(self.depth - cut_depth - 20) + ":" +
                       str(cut_width - self.pal_width + 20) + "(cant " + str(self.cant_lab) + "):" +
                       str(cut_depth - self.pal_width + 20) + "(cant " + str(self.cant_lab) + "):" +
                       str(self.width - cut_width - self.pal_width - 20) + ":" +
                       str(self.depth - self.pal_width))
        elif l_r == "right":
            pol.addObs("decupaj colt dreapta. Cote in sensul acelor de ceasornic, de la coltul din stanga spate: " +
                       str(self.width - (2 * self.pal_width)) + ":" +
                       str(self.depth - self.pal_width) + ":" +
                       str(self.width - cut_width - self.pal_width - 20) + ":" +
                       str(cut_depth - self.pal_width + 20) + "(cant " + str(self.cant_lab) + "):" +
                       str(cut_width - self.pal_width + 20) + "(cant " + str(self.cant_lab) + "):" +
                       str(self.depth - cut_depth - 20) + ":")
        else:
            print("ERROR: Undefined orientation (only 'left' or 'right' possible!")

        self.addPalObject(pol)
        pol.move("x", self.pal_width)
        pol.move("y", self.pal_width)
        pol.move("z", int((self.height - self.pal_width) / 2))
        pol.move("y", -cut_depth)

        spate = placa_pal(self.label + ".spate", self.height - (2 * self.pal_width), self.depth - self.pal_width,
                          self.pal_width, "", "", "", "")
        self.addPalObject(spate)
        spate.rotate("y")
        spate.move("y", self.pal_width)
        spate.move("z", self.pal_width)
        spate.move("y", -cut_depth)

        lat1 = placa_pal(self.label + ".lat1", self.height, self.width - cut_width, self.pal_width, self.cant_lab, "",
                         self.cant_lab, self.cant_lab)
        self.addPalObject(lat1)
        lat1.rotate("y")
        lat1.rotate("z")
        lat1.move("y", -cut_depth)

        lat2 = placa_pal(self.label + ".lat2", self.height, self.depth - cut_depth, self.pal_width, self.cant_lab, "",
                         self.cant_lab, self.cant_lab)
        self.addPalObject(lat2)
        lat2.rotate("y")
        lat2.move("x", self.width - self.pal_width)
        lat2.move("y", self.depth - lat2.width)
        lat2.move("y", -cut_depth)

        self.front = self.front + [["front", self.label + "_1", self.height - 4, cut_depth - 3 - front_thick]]
        self.front = self.front + [["front", self.label + "_2", self.height - 4, cut_width - 3 - front_thick]]

        self.addPFL()

        self.addAcces("balama usa franta", 2)
        self.addAcces("balama 170 deg", 2)
        self.addAcces("surub 3.5x16", 4 * 4)  # pentru balamale
        self.addAcces("surub", 20)
        self.addAcces("pereche clema prindere perete", 1)
        self.addAcces("sina perete", self.width / 1000)
        self.addAcces("surub diblu perete", round(self.width / 201))

    def buildBaseBox(self):

        picioare = math.ceil(self.width / 400) * 2
        self.addAcces("picioare", picioare)
        self.addAcces("clema plinta", picioare / 2)
        self.addAcces("surub 3.5x16", picioare * 4)  # pentru picioare
        self.addAcces("surub blat", 4)
        self.addAcces("surub", 14)
        # self.addAcces("blat", self.width/1000)
        self.addAcces("plinta", self.width / 1000)
        self.addAcces("sipca apa", self.width / 1000)
        self.addBlat(self.width / 1000)

        # arhitectura
        # jos
        jos = placa_pal(self.label + ".jos", self.width, self.depth, self.pal_width, self.cant_lab, "", self.cant_lab,
                        self.cant_lab)
        self.addPalObject(jos)
        ##self.arch.append([self.pal[2][1],self.pal[2][2],self.pal[2][3],self.pal[2][4],0,0,0])

        # lat rotit pe Y si ridicat pe z cu grosimea lui jos
        lat1 = placa_pal(self.label + ".lat", self.height - self.pal_width, self.depth, self.pal_width, self.cant_lab,
                         "", "", "")
        lat1.rotate("y")
        lat1.move("z", jos.thick)
        self.addPalObject(lat1)
        # self.arch.append([self.pal[0][1],self.pal[0][4],self.pal[0][3],self.pal[0][2],0,0,self.pal[2][4]])

        # lat rotit pe y, translatat pe x cu (jos - grosime), translatat pe z cu grosime jos
        lat2 = placa_pal(self.label + ".lat", self.height - self.pal_width, self.depth, self.pal_width, self.cant_lab,
                         "", "", "")
        lat2.rotate("y")
        lat2.move("x", jos.length - lat2.thick)
        lat2.move("z", jos.thick)
        self.addPalObject(lat2)
        # self.arch.append([self.pal[1][1],self.pal[1][4],self.pal[1][3],self.pal[1][2],self.pal[2][2]-self.pal[1][4],0,self.pal[2][4]])

        # leg translatat pe z cu (lungimea lat + offset lat - grosime leg), si pe x cu grosime lat
        leg1 = placa_pal(self.label + ".leg", self.width - (2 * (self.pal_width + self.cant)), 100, self.pal_width,
                         self.cant_lab, self.cant_lab, "", "")
        leg1.move("z", lat1.length + jos.thick - leg1.thick)
        leg1.move("x", lat1.thick)
        self.addPalObject(leg1)
        # self.arch.append([self.pal[3][1],self.pal[3][2],self.pal[3][3],self.pal[3][4],self.pal[0][4],0,self.pal[0][2]+self.pal[2][4]-self.pal[3][4]])

        # leg translatat pe z cu (lungimea lat + offset lat - grosime leg)
        #               pe y cu (latime lat - latime leg)
        #               pe x cu grosime lat
        leg2 = placa_pal(self.label + ".leg", self.width - (2 * (self.pal_width + self.cant)), 100, self.pal_width,
                         self.cant_lab, self.cant_lab, "", "")
        leg2.move("z", lat1.length + jos.thick - leg1.thick)
        leg2.move("y", lat1.width - leg2.width)
        leg2.move("x", lat1.thick)
        self.addPalObject(leg2)
        # self.arch.append([self.pal[4][1],self.pal[4][2],self.pal[4][3],self.pal[4][4],self.pal[0][4],self.pal[0][3]-self.pal[4][3],self.pal[0][2]+self.pal[2][4]-self.pal[4][4]])

        self.addPFL()

    def buildSinkBox(self):
        self.buildBaseBox()
        leg_width = 100
        legatura = placa_pal(self.label + ".leg", self.width - (2 * self.pal_width), leg_width, self.pal_width,
                             self.cant_lab, "", "", "")
        legatura.move("x", self.pal_width)
        legatura.move("z", self.pal_width)
        legatura.move("y", self.depth)
        legatura.rotate("x")
        self.addPalObject(legatura)

    def buildTopBox(self):

        self.sep_max_depth = self.depth - self.cant
        self.sep_prev = "h"
        self.addAcces("surub", 8)
        self.addAcces("pereche clema prindere perete", 1)
        self.addAcces("sina perete", self.width / 1000)
        self.addAcces("surub diblu perete", round(self.width / 201))

        # arhitectura
        lat1 = placa_pal(self.label + ".lat1", self.height, self.depth, self.pal_width, self.cant_lab, "",
                         self.cant_lab, self.cant_lab)
        lat1.rotate("y")
        self.addPalObject(lat1)
        # self.palOO.append(lat1)
        jos = placa_pal(self.label + ".jos", self.width - (2 * self.pal_width), self.depth - (self.cant),
                        self.pal_width, self.cant_lab, "", "", "")
        jos.move("x", lat1.thick)
        self.addPalObject(jos)
        # self.palOO.append(jos)
        lat2 = placa_pal(self.label + ".lat2", self.height, self.depth, self.pal_width, self.cant_lab, "",
                         self.cant_lab, self.cant_lab)
        lat2.rotate("y")
        lat2.move("x", lat1.thick + jos.length)
        self.addPalObject(lat2)
        # self.palOO.append(lat2)
        sus = placa_pal(self.label + ".sus", self.width - (2 * self.pal_width), self.depth - (self.cant),
                        self.pal_width, self.cant_lab, "", "", "")
        sus.move("z", lat1.length - sus.thick)
        sus.move("x", lat1.thick)
        self.addPalObject(sus)

        self.addPFL()

    def buildJolyBox(self):
        self.buildBaseBox()
        self.addAcces("Joly" + str(self.width) + str(self.depth), 1)
        self.addAcces("surub 3.5x16", 8)  # prentu glisiere
        self.addAcces("surub 3.5x16", 8)  # pentru front
        self.addPFL()

    def buildMsVBox(self):
        # self.addAcces("blat",self.width/1000)
        self.addAcces("sipca apa", self.width / 1000)
        self.addAcces("plinta", self.width / 1000)
        self.addAcces("surub intre corpuri", 10)
        self.addBlat(self.width / 1000)

    def buildTower(self, gap1, gap2, gap3, gap_heat):
        self.depth = self.depth - gap_heat
        jos = placa_pal(self.label + ".jos", self.width, self.depth, self.pal_width, self.cant_lab, "", self.cant_lab,
                        self.cant_lab)
        self.addPalObject(jos)

        lat1 = placa_pal(self.label + ".lat", self.height - self.pal_width, self.depth + gap_heat, self.pal_width,
                         self.cant_lab, self.cant_lab, "", "")
        lat1.rotate("y")
        lat1.move("z", jos.thick)
        self.addPalObject(lat1)

        lat2 = placa_pal(self.label + ".lat", self.height - self.pal_width, self.depth + gap_heat, self.pal_width,
                         self.cant_lab, self.cant_lab, "", "")
        lat2.rotate("y")
        lat2.move("z", jos.thick)
        lat2.move("x", jos.length - lat2.thick)
        self.addPalObject(lat2)

        sus = placa_pal(self.label + ".sus", self.width - (2 * self.pal_width), self.depth - (self.cant),
                        self.pal_width, self.cant_lab, "", "", "")
        sus.move("x", lat1.thick)
        sus.move("z", lat1.length)
        self.addPalObject(sus)

        self.addSepH(self.width - 2 * self.pal_width, 0, gap1, self.cant)
        self.addSepH(self.width - 2 * self.pal_width, 0, gap1 + gap2 + self.pal_width, self.cant)
        self.addSepH(self.width - 2 * self.pal_width, 0, gap1 + gap2 + gap3 + (2 * self.pal_width), self.cant)
        # self.addSeparator("h",self.cant_lab)
        # self.addSeparator("h",self.cant_lab)
        self.addAcces("surub", 8)
        self.addAcces("plinta", self.width / 1000)
        picioare = math.ceil(self.width / 400) * 2
        self.addAcces("picioare", picioare)
        self.addAcces("clema plinta", picioare / 2)
        self.addAcces("surub 3.5x16", picioare * 4)  # pentru picioare

        self.addPFL()

    ############
    ## UTILS ###
    ############

    def getLabel(self):
        print(self.label)

    def printPal(self):
        corp = self.pal
        for i in range(len(corp)):
            print(corp[i])

    def printCorp(self):
        corp = self.pal + self.pfl + self.front + self.acc
        for i in range(len(corp)):
            print(corp[i])

    def printAcc(self):
        acc = self.acc
        for i in range(len(acc)):
            print(acc[i])

    def getPal(self):
        return self.pal

    def getCorp(self):
        return self.pal + self.pfl + self.front + self.acc

    def getPFL(self):
        return self.pfl

    def getFront(self):
        return self.front

    def getAcces(self):
        return self.acc

    ############
    ## EXPORT ##
    ############

    def exportCSV(self, mobila):
        with open('comanda_pal.csv', mode='w') as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(mobila)):
                p = mobila[i].getPal()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])
            for i in range(len(mobila)):
                p = mobila[i].getPFL()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])
            for i in range(len(mobila)):
                p = mobila[i].getFront()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])
            for i in range(len(mobila)):
                p = mobila[i].getAcces()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])

    def drawCorp(self, filename, ox, oy, oz):
        for i in range(len(self.arch)):
            exportStl(filename,
                      self.arch[i][0] + str(i),
                      self.arch[i][1],
                      self.arch[i][2],
                      self.arch[i][3],
                      self.arch[i][4] + ox,
                      self.arch[i][5] + oy,
                      self.arch[i][6] + oz)


class comanda:
    def __init__(self, client, discount):
        self.client = client
        self.corpuri = []
        self.lungime = 0
        self.corp_count = 0
        self.pret_manop = 0
        self.acc = []
        self.m2pal = 0
        self.m2front = 0
        self.frezare = ""
        self.m2pfl = 0
        self.m_blat = 0
        self.m_cant = [0, 0]
        self.price_pal = 1
        self.price_pfl = 1
        self.price_front = 1
        self.price_blat = 1
        self.price_cant = [0, 0]
        self.price_list = []
        self.cost_pal = 0
        self.cost_pfl = 0
        self.cost_front = 0
        self.cost_blat = 0
        self.cost_cant = [0, 0]
        self.cost_acc = 0
        self.discount = discount
        with open('price_list.csv') as price_list_file:
            price_reader = csv.reader(price_list_file, delimiter=',')
            line_count = 0
            for row in price_reader:
                if line_count == 1:
                    self.price_pal = float(row[1])
                elif line_count == 2:
                    self.price_blat = float(row[1])
                elif line_count == 3:
                    self.price_pfl = float(row[1])
                elif line_count == 4:
                    self.price_front = float(row[1])
                elif line_count == 5:
                    self.price_cant[0] = float(row[1])
                elif line_count == 6:
                    self.price_cant[1] = float(row[1])
                else:
                    self.price_list.append([row[0], row[1]])
                line_count += 1

        # self.price_pal = price_list_file[1][1]
        # self.price_blat = price_list_file[2][1]
        # self.price_pfl = price_list_file[3][1]
        # self.price_front = price_list_file[4][1]

    def append(self, corp):
        self.corpuri.append(corp)
        self.lungime = self.lungime + corp.width
        self.corp_count = self.corp_count + 1
        for j in range(len(corp.acc)):
            self.addAcces(corp.acc[j][2], corp.acc[j][3])
        self.addAcces("surub intre corpuri", 2)
        for j in range(len(corp.pal)):
            self.m2pal = self.m2pal + ((corp.pal[j][2] * corp.pal[j][3]) / 1000000)
        for j in range(len(corp.pfl)):
            self.m2pfl = self.m2pfl + ((corp.pfl[j][2] * corp.pfl[j][3]) / 1000000)
        for j in range(len(corp.front)):
            self.m2front = self.m2front + ((corp.front[j][2] * corp.front[j][3]) / 1000000)
        self.m_blat = self.m_blat + corp.blat
        self.m_cant[0] = self.m_cant[0] + corp.cant_length[0][1] / 1000
        self.m_cant[1] = self.m_cant[1] + corp.cant_length[1][1] / 1000

    def addAcces(self, name, buc):
        found = False
        for i in range(len(self.acc)):
            acc_current = self.acc[i]
            if (name == acc_current[2]):
                acc_current[3] = acc_current[3] + buc
                found = True
        if not found:
            self.acc = self.acc + [["accesoriu", "total", name, buc]]

    def print_status(self):

        print("*** INFORMATII GENERALE ***")
        print("Numar de corpuri: ", self.corp_count)
        print("M2 PAL: ", self.m2pal)
        print("Nr. coli PAL: ", math.ceil(self.m2pal / (2800 * 2070 / 1000000)))
        print("M2 PFL: ", self.m2pfl)
        print("Nr. coli PFL: ", math.ceil(self.m2pfl / (2800 * 2070 / 1000000)))
        print("M2 Front: ", self.m2front)
        print("M Blat: ", math.ceil(self.m_blat))
        print("M Cant 0.4", self.m_cant[0])
        print("M Cant 2", self.m_cant[1])
        print("Lungime totala: ", self.lungime / 1000, " m")

        print("*** COSTURI ***")
        # ACCESORII
        for i in range(len(self.acc)):
            acc_to_find = self.acc[i][2]
            index_of_acc = -1
            for row in self.price_list:
                if acc_to_find in row:
                    index_of_acc = self.price_list.index(row)
            self.cost_acc = self.cost_acc + (float(self.price_list[index_of_acc][1]) * float(self.acc[i][3]))
            print("Cost", acc_to_find, ":", round(float(self.price_list[index_of_acc][1]) * float(self.acc[i][3]), 2),
                  "| Pret: ", round(float(self.price_list[index_of_acc][1]), 2), "| Bucati: ",
                  round(float(self.acc[i][3]), 2))
        print("Cost total accesorii: ", round(self.cost_acc))
        # MANOPERA
        discount = self.discount
        h_rate = 100
        self.pret_manop = math.ceil((8 + (self.corp_count * 2) + 4 + self.m_blat * 0.5)) * h_rate
        # 8h proictare
        # 2h per corp asamblare, pozitionare si montaj fronturi
        # 4h montaj electrocasnice
        # 0.5h pe metru de blat, montaj blat
        self.cost_pal = math.ceil(self.m2pal / 5.3) * self.price_pal #5,3 e suprafata aprox ce poate fi utilizata dint-o placa de pal
        self.cost_pfl = math.ceil(self.m2pfl / 5.3) * self.price_pfl #5,3 e suprafata aprox ce poate fi utilizata dint-o placa de pal
        self.cost_front = math.ceil(self.m2front) * self.price_front
        self.cost_blat = math.ceil(self.m_blat) * self.price_blat
        self.cost_cant[0] = math.ceil(self.m_cant[0]) * self.price_cant[0]
        self.cost_cant[1] = math.ceil(self.m_cant[1]) * self.price_cant[1]

        print("Cost manopera:", self.pret_manop, "| Discount[%]:", discount)
        print("Cost Pal: ", self.cost_pal, "| Placi:", self.cost_pal / self.price_pal, "| Pret placa:", self.price_pal)
        print("Cost PFL: ", self.cost_pfl, "| Placi:", self.cost_pfl / self.price_pfl, "| Pret placa:", self.price_pfl)
        print("Cost Front: ", self.cost_front, "| m2:", math.ceil(self.m2front), "| Pret: ", self.price_front)
        print("Cost Blat: ", math.ceil(self.cost_blat), "| m:", math.ceil(self.m_blat), "| Pret: ", self.price_blat)
        print("Cost cant: ", self.cost_cant, "| lungime:", self.m_cant, "| Pret: ", self.price_cant)
        print("Cost TOTAL: ", round(self.cost_acc + (self.pret_manop * (
                    100 - discount) / 100) + self.cost_pal + self.cost_pfl + self.cost_front + self.cost_blat +
                                    self.cost_cant[0] + self.cost_cant[1]))

    def setPrice(self, item, price):
        if (item == "pal"):
            self.price_pal = price
        elif (item == "pfl"):
            self.price_pfl = price
        elif (item == "front"):
            self.price_front = price
        else:
            self.priceList.append(item, price)

    def export_csv(self):
        name = "comanda_pal_" + self.client + ".csv"
        mobila = self.corpuri
        with open(name, mode='w') as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["tip", "eticheta", "lungime", "latime", "grosime", "L1", "L2", "l1", "l2"])
            for i in range(len(mobila)):
                p = mobila[i].getPal()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])
        name = "comanda_pfl_" + self.client + ".csv"
        mobila = self.corpuri
        with open(name, mode='w') as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["tip", "eticheta", "lungime", "latime"])
            for i in range(len(mobila)):
                p = mobila[i].getPFL()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])
        name = "comanda_front_" + self.client + ".csv"
        mobila = self.corpuri
        with open(name, mode='w') as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["tip", "eticheta", "lungime", "latime"])
            comanda_writer.writerow([self.__getattribute__("frezare")])
            for i in range(len(mobila)):
                p = mobila[i].getFront()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])

        name = "comanda_accesorii_" + self.client + ".csv"
        mobila = self.corpuri
        with open(name, mode='w') as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["tip", "eticheta", "lungime", "latime", "grosime", "L1", "L2", "l1", "l2"])
            # pe corpuri
            for i in range(len(mobila)):
                p = mobila[i].getAcces()
                for j in range(len(p)):
                    comanda_writer.writerow(p[j])
            # total
            for i in range(len(self.acc)):
                comanda_writer.writerow(self.acc[i])

        Opticut_Limit = 50
        name = "PannelsCuttingList_pal_" + self.client + ".csv"
        mobila = self.corpuri
        with open(name, mode='w') as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # comanda_writer.writerow(["N",self.client])
            # comanda_writer.writerow(["M", "PAL ALB 18"])
            # comanda_writer.writerow(["@", "Length", "Width", "Quantity"])
            # comanda_writer.writerow(["S", 2800, 2070, ""])
            # comanda_writer.writerow(["K", 2])
            # comanda_writer.writerow(["@", "Length", "Width", "Quantity","Label","Can turn"])
            comanda_writer.writerow(["Length", "Width", "Qty","Enabled"])
            # pe corpuri
            for i in range(len(mobila)):
                p = mobila[i].getPal()
                for j in range(len(p)):
                    placa = p[j]
                    length = placa[2]
                    width = placa[3]
                    label = placa[1]
                    comanda_writer.writerow([length, width, 1, "TRUE"])
                    # comanda_writer.writerow([length, width, "1", "", "", "", "-1", "", "", "", "", "", "", ""])
                    # comanda_writer.writerow(["P", length, width, 1, label, "y"])




    def draw(self, ox, oy, oz):
        ofset = 0
        for i in range(len(self.corpuri)):
            self.corpuri[i].drawCorp(self.client, ox + ofset, oy, oz)
            ofset = ofset + self.corpuri[i].width + 1