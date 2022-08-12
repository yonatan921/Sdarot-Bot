import argparse
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class sdarotBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    def open(self):
        self.driver.get('https://www.sdarot.website/')

    def search(self, sidraName):
        searchInput = self.driver.find_element(By.XPATH, value='//form[@id = "mainSearch"]/div/input')
        searchInput.send_keys(sidraName)
        searchBTN = self.driver.find_element(By.XPATH, '//form[@id = "mainSearch"]/div/span')
        searchBTN.click()

    def chooseSeason(self, seasonNumber):
        seasonBTN = self.driver.find_element(By.XPATH, value=f'//ul[@id = "season"]/li[{seasonNumber}]')
        seasonBTN.click()

    def chooseEpisode(self, episodeNumber):
        episodeBTN = self.driver.find_element(By.XPATH, value=f'//ul[@id = "episode"]/li[{episodeNumber}]')
        episodeBTN.click()
        time.sleep(36)
        proceed = self.driver.find_element(By.ID, value="proceed")
        proceed.click()
        start = self.driver.find_element(By.XPATH, value="//section[@id = 'player']/div[2]/div[2]")
        start.click()


parser = argparse.ArgumentParser(description='Sdarot script, insert the name of the series #season #episode')
parser.add_argument('-p', "--getargs", '--list', nargs='+', required=True)
value = parser.parse_args()

series = value.getargs[0]
season = value.getargs[1]
episode = value.getargs[2]
bot = sdarotBot()  # init bot
bot.open()  # connect to sdarot website
bot.search(series)  # search for the series
bot.chooseSeason(season)  # chose season
bot.chooseEpisode(episode)  # chose episode and have fun!
