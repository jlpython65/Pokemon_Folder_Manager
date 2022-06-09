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

    for i in range(int(len(list_of_pokemon)/2)):
            NUMBER = list_of_pokemon[2*i]
            if i == 0:
                NUMBER = list_of_pokemon[0]
            NAME = list_of_pokemon[(2*i)+1]
            if i == 0:
                NAME = list_of_pokemon[1]
        
    print(NUMBER+" "+NAME)
    for image_filename in glob.iglob(src_path+r"/*.png"): 
        if re.search(f'{NUMBER}', image_filename):
            try:
                os.rename(image_filename,src_path+"\\"+f"{NAME}"+".png")
                print(image_filename)
            except:
                os.rename(image_filename,image_filename.replace(f'{NUMBER}',f'{NAME}'))



rename_pokemon()
