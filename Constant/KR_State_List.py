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
#object:		tower/character/path	#防御塔/角色/地图的路径
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
}
