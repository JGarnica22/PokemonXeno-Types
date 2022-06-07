# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:14:02 2020

@author: neil_
"""
#The purpose of this script is to summarize the defensive properties of any type combination in Pokemon. Current games recognize 18 types, but this script was developed to strategize in an unofficial fan-made Pokemon game (Pokemon Xenoverse: Per Aspera Ad Astra) that recognizes an additional type: "sound"

# Create list of types
Types = ["grass", "fire", "water", "electric", "rock", "ground", "poison",
         "bug", "flying", "psychic", "fighting", "ice", "ghost", "dark",
         "dragon", "normal", "fairy", "steel", "sound"]


##Create dicts for each type according to the damage multiplier. Each value is a list of types that use said multiplier on that type

# 2x damage
weaknesses = {
    "grass":["fire", "flying", "ice", "bug", "poison"],
    "fire":["water", "rock", "ground"],
    "water":["electric", "grass", "sound"],
    "electric":["ground"],
    "rock":["water", "grass", "fighting", "steel", "ground"],
    "ground":["water","grass","ice"],
    "poison":["ground","psychic"],
    "bug":["flying", "fire", "rock"],
    "flying":["electric", "rock", "ice", "sound"],
    "psychic":["dark", "bug", "ghost"],
    "fighting":["flying", "psychic", "fairy"],
    "ice":["rock", "fire", "steel", "fighting"],
    "ghost":["dark", "ghost"],
    "dark":["bug", "fairy", "fighting"],
    "dragon":["dragon", "ice", "fairy"],
    "normal":["fighting"],
    "fairy":["poison", "steel", "sound"],
    "steel":["fire", "fighting", "ground"],
    "sound":["dragon", "electric"]
    }

# 1/2x damage
resistances = {
    "grass":["water", "ground", "grass", "electric"],
    "fire":["steel", "fire", "grass", "ice", "fairy","bug"],
    "water":["steel", "fire", "ice", "water"],
    "electric":["flying", "steel", "electric", "sound"],
    "rock":["normal", "flying", "poison", "fire"],
    "ground":["poison", "rock"],
    "poison":["fighting", "poison", "grass", "bug", "fairy"],
    "bug":["fighting", "ground", "grass"],
    "flying":["bug","fighting", "grass"],
    "psychic":["fighting", "psychic"],
    "fighting":["rock", "bug", "dark"],
    "ice":["ice"],
    "ghost":["poison", "bug"],
    "dark":["dark", "ghost"],
    "dragon":["grass", "fire", "water", "electric", "sound"],
    "normal":[],
    "fairy":["dark", "bug", "fighting"],
    "steel":["normal", "flying", "rock", "bug", "steel", "grass", "psychic", "ice", "dragon", "fairy" ],
    "sound":["water", "flying", "fairy"]
    }

# 0x damage
immunities = {
    "ground":["electric"],
    "normal":["ghost"],
    "ghost":["normal", "fighting"],
    "flying":["ground"],
    "steel":["poison"],
    "dark":["psychic"],
    "fairy":["dragon"],
    "grass":[] ,
    "fire":[],
    "water":[],
    "electric":[],
    "rock":[],
    "poison":[],
    "bug":[],
    "psychic":[],
    "fighting":[],
    "ice":[],
    "dragon":[],
    "sound":[]
    }

print("\nSo you want to be a Pokemon Master?")
print("\nChoose two types from the list:")
print(Types)

#while loop that will run until user confirms quit
run_again = None
while run_again != "q":
    type1 = input("Enter first type: ")
    type2 = input("Enter second type: ")
    
    # Users can leave one type blank to get summary of mono-typed combinations
    if type1 == "":
        type1 = type2
        
    if type2 == type1:
         type2 = ""
    
    # change this to "in Types"
    if type2 != "" and type1 != "":
    
        weaknesses1 = weaknesses[type1]
        weaknesses2 = weaknesses[type2]
        resistances1 = resistances[type1]
        resistances2 = resistances[type2]
        immunities1 = immunities[type1]
        immunities2 = immunities[type2]
        
        #There are 6 possible damage multipliers
        x0 = immunities[type1] + immunities[type2]
        nonimmune = set(Types)^set(x0)
        
        x4 = list(set(weaknesses1).intersection(weaknesses2))
        x1_4 = list(set(resistances1).intersection(resistances2))
        
        x1 = list(set(weaknesses1).intersection(resistances2)) + list(set(weaknesses2).intersection(resistances1))
        
        x2 = list((set(weaknesses1)^set(weaknesses2)^set(x1)).intersection(nonimmune))
        x1_2 = list((set(resistances1)^set(resistances2)^set(x1)).intersection(nonimmune))
        x1 = list(set(Types)^set(x0 + x4 + x2 + x1_4 + x1_2))
    
    
        print("\nType combination: ", type1, "/", type2)
        print("Takes x4 damage from: ", x4)
        print("Takes x2 damage from: ", x2)
        print("Takes x1 damage from: ", x1)
        print("Takes x1/2 damage from: ", x1_2)
        print("Takes x1/4 damage from: ", x1_4)
        print("Takes x0 damage from: ", x0)
    
    elif type2 == "" and type1 == "":
        print ("\nChoose from types:\n", Types)
    
    else:
        x2 = weaknesses[type1]
        x1_2 = resistances[type1]
        x0 = immunities[type1]
        x1 = list(set(Types)^set(x0 + x2 + x1_2))
        
        print("Type: ", type1,)
        print("Takes x2 damage from: ",  x2)
        print("Takes x1 damage from: ",  x1)
        print("Takes x1/2 damage from: ", x1_2)
        print("Takes x0 damage from: ", x0)

    run_again = input("Run again? enter 'q' to quit \n")
    if run_again != "q":
        run_again == ""
    else:
        print("Peace out, future champ")