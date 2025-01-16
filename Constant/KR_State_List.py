# -*- coding: utf-8 -*-
'''
@File    : state_list.py
@Time    : 2023/11/11 10:49:01
@Author  : songxinrui
@Version : 1.0
@Blog    :
@Desc    :
Based on `KR_dataset annotation.md`, we define all the state with special ids.
'''
import KR_Unit_List
'''
`K` means the classification dimension for each `class_name`.
| class_name    | K |
|---------------|---|
| belong        | 2 |
| movement      | 4 |
| state         | 2 |
| dig           | 2 |
| rage          | 2 |
'''

'''
# Need predict:
#blong:			0/1	#firend/enermy
#movement:		norm/melee attack/ranged attack/freeze	#正常(角色的行走，防御塔的正常)/近战攻击/远程攻击/冻结(角色，防御塔)
#state:			normal/broken		#正常/(机器人)损坏（可被修复）
#dig:				normal/dig	#正常/挖掘
#rage:				norm/rage	#正常/狂暴

# Constants:
#height:			ground/air	#地面/空中
#object:		tower/character/item	#防御塔/角色/游戏物体
'''

state2idx = {  # key: (class, id)
  '0': (0, 0),  # Class 1: Belong (binary: 1 variable)
  '1': (0, 1),
  'normal': (1, 0),  # Class 2: Movement (mutli classes: 4 variables, default 0)
  'melee attack': (1, 1),
  'ranged attack': (1, 2),
  'freeze':   (1, 3),
  'normal_State': (2, 0),  # Class 3: State (binary: 2 variable, default 0)
  'broken': (2, 1),
  'normal_Dig': (3, 0),  # Class 4: Dig (binary: 2 variable)
  'Dig':  (3, 1),
  'normal_Rage':  (4, 0),   # Class 5: Rage (binary: 1 variable)
  'Rage':  (4, 1)
}
# num_state_classes =  4 + 2 * 4  # 12
id2state = {v: k for k, v in state2idx.items()}

