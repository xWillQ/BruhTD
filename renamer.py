import os

assets_archer = "Assets/Towers/Archer/"
assets_magic = "Assets/Tower/Magic/"
assets_support = "Assets/Tower/Support/"

support_mobs = assets_support + "support_mobs/"
types = os.listdir(support_mobs)
for t in types:
    assets = os.listdir(support_mobs + "/" + t + "/")
    for asset in assets:
        count = 0
        old = support_mobs + t + "/" + asset
        new = support_mobs + t + "/"
        for i in range(0, len(asset)):
            if (asset[i] == "_"):
                count += 1
            if (count == 3):
                new += asset[i + 1:len(asset)]
                break
        if (new != support_mobs + t + "/"):
            print(old, "->", new)
            os.rename(old, new)

# archer tower assets
os.rename(assets_archer + "1.png", assets_archer + "lvl1_forest_top.png")
os.rename(assets_archer + "2.png", assets_archer + "lvl1_forest_tower.png")
os.rename(assets_archer + "3.png", assets_archer + "lvl2_forest_top.png")
os.rename(assets_archer + "4.png", assets_archer + "lvl2_forest_tower.png")
os.rename(assets_archer + "5.png", assets_archer + "lvl3_forest_top.png")
os.rename(assets_archer + "6.png", assets_archer + "lvl3_forest_tower.png")
os.rename(assets_archer + "7.png", assets_archer + "lvl1_desert_tower.png")
os.rename(assets_archer + "8.png", assets_archer + "lvl2_desert_tower.png")
os.rename(assets_archer + "9.png", assets_archer + "lvl3_desert_tower.png")
os.rename(assets_archer + "10.png", assets_archer + "lvl1_other_tower.png")
os.rename(assets_archer + "11.png", assets_archer + "lvl2_other_tower.png")
os.rename(assets_archer + "12.png", assets_archer + "lvl3_other_tower.png")

# magic tower assets
os.rename(assets_magic + "1.png", assets_magic + "desert_tower_top.png")
os.rename(assets_magic + "2.png", assets_magic + "lvl1_desert_tower.png")
os.rename(assets_magic + "3.png", assets_magic + "lvl2_desert_tower.png")
os.rename(assets_magic + "4.png", assets_magic + "lvl3_desert_tower.png")
os.rename(assets_magic + "5.png", assets_magic + "forest_tower_top.png")
os.rename(assets_magic + "6.png", assets_magic + "lvl1_forest_tower.png")
os.rename(assets_magic + "7.png", assets_magic + "lvl2_forest_tower.png")
os.rename(assets_magic + "8.png", assets_magic + "lvl3_forest_tower.png")
os.rename(assets_magic + "9.png", assets_magic + "other_tower_top_lvl1.png")
os.rename(assets_magic + "10.png", assets_magic + "other_tower_top_lvl2-3.png")
os.rename(assets_magic + "11.png", assets_magic + "lvl1_other_tower.png")
os.rename(assets_magic + "12.png", assets_magic + "lvl2_other_tower.png")
os.rename(assets_magic + "13.png", assets_magic + "lvl3_other_tower.png")

# support tower assets
os.rename(assets_support + "1.png", assets_support + "lvl1_forest_support.png")
os.rename(assets_support + "2.png", assets_support + "lvl2_forest_support.png")
os.rename(assets_support + "3.png", assets_support + "lvl3_forest_support.png")
os.rename(assets_support + "4.png", assets_support + "lvl1_desert_support.png")
os.rename(assets_support + "5.png", assets_support + "lvl2_desert_support.png")
os.rename(assets_support + "6.png", assets_support + "lvl3_desert_support.png")
os.rename(assets_support + "7.png", assets_support + "lvl1_other_support.png")
os.rename(assets_support + "8.png", assets_support + "lvl2_other_support.png")
os.rename(assets_support + "9.png", assets_support + "lvl3_other_support.png")
os.rename(assets_support + "10.png", assets_support + "lvl4_forest_support.png")
os.rename(assets_support + "11.png", assets_support + "lvl4_desert_support.png")
os.rename(assets_support + "12.png", assets_support + "lvl4_other_support.png")

# magic tower attack
os.rename(assets_magic + "19.png", assets_magic + "desert_strike_1.png")
os.rename(assets_magic + "20.png", assets_magic + "desert_strike_2.png")

os.rename(assets_magic + "21.png", assets_magic + "forest_strike_1.png")
os.rename(assets_magic + "22.png", assets_magic + "forest_strike_2.png")

os.rename(assets_magic + "23.png", assets_magic + "other_strike_1.png")
os.rename(assets_magic + "24.png", assets_magic + "other_strike_2.png")

# gui assets
os.rename(assets_archer + "32.png", assets_archer + "lvl1_archer_icon.png")
os.rename(assets_archer + "33.png", assets_archer + "lvl2_archer_icon.png")
os.rename(assets_archer + "34.png", assets_archer + "lvl3_archer_icon.png")

os.rename(assets_magic + "27.png", assets_magic + "lvl1_magic_icon.png")
os.rename(assets_magic + "28.png", assets_magic + "lvl2_magic_icon.png")
os.rename(assets_magic + "29.png", assets_magic + "lvl3_magic_icon.png")

os.rename(assets_support + "13.png", assets_support + "lvl1_support_icon.png")
os.rename(assets_support + "14.png", assets_support + "lvl2_support_icon.png")
os.rename(assets_support + "15.png", assets_support + "lvl3_support_icon.png")
os.rename(assets_support + "16.png", assets_support + "lvl4_support_icon.png")

os.rename(assets_archer + "36.png", assets_archer + "build_gui.png")

# archers assets desert
os.rename(assets_archer + "37.png", assets_archer + "desert_archer_0.png")
os.rename(assets_archer + "38.png", assets_archer + "desert_archer_1.png")
os.rename(assets_archer + "39.png", assets_archer + "desert_archer_2.png")
os.rename(assets_archer + "40.png", assets_archer + "desert_archer_3.png")
os.rename(assets_archer + "41.png", assets_archer + "desert_archer_4.png")
os.rename(assets_archer + "42.png", assets_archer + "desert_archer_5.png")

# archers assets other
os.rename(assets_archer + "43.png", assets_archer + "other_archer_0.png")
os.rename(assets_archer + "44.png", assets_archer + "other_archer_1.png")
os.rename(assets_archer + "45.png", assets_archer + "other_archer_2.png")
os.rename(assets_archer + "46.png", assets_archer + "other_archer_3.png")
os.rename(assets_archer + "47.png", assets_archer + "other_archer_4.png")
os.rename(assets_archer + "48.png", assets_archer + "other_archer_5.png")

# archers assets forest
os.rename(assets_archer + "49.png", assets_archer + "forest_archer_0.png")
os.rename(assets_archer + "50.png", assets_archer + "forest_archer_1.png")
os.rename(assets_archer + "51.png", assets_archer + "forest_archer_2.png")
os.rename(assets_archer + "52.png", assets_archer + "forest_archer_3.png")
os.rename(assets_archer + "53.png", assets_archer + "forest_archer_4.png")
os.rename(assets_archer + "54.png", assets_archer + "forest_archer_5.png")
