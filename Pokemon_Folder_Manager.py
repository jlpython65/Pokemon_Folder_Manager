#Pokemon_file_rename

import imp
from lib2to3.pgen2.token import NAME, NUMBER
import os
import shutil
import glob
import re
from tokenize import Number

import re


string = "Geeks for Geeks"
pattern = "Geeks for Geeks"

print(re.match(pattern, string))
print(re.fullmatch(pattern, string))

src_path = r"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\gen8"

def delete_back_shinies_gigashiny(dir_list):
    regex = r'.+?sb.png|.+?b.png|.+?s.png' #.+? is satisfied after the sprite number so regex moves onto matching the sb part. Actually greedy or not greedy, wouldn't make a difference. Greedy, the dot would bakc trakc


    for x in range(len(dir_list)):
        for sprite in glob.iglob(dir_list[x]+r"/*.png"): #iglob is an iterator version of glob
            if re.search(regex, sprite):
                print(sprite)
                os.remove(sprite)

def rename_pokemon(dir_list):
    list_of_pokemon = input("please insert list of pokemon here").split()
    print(list_of_pokemon)

    for i in range(int(len(list_of_pokemon)/2)):
        NUMBER = list_of_pokemon[2*i]
        if i == 0:
            NUMBER = list_of_pokemon[0]
        NAME = list_of_pokemon[(2*i)+1]
        if i == 0:
            NAME = list_of_pokemon[1]
            
        print(NUMBER+" "+NAME)

        for x in range(int(len(dir_list))):
            PATH=dir_list[x]
            PATH_FOR_REG = dir_list[x].replace("\\","\\\\")
            print("Looking through path: " + f'{PATH}')
            for image_filename in glob.iglob(fr'{PATH}'+fr"/{NUMBER}.png"):
                print(image_filename)
                
                try:
                    os.rename(image_filename,fr'{PATH}'+"\\"+f"{NAME}"+".png")

                except:
                    os.rename(image_filename,fr'{PATH}'+"\\"+f"{NUMBER}".replace(f'{NUMBER}',f'{NAME}'))

dir_list= []


for dirpath, dirs, files in os.walk(r'C:\Users\JASON LEE\Documents\1Python\Pokemon_Game', topdown=False): #returns 3-tuple (dirpath, dirnames, filenames)
    print(dirpath)
    if re.search("gen",dirpath):
        dir_list.append(dirpath)

delete_back_shinies_gigashiny(dir_list)
rename_pokemon(dir_list)
