import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import urllib

class G2WebScraper:
    def __init__(self) -> None:
        self.base_search_url = 'https://www.g2.com/search?utf8=%E2%9C%93&query='

        # selinium
        options = uc.ChromeOptions()
        # options.add_argument('--headless')  # Run in headless mode (no browser window)
        options.add_argument('--no-sandbox')
        options.add_argument('user-data-dir=Profile')  # Path to your chrome profile
        options.add_argument('--disable-dev-shm-usage')

        self.driver = uc.Chrome(options=options)

        self.driver.get("https://www.g2.com/")
        time.sleep(1)

    def randomSleep(self):
        time.sleep(random.randint(5, 10))

    def getSearchResults(self, query: str, limit: int):
        """
        Returns a list of search results from G2
        """
        url = self.base_search_url + urllib.parse.quote(query)
        self.driver.get(url)


        self.randomSleep()
        print(f'Page HTML: {self.driver.page_source}')

        # wait for the page to load
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div[4]/div[1]/div[1]/div/div/div[1]/a/div')))

        # time.sleep(50)
        print(self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div[4]/div[1]/div[1]/div/div/div[1]/a/div').text)
        div_counter = 4

        companies = []

        try:
            while div_counter-3 < limit:
                print(f'Getting result {div_counter-3}')
                
                try:
                    xpath = f'/html/body/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div[{div_counter}]/div[1]/div[1]/div/div/div[1]/a/div'
                    # get the name of the product using the xpath using undetectable chrome driver
                    element = self.driver.find_element(By.XPATH, xpath)
                    print(element.text)
                    div_counter += 1

                    companies.append(element.text)
                
                except:
                    # press button for next page
                    button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[3]/div/div[2]/ul/li[7]/a')
                    button.click()
                    self.randomSleep()
        
        except Exception as e:
            print(f'no more companies, error: {e}')

        return companies


# scraper = G2WebScraper()
# print(scraper.getSearchResults('ai software', 10))