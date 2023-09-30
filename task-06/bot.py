from logging import exception
import os

import discord
from dotenv import load_dotenv

from fileinput import filename
import requests
from bs4 import BeautifulSoup
import csv
from datetime import date
from scraper import *

load_dotenv()


client = discord.Client()

try:
    @client.event
    async def on_ready():
        
        print(f'{client.user} has connected to Discord!')
        

        
        
        



    @client.event
    async def on_message(message):
        if message.content.startswith('!livescore'):
            await message.channel.send("fetching livescores")
            summary,score=scraper()


            
            date_of_the_day=date.today()


            fields=['score','summary','date']
            rows=[ [score.text,summary.text,date_of_the_day]]
            filename="Score.csv"
            with open(filename, 'a') as csvfile: 
                    
                csvwriter = csv.writer(csvfile) 
                csvwriter.writerows(rows)

            
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

except Exception:
    pass

  

client.run('MTE1MDAwNDExNTg2MzI1Mjk5Mg.Gt-M61.xMY681ulQ_ISdiTUaAfjkY_KQvFVpLEPEqIC5I')