import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class SdarotBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # maximize window
        chrome_options.add_experimental_option("detach", True)  # prevet selenium from closing browser
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
        self.driver.find_element(By.XPATH, value='//form[@id = "mainSearch"]/div/input').send_keys(series_name)  # send series name
        self.driver.find_element(By.XPATH, '//form[@id = "mainSearch"]/div/span').click()  # click search

    def choose_season(self, season_number: str) -> None:
        """
        Clicks on the chosen season
        :param season_number: The number of the chosen season
        :return: None
        """
        self.driver.find_element(By.XPATH, value=f'//ul[@id = "season"]/li[{season_number}]').click()  # click chosen season

    def choose_episode(self, episode_number: str) -> None:
        """
        Click on the chosen episode, wait 30 sec and start the episode
        :param episode_number: The number of the chosen episode
        :return: None
        """
        self.driver.find_element(By.XPATH, value=f'//ul[@id = "episode"]/li[{episode_number}]').click()  # click chosen episode
        WebDriverWait(self.driver, timeout=40).until(EC.visibility_of_element_located((By.ID, "proceed"))).click()  # wait until proceed btn and click
        self.driver.find_element(By.XPATH, value="//section[@id = 'player']/div[2]/div[2]").click()  # start the episode


def main():
    parser = argparse.ArgumentParser(description='Sdarot script, insert the name of the series #season #episode')
    parser.add_argument("series", help="series to watch")
    parser.add_argument("season", help="Season to select")
    parser.add_argument("episode", help="Episode to watch")
    args = parser.parse_args()
    bot = SdarotBot()  # init bot
    bot.open()  # connect to sdarot website
    bot.search(args.series)  # search for the series
    bot.choose_season(args.season)  # chose season
    bot.choose_episode(args.episode)  # chose episode and have fun!


if __name__ == "__main__":
    main()