unit2height = {  # key: unit_name, value: height
# (6, ground/air)
"Human Woodcutter" : 0, #人类伐木工
    "Human Worker" : 0, #人类工人
    "Dwarf Bruiser" : 0,  #矮人布鲁塞尔
    "Warhammer Guard" : 0, #战锤守卫
    "Clockwork Spider" : 0, #发条蜘蛛
    "Chomp Bot" : 0,  #糖果机器人
    "Cyclopter" : 1, #牢大直升机
    "Tinbeard Gunman" : 0,  #锡须枪手
    "Smokebeard Engineer" : 0,  #烟须工程师
    "Sulfur Alchemist" : 0,  #硫磺炼金术师
    "Quarry Worker" : 0,  #矿工
    "Stonebeard Geomancer"  : 0,  #石头矮人风水师
    "MechaDwarf MK.9" : 0,  #机械矮人MK.9
    "Northern Wildling" : 0,  #北国野蛮人
    "Northern Huntress" : 0,  #北国女猎人
    "Glacial Wolf" : 0,   #冰原狼
    "Bule Wyvern" : 1,  #蓝色飞龙
    "Northern Berserker" : 0,  #北国狂战士
    "Nanoq Warbear" : 0,  #北国战熊
    "Apex Stalker" : 0,  #顶级掠食者
    "Apex Shard" : 0,  #顶级掠食者碎片
    "Ice Witch" : 0,  #寒冰女巫
    "Leap Dragon"   : 0,  #飞纵龙
    "Valkyrie" : 0,   #女武神
    "Draugr" : 0,  #食尸鬼
    "Svell Druid" : 0,  #斯维尔德鲁伊
    "Frost Giant" : 0,  #冰霜巨人
    "Recruit" : 0,    #新兵
    "Footman" : 0,   #步兵（老兵）
    "Watchdog" : 0,  # 看门狗
    "Troop Captain" : 0,  #军队指挥官
    "Farmer_1" : 0,  #农民1
    "Farmer_2" : 0,  #农民2
    "Farmer_3" : 0,  #农民3
    "Farmer_4" : 0,  #农民4
    "Farmer_5" : 0,  #农民5
    "Hunting Eagle" : 1,  #猎鹰
    "Joe Jenkins" : 0,  #乔·詹金斯
    "Baa San" : 0,  #芭山  （强化绵羊，可以攻击和被阻挡，在后期出现，需要3+级别塔的照顾）
    "Alleria Swiftwind" : 0,  #奥莱利娅-追风
    "Elven Ranger" : 0,  #精灵游侠
    "Devoted Priest" : 0,  #神圣牧师
    "Gryphon Bombardier" : 1,  #狮鹫投弹者
    "Arcane Magus" : 0,  #奥术大师
    "High Sorcerer" : 0,  #高级巫师
    "Sheep" : 0,  #绵羊
    "Paladin" : 0,  #圣骑士
    "Golem House" : 0,  #魔像（这个就是会从场景的房屋变大怪的东西）
    "Shieldbearer" : 0,  #持盾者，必须使用魔法塔或者兵营阻挡加灌伤打法
    "Cavalier" : 0,  #骑士（其实就是骑士进入马厩以后骑上马）
    "Musketeer" : 0,  #火枪手
    "War Wagon" : 0,  #战车
    #add more unit here...
    "Orc Warrior_Level1" : 0,  # 兵营兽人等级1
    "Orc Warrior_Level2" : 0,  # 兵营兽人等级2
    "Orc Warrior_Level3" : 0,  # 兵营兽人等级3
    "Orc Warrior_Level4" : 0,  # 兵营兽人等级4
    "Dark Knight_Level1" : 0,  # 兵营黑暗骑士等级1
    "Dark Knight_Level2" : 0,  # 兵营黑暗骑士等级2
    "Dark Knight_Level3" : 0,  # 兵营黑暗骑士等级3
    "Dark Knight_Level4" : 0,  # 兵营黑暗骑士等级4
    "Guardian Gargoyle" : 0,  # 石像鬼
    "Elite Harasser_Level1" : 0,  # 骚扰者等级1
    "Elite Harasser_Level2" : 0,  # 骚扰者等级2
    "Elite Harasser_Level3" : 0,  # 骚扰者等级3
    "Elite Harasser_Level4" : 0,  # 骚扰者等级4
    "Troll_jinzhan" : 0,  # 巨魔战士近战
    "Troll_ranged" : 0,  # 巨魔战士远程
    "warmongers" : 0, #战争贩子
    "Goonies" : 0, #呆头鹅
    "Veruk" : 0, # 维鲁克
    "Asra" : 0,  # 阿斯拉
    "Oloch": 0,  # 奥罗克
}

