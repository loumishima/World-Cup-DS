# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 21:15:41 2018

@author: LuizH
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# =============================================================================
# INDIVIDUAL GOALS IN WORLD CUPS (1930 - 2010)
# =============================================================================
links = open("igoals.txt", "r").read()
links = links.split("\n")

count = 0
index_2014 = 0
index = []
name = []
role = []
goals = []
pens = []
assist = []
minutes =[]
matches = []

for link in links:
    
    page = requests.get(link)
    print(requests.get(link))

    soup = BeautifulSoup(page.content, 'html.parser')
    table_goal = soup.find('table', class_='table tbl-statistics sortable')
    table_head = soup.find('tbody')
    
    
    if count == 0:
        for row  in table_head.find_all('tr'):
            index_2014 = index_2014 + 1
            index.append(index_2014)
            name.append(row.find(class_ = 'tbl-playername teamname-nolink').get_text())
            role.append(None)
            goals.append(row.find(class_ = 'tbl-goalfor').get_text())
            pens.append(row.find(class_ = 'tbl-pens').get_text())
            assist.append(row.find(class_ = 'tbl-assist').get_text())
            minutes.append(row.find(class_ = 'tbl-minp').get_text())
            matches.append(row.find(class_ = 'tbl-mp').get_text())
             
              
             
    else:
        for row  in table_head.find_all('tr'):
            index.append(row.find(class_ = 'tbl-rownumber').get_text())
            name.append(row.find(class_ = 'tbl-playername teamname-nolink').get_text())
            role.append(row.find(class_ = 'tbl-role').get_text())
            goals.append(row.find(class_ = 'tbl-goalfor').get_text())
            pens.append(row.find(class_ = 'tbl-pens').get_text())
            assist.append(row.find(class_ = 'tbl-assist').get_text())
            minutes.append(row.find(class_ = 'tbl-minp').get_text())
            matches.append(row.find(class_ = 'tbl-mp').get_text())
        
    count = count + 1  
        
    #Creating the Dataframe 
    
players_g = pd.DataFrame({
        "rank": index,
        "name": name,
        "role":role,
        "goals":goals,
        "pens":pens,
        "assist":assist,
        "minutes":minutes,
        "matches":matches
               
        })
    
players_g = players_g[['rank','name','role','goals','pens','assist','minutes','matches']]
players_g.to_csv('cup-igoals.csv', index = False , header = True)

del index,name,role,goals,pens,assist,minutes,matches
count = 0
index_2014 = 0
# =============================================================================
# INDIVIDUAL CARDS IN WORLD CUPS (1930 - 2010)
# =============================================================================

links = open("icards.txt", "r").read()
links = links.split("\n")

index = []
name = []
role = []
y = []
second_y = []
red = []
minutes = []
matches =[]

for link in links:
    page = requests.get(link)
    print(requests.get(link))

    soup = BeautifulSoup(page.content, 'html.parser')
    table_goal = soup.find('table', class_='table tbl-statistics sortable')
    table_head = soup.find('tbody')
    
    if count == 0:
        for row  in table_head.find_all('tr'):
            index_2014 = index_2014 + 1
            index.append(index_2014)
            name.append(row.find(class_ = 'tbl-playername teamname-nolink').get_text())
            role.append(None)
            y.append(row.find(class_ = 'tbl-yc').get_text())
            second_y.append(row.find(class_ = 'tbl-2yc').get_text())
            red.append(row.find(class_ = 'tbl-rc').get_text())
            minutes.append(None)
            matches.append(row.find(class_ = 'tbl-mp').get_text())
        
    else:
        for row  in table_head.find_all('tr'):
            index.append(row.find(class_ = 'tbl-rownumber').get_text())
            name.append(row.find(class_ = 'tbl-playername teamname-nolink').get_text())
            role.append(row.find(class_ = 'tbl-role').get_text())
            y.append(row.find(class_ = 'tbl-yc').get_text())
            second_y.append(row.find(class_ = 'tbl-2yc').get_text())
            red.append(row.find(class_ = 'tbl-rc').get_text())
            minutes.append(row.find(class_ = 'tbl-minp').get_text())
            matches.append(row.find(class_ = 'tbl-mp').get_text())
            
    count = count + 1
            
