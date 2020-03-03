import pandas as pd 
from bs4 import BeautifulSoup
import requests
import urllib.request
import lxml

STATS = {
    'Top': {
        'pitcher_id': [],
        'batter_id': [],
        'bat_count':[],
        'pitch_count': [],
        'time_thrown': [],
        'pitch_description':[],
        'pitch_type': [],
        'break_length': [],
        'break_angle': [],
        'x_axis': [],
        'y_axis': [],
        'start_speed': [],
        'end_speed': [],
        'strikezone_top': [],
        'strikezone_bottom' : [],
        'pfx_x': [],
        'pfx_z': [],
        'event': [],
        'play_description': [],
        'px': [],
        'pz': [],
        'xo': [],
        'yo':[],
        'zo':[],
        'vxo':[],
        'vyo':[],
        'vzo':[],
        'ax': [],
        'ay': [],
        'az': [],
        'break_y':[]
    },
    'Bottom': {
        'pitcher_id': [],
        'batter_id': [],
        'bat_count':[],
        'pitch_count': [],
        'time_thrown': [],
        'pitch_description':[],
        'pitch_type': [],
        'break_length': [],
        'break_angle': [],
        'x_axis': [],
        'y_axis': [],
        'start_speed': [],
        'end_speed': [],
        'strikezone_top': [],
        'strikezone_bottom' : [],
        'pfx_x': [],
        'pfx_z': [],
        'event': [],
        'play_description': [],
        'px': [],
        'pz': [],
        'xo': [],
        'yo':[],
        'zo':[],
        'vxo':[],
        'vyo':[],
        'vzo':[],
        'ax': [],
        'ay': [],
        'az': [],
        'break_y':[]
    }
}


