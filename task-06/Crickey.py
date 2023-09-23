import os

import discord
from dotenv import load_dotenv

from fileinput import filename
import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

load_dotenv()


client = discord.Client()


@client.event
async def on_ready():
    
    print(f'{client.user} has connected to Discord!')
    

    
    
    



@client.event
async def on_message(message):
    if message.content.startswith('!livescore'):
        await message.channel.send("fetching livescores")
        response = requests.get('https://www.espncricinfo.com/live-cricket-score')
        soup=BeautifulSoup(response.content,'html.parser')





        
        team_1=soup.find(class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3")
        team_2=soup.find(class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")
        summary=soup.find(class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")
        score=soup.find(class_="ds-flex ds-flex-col ds-mt-2 ds-mb-2")


        
        date_of_the_day=date.today()


        fields=['Match','score','summary','date']
        rows=[ [(f"{team_1.text} vs {team_2.text}"),score.text,summary.text,date_of_the_day]]
        filename="Score.csv"
        with open(filename, 'a') as csvfile: 
                
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerows(rows)

        await message.channel.send(f"{team_1.text} vs {team_2.text}")
        await message.channel.send(score.text)
        await message.channel.send(summary.text)
        await message.channel.send(date_of_the_day)
    elif message.content.startswith('!csv'):
        await message.channel.send(file=discord.File(r'Score.csv'))
    elif message.content.startswith('!help'):
        await message.channel.send('! livescore-for livescore')
        await message.channel.send('! csv-for csv file')
    else:
        pass




  

client.run('MTE1MDAwNDExNTg2MzI1Mjk5Mg.Gt-M61.xMY681ulQ_ISdiTUaAfjkY_KQvFVpLEPEqIC5I')