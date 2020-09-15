from googleapiclient.discovery import build
import logging
import json
import pygame
import schedule
import time

"""API section"""

api_key = 'Your Youtube API_Key HERE!'

# service
youtube = build('youtube', 'v3', developerKey = api_key)

# Create request
request = youtube.channels().list(part = 'statistics', id = 'UCy0YHkGM8szRMOhIkNUFwiA')
response = request.execute()  # Read youtube API raw data


"""Logging Section"""

logger = logging.getLogger(__name__)  # Logger obj created

# Setting level
logger.setLevel(logging.INFO)

# Formating
formatter = logging.Formatter('%(asctime)s:%(message)s')

# Creating a new Log file
file_handler = logging.FileHandler('SubsReport.txt')
file_handler.setFormatter(formatter)

# Adding the file to our logger
logger.addHandler(file_handler)

# End Logger section

"""Data treatment"""

# Read data from youtube API
data = response

"""Extract subscriber from Nested Dictionary"""
def subscribers():
    subs = data['items'][0]['statistics']['subscriberCount']
    return (subs)

"""GUI section"""
pygame.init()
pygame.display.init()
pygame.display.set_caption("Youtube Subscriber Counter by @iobotic")

"""Screen settings"""
scr_width = 900
scr_height = 600
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

black = (0,0,0)
mBlack = (20,20,20)
white = (255,255,255)
red = (255,0,0)

screen.fill(black)


"""Visuals Functions"""

def checkitout():
    """show subscribers"""
    newsubs = subscribers() # Reading YT_Subs
    
    # Show Up!
    font = pygame.font.SysFont(None, 500)
    text = font.render(newsubs, True, white)
    screen.blit(text,(scr_width/2 - text.get_rect().width/2+240, scr_height/2 - text.get_rect().height/2+100))
    pygame.display.update()
    logger.info("The number of suscribers = {}".format(newsubs))

def firstView():
    """show subscribers"""
    newsubs = subscribers() # Reading YT_Subs
    
    # Show Up!
    font = pygame.font.SysFont(None, 500)
    text = font.render(newsubs, True, white)
    screen.blit(text,(scr_width/2 - text.get_rect().width/2+240, scr_height/2 - text.get_rect().height/2+100))
    pygame.display.update()
    
def info():
    font = pygame.font.SysFont(None,140)
    info = font.render("SUSCRIPTORES", True, red)
    screen.blit(info, (300,540))
    pygame.display.update()
    
    
    
"""Schedule"""

# every 30 minutes
schedule.every(30).minutes.do(checkitout)

"""Main code"""
firstView()
exitsubs = False

while(exitsubs == False):
    for event in pygame.event.get():
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_e):
                exitsubs = True

    schedule.run_pending()
    time.sleep(0.1)
    info()

pygame.quit()
    