players_c = pd.DataFrame({
        "rank": index,
        "name": name,
        "role":role,
        "yellow cards":y,
        "second yellow":second_y,
        "red cards":red,
        "minutes":minutes,
        "matches":matches
               
        })
    
players_c = players_c[['rank','name','role','yellow cards','second yellow','red cards','minutes','matches']]
players_c.to_csv('cup-icards.csv', index = False , header = True)
        
del index,name,role,y,second_y,red,minutes,matches
count = 0        
index_2014 = 0        
# =============================================================================
# TEAM GOALS IN WORLD CUPS (1930 - 2010)
# =============================================================================
links = open("tgoals.txt", "r").read()
links = links.split("\n")

index = []
team = []
goals_for = []
goals_against = []
penalty = []
matches = []

for link in links:
    page = requests.get(link)
    print(requests.get(link))

    soup = BeautifulSoup(page.content, 'html.parser')
    table_goal = soup.find('table', class_='table tbl-statistics sortable')
    table_head = soup.find('tbody')
    
    if count == 0:
        for row in table_head.find_all('tr'):
            index_2014 = index_2014 + 1
            index.append(index_2014)
            team.append(row.find(class_ = 'tbl-teamname teamname-nolink').get_text())
            goals_for.append(row.find(class_='tbl-goalfor').get_text())
            goals_against.append(row.find(class_='tbl-goalagainst').get_text())
            penalty.append(row.find(class_='tbl-pens').get_text())
            matches.append(row.find(class_='tbl-mp').get_text())
            
    else:
        for row  in table_head.find_all('tr'):
            index.append(row.find(class_ = 'tbl-rownumber').get_text())
            team.append(row.find(class_ = 'tbl-teamname teamname-nolink').get_text())
            goals_for.append(row.find(class_='tbl-goalfor').get_text())
            goals_against.append(row.find(class_='tbl-goalagainst').get_text())
            penalty.append(row.find(class_='tbl-pens').get_text())
            matches.append(row.find(class_='tbl-mp').get_text())
        
    count = count + 1
    
team_g = pd.DataFrame({
        "rank": index,
        "team": team,
        "goals for":goals_for,
        "goals against":goals_against,
        "penalties":penalty,
        "matches":matches
               
        })
    
team_g = team_g[['rank','team','goals for','goals against','penalties','matches']]
team_g.to_csv('cup-tgoals.csv', index = False , header = True)
        
del index,team,goals_for,goals_against,penalty,matches 
count = 0        
index_2014 = 0    
        
# =============================================================================
# TEAM CARDS IN WORLD CUPS (1930 - 2010)
# =============================================================================
links = open("tcards.txt", "r").read()
links = links.split("\n")

index = []
team = []
y = []
second_y = []
red = []
matches = []

for link in links:
    page = requests.get(link)
    print(requests.get(link))

    soup = BeautifulSoup(page.content, 'html.parser')
    table_goal = soup.find('table', class_='table tbl-statistics sortable')
    table_head = soup.find('tbody')
    if count == 0:
        for row  in table_head.find_all('tr'):
            index_2014 = index_2014 + 1
            index.append(index_2014)
            team.append(row.find(class_ = 'tbl-teamname teamname-nolink').get_text())
            y.append(row.find(class_ = 'tbl-y').get_text())
            second_y.append(row.find(class_ = 'tbl-2yc').get_text())
            red.append(row.find(class_ = 'tbl-rc').get_text())
            matches.append(row.find(class_ = 'tbl-mp').get_text())
        
    else:
        for row  in table_head.find_all('tr'):
            index.append(row.find(class_ = 'tbl-rownumber').get_text())
            team.append(row.find(class_ = 'tbl-teamname teamname-nolink').get_text())
            y.append(row.find(class_ = 'tbl-y').get_text())
            second_y.append(row.find(class_ = 'tbl-2yc').get_text())
            red.append(row.find(class_ = 'tbl-rc').get_text())
            matches.append(row.find(class_ = 'tbl-mp').get_text())
        
        
    count = count + 1
team_c = pd.DataFrame({
        "rank": index,
        "team": team,
        "yellow cards":y,
        "second yellow":second_y,
        "red cards":red,
        "matches":matches
        })
    
team_c = team_c[['rank','team','yellow cards','second yellow','red cards','matches']]
team_c.to_csv('cup-tcards.csv', index = False , header = True)
        
del index,team,y,second_y,red,matches        
count = 0        
index_2014 = 0  