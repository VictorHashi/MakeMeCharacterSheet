import json
import math

class Character:

    def __init__(self,name="Bly",race="Humano",exp="100",str=10,dex=10,con=10,int=10,wis=10,cha=10,ac=8,move=30,hitdie=6,hitdies=1):
        self.name = name
        self.race = race
        self.exp = exp
        self.str = str
        self.strMod = (math.floor(str/2))-5
        self.dex = dex
        self.dexMod = (math.floor(dex/2))-5
        self.con = con
        self.conMod = (math.floor(con/2))-5
        self.int = int
        self.intMod = (math.floor(int/2))-5
        self.wis = wis
        self.wisMod = (math.floor(wis/2))-5
        self.cha = cha
        self.chaMod = (math.floor(cha/2))-5
        self.ac = 8 + self.dexMod
        self.move = move + (math.floor(abs(dex-10)/5)*5)
        self.hitdie = hitdie
        self.hitdies = hitdies
        self.maxhp = hitdie+(self.conMod)
        self.feats = []

    def save_to_file(self, path):
        with open(path, 'w') as f:
            json.dump(self.__dict__, f, indent=4)

    @staticmethod
    def load_from_file(path):
        with open(path, 'r') as f:
            data = json.load(f)
        return Character(**data)
    
    def canAddFeat(self,feat):
        if (feat.name in self.feats):
            return False
        if (feat.requirement):
            return False
        return True

    def addFeat(self,feat):
        if self.canAddFeat(self,feat):
            self.feats.append(feat.name)