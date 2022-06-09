#Pokemon_file_rename

import imp
from lib2to3.pgen2.token import NAME, NUMBER
import os
import shutil
import glob
import re
from tokenize import Number

src_path = r"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\gen8 - Copy"

def delete_back_shinies_gigashiny():
    regex = r'.+?sb.png|.+?b.png|.+?s.png' #.+? is satisfied after the sprite number so regex moves onto matching the sb part. Actually greedy or not greedy, wouldn't make a difference. Greedy, the dot would bakc trakc

    glob.glob(src_path, recursive=False) #recursive false becasue I want to delete sprites in THIS folder


    for sprite in glob.iglob(src_path+r"/*.png"): #iglob is an iterator version of glob
        if re.search(regex, sprite):
            print(sprite)
            os.remove(sprite)

def rename_new_forms():
    regex = r'.+?\_\d\d+?' #.+? is satisfied after the sprite number so regex moves onto matching the sb part. Actually greedy or not greedy, wouldn't make a difference. Greedy, the dot would bakc trakc

    glob.glob(src_path, recursive=False) #recursive false becasue I want to delete sprites in THIS folder


    for sprite in glob.iglob(src_path+r"/*.png"): #iglob is an iterator version of glob
        if re.search(regex, sprite):    
            print(sprite)
            os.remove(sprite)

def rename_pokemon():
    list_of_pokemon = input("please insert list of pokemon here").split()
    print(list_of_pokemon)

    # for sprite in glob.iglob(src_path+r"/*.png"): #iglob is an iterator version of glob
    #     if re.search(r'_', sprite):
    #         re.match(r'',sprite)
    #         os.rename(sprite,fr'C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\gen8 - Copy\{}')
    #          #YOU CAN'T CHANGE STRINGS, you'll need to make a new one with parts of the string 
    #         #So maybe I can use os.join or whatever. parts of strings are assigned variables and are added together 



    for i in range(len(list_of_pokemon)): #Mr. Rime is split by a space 
        try:
            NUMBER = list_of_pokemon[2*i]
            if i == 0:
                NUMBER = list_of_pokemon[0]
        except:
            pass
        try:
                NAME = list_of_pokemon[(2*i)+1]
                if i == 0:
                 NAME = list_of_pokemon[1]
        except:
            pass
        
        print(NUMBER+" "+NAME)
        glob.glob(src_path, recursive=False)

        for sprite in glob.iglob(src_path+r"/*.png"): #iglob is an iterator version of glob shows the whole shooting range
            if re.search(f'{NUMBER}', sprite):    #find image with the number as the name
                try:
                    os.rename(sprite,src_path+"\\"+f"{NAME}"+".png")
                    print(sprite)
                except:
                    if re.search(f'{NUMBER}_', sprite):
                        os.rename(sprite,sprite.replace(f'{NUMBER}',f'{NAME}'))

    # Continue reading the book, review your previous problems and then come back. 

    #I don't get it, can sprite not be used as a path? It seems like it could
rename_pokemon()
