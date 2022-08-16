import argparse
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SdarotBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    def open(self) -> None:
        """
        Open Sdarot website
        :return: None
        """
        self.driver.get('https://www.sdarot.website/')

    def search(self, series_name: str) -> None:
        """
        Search the chosen series on Sdarot website
        :param series_name: The name of the chosen series
        :return: None
        """
        search_input = self.driver.find_element(By.XPATH, value='//form[@id = "mainSearch"]/div/input')
        search_input.send_keys(series_name)
        search_btn = self.driver.find_element(By.XPATH, '//form[@id = "mainSearch"]/div/span')
        search_btn.click()

    def choose_season(self, season_number: str) -> None:
        """
        Clicks on the chosen season
        :param season_number: The number of the chosen season
        :return: None
        """
        season_btn = self.driver.find_element(By.XPATH, value=f'//ul[@id = "season"]/li[{season_number}]')
        season_btn.click()

    def choose_episode(self, episode_number: str) -> None:
        """
        Click on the chosen episode, wait 30 sec and start the episode
        :param episode_number: The number of the chosen episode
        :return: None
        """
        episode_btn = self.driver.find_element(By.XPATH, value=f'//ul[@id = "episode"]/li[{episode_number}]')
        episode_btn.click()
        time.sleep(36)
        proceed = self.driver.find_element(By.ID, value="proceed")
        proceed.click()
        start = self.driver.find_element(By.XPATH, value="//section[@id = 'player']/div[2]/div[2]")
        start.click()


def main():
    parser = argparse.ArgumentParser(description='Sdarot script, insert the name of the series #season #episode')
    parser.add_argument("series", help="series to watch")
    parser.add_argument("season", help="Season to select")
    parser.add_argument("episode", help="Episode to watch")
    args = parser.parse_args()
    series = args.series
    season = args.season
    episode = args.episode
    bot = SdarotBot()  # init bot
    bot.open()  # connect to sdarot website
    bot.search(series)  # search for the series
    bot.choose_season(season)  # chose season
    bot.choose_episode(episode)  # chose episode and have fun!


if __name__ == "__main__":
    main()
