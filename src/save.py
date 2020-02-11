##
## EPITECH PROJECT, 2020
## save
## File description:
## save
##

def save(self, filesav):
    path = "data/saves/" + filesav + ".sav"
    file = open(path, "w", encoding='utf-8')
    text = "# SYSTEM\n"
    text += "fen=" + str(self.fen) + "\n"
    text += "page=" + str(self.page) + "\n"
    text += "map=map1" + "\n"
    text += "item_count="
    itemlist = []
    for i in self.items:
        itemlist.append(str(i.get_count()))
    if len(itemlist) == 0:
        text += "[]\n"
    else:
        text += ",".join(itemlist) + "\n"
    del itemlist
    text += "# PLAYER\n"
    pos = self.p.get_positions()
    text += "pos=" + str(pos[0]) + "," + str(pos[1]) + "\n"
    del pos
    text += "money=" + str(self.p.get_money()) + "\n"
    text += "player_info=" + "MaxHealth:" + str(self.p.get_player_info("MaxHealth")) + ",Health:" + str(self.p.get_player_info("Health")) + ",Attack:" + str(self.p.get_player_info("Attack")) + ",Defense:" + str(self.p.get_player_info("Defense")) + ",Speed:" + str(self.p.get_player_info("Speed")) + "\n"
    text += "equipment=Weapon:" + str(self.p.get_equipment("Weapon")) + ",Body:" + str(self.p.get_equipment("Body")) + ",Head:" + str(self.p.get_equipment("Head")) + ",Legs:" + str(self.p.get_equipment("Legs")) + ",Feet:" + str(self.p.get_equipment("Feet")) + ",Arm left:" + str(self.p.get_equipment("Arm left")) + ",Arm right:" + str(self.p.get_equipment("Arm right")) + "\n"
    text += "# OPTIONS\n"
    text += "keys=Up:" + str(self.option.get_key("Up")) + ",Down:" + str(self.option.get_key("Down")) + ",Left:" + str(self.option.get_key("Left")) + ",Right:" + str(self.option.get_key("Right")) + ",Inventory:" + str(self.option.get_key("Inventory")) + ",Menu:" + str(self.option.get_key("Menu")) + ",Action:" + str(self.option.get_key("Action")) + ",Dash:" + str(self.option.get_key("Dash")) + "\n"
    text += "# MONSTERS\n"
    text += "nb=" + str(len(self.mobs))
    if len(self.mobs) > 0:
        for i in range(0, len(self.mobs)):
            mob = self.mobs[i]
            text += "\n---\n"
            pos = mob.get_positions()
            text += "pos=" + str(pos[0]) + "," + str(pos[1]) + "\n"
            del pos
            text += "monster_info=MaxHealth:" + str(mob.get_monster_info("MaxHealth")) + ",Health:" + str(mob.get_monster_info("Health")) + ",Attack:" + str(mob.get_monster_info("Attack")) + ",Defense:" + str(mob.get_monster_info("Defense")) + ",Speed:" + str(mob.get_monster_info("Speed")) + "\n"
            text += "monster_loot=Gold:" + str(mob.get_monster_loot("Gold")) + ",Exp:" + str(mob.get_monster_loot("Exp")) + ",Objects:" + str(mob.get_monster_loot("Objects"))
    file.write(text)
    file.close()

def load(self, filesav):
    path = "data/saves/" + filesav + ".sav"
    file = open(path, "r", encoding='utf-8')
    data = file.read()
    file.close()

    lines_data = data.split("\n")
    del data
    index = -1
    double_data = []
    for i in lines_data:
        if "#" in i:
            double_data.append([])
            index += 1
        else:
            double_data[index].append(i)
    del lines_data
    print(double_data)