class Baseball:

    def run(self):
        soup = self.getStats()
        self.top_inning(soup)
        self.bottom_inning(soup)
        self.dataframe_analysis()
       

    def getStats(self):
        baseball_URL = 'https://gd2.mlb.com/components/game/mlb/year_2019/month_07/day_15/gid_2019_07_15_detmlb_clemlb_1/inning/inning_1.xml'
        datat_source = urllib.request.urlopen(baseball_URL).read()
        soup = BeautifulSoup(datat_source,'lxml')
        return soup



    def top_inning(self, soup):
        top_inning_stats = soup.find('top')
        
        for atbat in top_inning_stats.find_all('atbat'):
            event = str(atbat['event']) # Event of at-bat
            play_description = str(atbat['des']) # Description of what occurred
            pitcher_id = str(atbat['pitcher']) # unique id asspciated with pitcher
            batter_id = str(atbat['batter']) # unique id associated with batter
            bat_count = str(atbat['num']) # number of batter faced by pitcher
            for pitch_id in atbat.find_all('pitch'):
              STATS['Top']['pitch_count'].append(str(pitch_id['id'])) # Gets the pitch count
              STATS['Top']['pitch_description'].append(str(pitch_id['des'])) # Gives a description of what occurred during the pitch
              STATS['Top']['pitch_type'].append(str(pitch_id['pitch_type'])) # Type of pitch thrown
              STATS['Top']['break_length'].append(str(pitch_id['break_length'])) # measurement in inches between the release point to home plate
              STATS['Top']['break_angle'].append(str(pitch_id['break_angle'])) # amgle in degrees from vertical to the straight line path from the release point
              STATS['Top']['x_axis'].append(str(pitch_id['x'])) # Horizontal pitch location of the pitch crossing home plate
              STATS['Top']['y_axis'].append(str(pitch_id['y'])) # Vertical pitch location of the pitch crossing home plate
              STATS['Top']['start_speed'].append(str(pitch_id['start_speed'])) # speed of pitch in miles per hour measured at initial point
              STATS['Top']['end_speed'].append(str(pitch_id['end_speed'])) # speed of pitch in miles per hour measured as it crosses home plate
              STATS['Top']['strikezone_top'].append(str(pitch_id['sz_top'])) # distance in feet from ground to top of batter's strike zone
              STATS['Top']['strikezone_bottom'].append(str(pitch_id['sz_bot'])) # distance in feet from ground to bottom of batter's strike zone
              STATS['Top']['pfx_x'].append(str(pitch_id['pfx_x'])) # horizontal movement of the pitch between the release point and home plate 
              STATS['Top']['pfx_z'].append(str(pitch_id['pfx_z'])) # the vertical movement of the pitch between the release point and home plate
              STATS['Top']['px'].append(str(pitch_id['px'])) # left/right distance of the pitch from the middle of the plate as it crossed home plate
              STATS['Top']['pz'].append(str(pitch_id['pz'])) # height of the pitch as it crossed home plate
              STATS['Top']['xo'].append(str(pitch_id['x0'])) # left/right distance of the pitch at its initial point
              STATS['Top']['yo'].append(str(pitch_id['y0'])) # distance in feet from home plate where the pitch system is set to measure the intial parameters
              STATS['Top']['zo'].append(str(pitch_id['z0'])) # height of the pitch measured at the initial point
              STATS['Top']['vxo'].append(str(pitch_id['vx0'])) # velocity of pitch measured in 3 dimensions
              STATS['Top']['vyo'].append(str(pitch_id['vy0'])) # veloicty of pitch measured in 3 dimensions
              STATS['Top']['vzo'].append(str(pitch_id['vz0'])) # velocity of pitch measurted in 3 dimensions
              STATS['Top']['ax'].append(str(pitch_id['ax'])) # acceleration of pitch measured in 3 dimensions
              STATS['Top']['ay'].append(str(pitch_id['ay'])) # acceleration of pitch measured in 3 dimensions
              STATS['Top']['az'].append(str(pitch_id['az'])) # acceleration of pitch measured in 3 dimensions
              STATS['Top']['break_y'].append(str(pitch_id['break_y'])) # distance in feet where pitch achieved greatest deviation from initial point to home plate
              STATS['Top']['time_thrown'].append(str(pitch_id['tfs_zulu'])) # time stamp of when pitch was thrown
              STATS['Top']['event'].append(event)
              STATS['Top']['play_description'].append(play_description)
              STATS['Top']['pitcher_id'].append(pitcher_id)
              STATS['Top']['batter_id'].append(batter_id)
              STATS['Top']['bat_count'].append(bat_count)
        print("DONE WITH TOP INNING")
            
    def bottom_inning(self, soup):
        bottom_inning_stats = soup.find('bottom')
        
        for atbat in bottom_inning_stats.find_all('atbat'):
            event = str(atbat['event']) # Event of at-bat
            play_description = str(atbat['des']) # Description of what occurred
            pitcher_id = str(atbat['pitcher']) # unique id asspciated with pitcher
            batter_id = str(atbat['batter']) # unique id associated with batter
            bat_count = str(atbat['num']) # number of batter faced by pitcher
            for pitch_id in atbat.find_all('pitch'):
              STATS['Bottom']['pitch_count'].append(str(pitch_id['id'])) # Gets the pitch count
              STATS['Bottom']['pitch_description'].append(str(pitch_id['des'])) # Gives a description of what occurred during the pitch
              STATS['Bottom']['pitch_type'].append(str(pitch_id['pitch_type'])) # Type of pitch thrown
              STATS['Bottom']['break_length'].append(str(pitch_id['break_length'])) # measurement in inches between the release point to home plate
              STATS['Bottom']['break_angle'].append(str(pitch_id['break_angle'])) # amgle in degrees from vertical to the straight line path from the release point
              STATS['Bottom']['x_axis'].append(str(pitch_id['x'])) # Horizontal pitch location of the pitch crossing home plate
              STATS['Bottom']['y_axis'].append(str(pitch_id['y'])) # Vertical pitch location of the pitch crossing home plate
              STATS['Bottom']['start_speed'].append(str(pitch_id['start_speed'])) # speed of pitch in miles per hour measured at initial point
              STATS['Bottom']['end_speed'].append(str(pitch_id['end_speed'])) # speed of pitch in miles per hour measured as it crosses home plate
              STATS['Bottom']['strikezone_top'].append(str(pitch_id['sz_top'])) # distance in feet from ground to top of batter's strike zone
              STATS['Bottom']['strikezone_bottom'].append(str(pitch_id['sz_bot'])) # distance in feet from ground to bottom of batter's strike zone
              STATS['Bottom']['pfx_x'].append(str(pitch_id['pfx_x'])) # horizontal movement of the pitch between the release point and home plate 
              STATS['Bottom']['pfx_z'].append(str(pitch_id['pfx_z'])) # the vertical movement of the pitch between the release point and home plate
              STATS['Bottom']['px'].append(str(pitch_id['px'])) # left/right distance of the pitch from the middle of the plate as it crossed home plate
              STATS['Bottom']['pz'].append(str(pitch_id['pz'])) # height of the pitch as it crossed home plate
              STATS['Bottom']['xo'].append(str(pitch_id['x0'])) # left/right distance of the pitch at its initial point
              STATS['Bottom']['yo'].append(str(pitch_id['y0'])) # distance in feet from home plate where the pitch system is set to measure the intial parameters
              STATS['Bottom']['zo'].append(str(pitch_id['z0'])) # height of the pitch measured at the initial point
              STATS['Bottom']['vxo'].append(str(pitch_id['vx0'])) # velocity of pitch measured in 3 dimensions
              STATS['Bottom']['vyo'].append(str(pitch_id['vy0'])) # veloicty of pitch measured in 3 dimensions
              STATS['Bottom']['vzo'].append(str(pitch_id['vz0'])) # velocity of pitch measurted in 3 dimensions
              STATS['Bottom']['ax'].append(str(pitch_id['ax'])) # acceleration of pitch measured in 3 dimensions
              STATS['Bottom']['ay'].append(str(pitch_id['ay'])) # acceleration of pitch measured in 3 dimensions
              STATS['Bottom']['az'].append(str(pitch_id['az'])) # acceleration of pitch measured in 3 dimensions
              STATS['Bottom']['break_y'].append(str(pitch_id['break_y'])) # distance in feet where pitch achieved greatest deviation from initial point to home plate
              STATS['Bottom']['time_thrown'].append(str(pitch_id['tfs_zulu'])) # time stamp of when pitch was thrown
              STATS['Bottom']['event'].append(event)
              STATS['Bottom']['play_description'].append(play_description)
              STATS['Bottom']['pitcher_id'].append(pitcher_id)
              STATS['Bottom']['batter_id'].append(batter_id)
              STATS['Bottom']['bat_count'].append(bat_count)
        print("DONE WITH BOTTOM INNING")

    def dataframe_analysis(self):
        top_frame = pd.DataFrame(STATS['Top'])
        bottom_frame = pd.DataFrame(STATS['Bottom'])
        print(top_frame)
        print(bottom_frame)
              


                







if __name__ == "__main__":
    zelus = Baseball()
    zelus.run()