is_tower = {
    "Shadow Archers_Level1" : 0,  # 暗影弓手等级1
    "Shadow Archers_Level2" : 0,  # 暗影弓手等级2
    "Shadow Archers_Level3" : 0,  # 暗影弓手等级3
    "Shadow Archers_Level4" : 0,  # 暗影弓手等级4
    "Orc Warriors Den_Level1" : 0,  # 兽人巢穴等级1
    "Orc Warriors Den_Level2" : 0,  # 兽人巢穴等级2
    "Orc Warriors Den_Level3" : 0,  # 兽人巢穴等级3
    "Orc Warriors Den_Level4" : 0,  # 兽人巢穴等级4
    "Infernal Mage_Level1" : 0,  # 恶魔法师等级1
    "Infernal Mage_Level2" : 0,  # 恶魔法师等级2
    "Infernal Mage_Level3" : 0,  # 恶魔法师等级3
    "Infernal Mage_Level4" : 0,  # 恶魔法师等级4
    "Rocket Riders_Level1" : 0,  # 火箭炮塔等级1
    "Rocket Riders_Level2" : 0,  # 火箭炮塔等级2
    "Rocket Riders_Level3" : 0,  # 火箭炮塔等级3
    "Rocket Riders_Level4" : 0,  # 火箭炮塔等级4
    "Dark Knights_Level1" : 0,  # 黑暗骑士等级1
    "Dark Knights_Level2" : 0,  # 黑暗骑士等级2
    "Dark Knights_Level3" : 0,  # 黑暗骑士等级3
    "Dark Knights_Level4" : 0,  # 黑暗骑士等级4
    "Melting Furnace_Level1" : 0,  # 熔炉等级1
    "Melting Furnace_Level2" : 0,  # 熔炉等级2
    "Melting Furnace_Level3" : 0,  # 熔炉等级3
    "Melting Furnace_Level4" : 0,   # 熔炉等级4
    "Specters Mausoleum_Level1" : 0,  # 死灵墓等级1
    "Specters Mausoleum_Level2" : 0,  # 死灵墓等级2
    "Specters Mausoleum_Level3" : 0,  # 死灵墓等级3
    "Specters Mausoleum_Level4" : 0,  # 死灵墓等级4
    "Goblirangs_Level1" : 0,  # 哥布林回旋镖等级1
    "Goblirangs_Level2" : 0,  # 哥布林回旋镖等级2
    "Goblirangs_Level3" : 0,  # 哥布林回旋镖等级3
    "Goblirangs_Level4" : 0,  # 哥布林回旋镖等级4
    "Bone Flingers_Level1" : 0,  # 掷骨者等级1
    "Bone Flingers_Level2" : 0,  # 掷骨者等级2
    "Bone Flingers_Level3" : 0,  # 掷骨者等级3
    "Bone Flingers_Level4" : 0,  # 掷骨者等级4
    "Elite Harassers_Level1" : 0,  # 骚扰者等级1
    "Elite Harassers_Level2" : 0,  # 骚扰者等级2
    "Elite Harassers_Level3" : 0,  # 骚扰者等级3
    "Elite Harassers_Level4" : 0,  # 骚扰者等级4
    "Orc Shaman_Level1" : 0,  # 兽人萨满等级1
    "Orc Shaman_Level2" : 0,  # 兽人萨满等级2
    "Orc Shaman_Level3" : 0,  # 兽人萨满等级3
    "Orc Shaman_Level4" : 0,  # 兽人萨满等级4
    "Troll Mercenaries" : 0,  # 巨魔军团
    #items
    "Tinbeard Gunman_Bullet" : 2,  # 锡须枪手--子弹
    "Sulfur Alchemist_Chemical" : 2,  # 硫磺炼金术师--化学药剂
    "Northern Huntress_Axe" : 2,  # 北国女猎手-斧
    "Svell Druid_Ice" : 2,  # 斯维尔德鲁伊--寒冰（可以对防御塔和我方，或者敌方）
    "Elven Ranger_Arrow" : 2,  # 精灵游侠--箭
    "Gryphon Bombardier_Bomb" : 2,  # 狮鹫投弹手--炸弹
    "Arcane Magus_energy" : 2,  # 奥数大师--能量
    "Musketeer_Bullet"   : 2,# 火枪手--子弹
    "Shadow Archers_Arrow"  : 2,#箭塔普通攻击弓箭
    "Shadow Mark_Arrow" : 2, #箭塔暗影标记箭
    "Blade of Demise_Kill" : 2, #箭塔秒杀
    "Crow" : 2, #箭塔召唤兽——乌鸦
    "Infernal Mage_Fire" : 2, #恶魔法师塔火焰普通攻击
    "Infernal Mage_infernal rune" : 2, #恶魔法师塔恶魔符文技能
    "Infernal Mage_lava geysers" : 2, #恶魔法师塔熔岩喷射技能
    "Rocket Riders_Rocket_Level1" : 2, #火箭队塔普通攻击火箭等级1
    "Rocket Riders_Rocket_Level2" : 2, #火箭队塔普通攻击火箭等级2
    "Rocket Riders_Rocket_Level3" : 2, #火箭队塔普通攻击火箭等级3
    "Rocket Riders_Rocket_Level4" : 2, #火箭队塔普通攻击火箭等级4
    "Specter" : 2, #死灵墓普通攻击
    "Bone Flinger_Bone_Level1" : 2, #掷骨者普通攻击等级1
    "Bone Flinger_Bone_Level2" : 2, #掷骨者普通攻击等级2
    "Bone Flinger_Bone_Level3" : 2, #掷骨者普通攻击等级3
    "Bone Flinger_Bone_Level4" : 2, #掷骨者普通攻击等级4
    "Elite Harasser_Arrow" : 2, #骚扰者普通攻击
    "Elite Harasser_Arrow_Storm" : 2,# 骚扰者箭群
      #add more item here...
    'Soul Impact_1' : 2, # 灵魂冲击,这里表示的绿色的技能特效而不是技能槽里的技能的图片
} # key: unit_name, value: is_tower or not
