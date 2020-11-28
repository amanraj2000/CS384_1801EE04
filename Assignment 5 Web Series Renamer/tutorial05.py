import pandas as pd
import csv
import os
import re

root_folder = os.getcwd()
def rename_FIR(folder_name):
    file_folder = root_folder+'/FIR'
    season_padding = int(input("Enter Season Padding: "))
    episode_padding = int(input("Enter Episode Padding: "))


    

def rename_Game_of_Thrones(folder_name):
    file_folder = root_folder + '/Game of Thrones'
    season_padding = int(input("Enter Season Padding: "))
    episode_padding = int(input("Enter Episode Padding: "))

    

def rename_Sherlock(folder_name):
    file_folder = root_folder + '/Sherlock'
    season_padding = int(input("Enter Season Padding: "))
    episode_padding = int(input("Enter Episode Padding: "))

    

def rename_Suits(folder_name):
    file_folder = root_folder + '/Suits'
    season_padding = int(input("Enter Season Padding: "))
    episode_padding = int(input("Enter Episode Padding: "))

    

def rename_How_I_Met_Your_Mother(folder_name):
    file_folder = root_folder + '/How I Met Your Mother'
    season_padding = int(input("Enter Season Padding: "))
    episode_padding = int(input("Enter Episode Padding: "))


web_series = input("Enter the web series: ").lower()
pattern = re.compile(r'\s+')
web_series = re.sub(pattern,'',web_series)
#web_series.replace(" ","")
print(web_series)
if web_series == 'fir':
    rename_FIR('fir')
elif web_series == 'game of thrones':
    rename_Game_of_Thrones('fir')
elif web_series == 'sherlock':
    rename_Sherlock('fir')
elif web_series == 'suits':
    rename_Suits('fir')
elif web_series == 'how i met your mother':
    rename_How_I_Met_Your_Mother('fir')
else:
    print("There isn't any file you are looking for! Please Try Later.")


