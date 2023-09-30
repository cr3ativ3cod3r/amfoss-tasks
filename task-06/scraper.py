import os

import discord
from dotenv import load_dotenv

from fileinput import filename
import requests
from bs4 import BeautifulSoup
import csv
def scraper():
    
    response = requests.get('https://www.espncricinfo.com/live-cricket-score')
    soup=BeautifulSoup(response.content,'html.parser')





        
    
    summary=soup.find(class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")
    score=soup.find(class_="ds-flex ds-flex-col ds-mt-2 ds-mb-2")
    return summary,score
