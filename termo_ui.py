from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import bs4

class TermoUi:
    def __init__(self, webdriver_path, bot):
        self.bot = bot
        self.driver = webdriver.Chrome(executable_path=webdriver_path)
        self.actions = ActionChains(self.driver)

    def run(self):
        self.driver.get("https://term.ooo/")
        
        self.type_word("coras")
        sleep(2)
        self.parse_result_to_bot()

    def type_word(self, word):
        self.actions.click()
        self.actions.send_keys(word)
        self.actions.send_keys(Keys.RETURN)
        self.actions.perform()

    # palabra fica no localstorage
    def _get_html(self):
        innerHTML = self.driver.execute_script("return document.body.innerHTML")
        print(innerHTML)
        return bs4.BeautifulSoup(innerHTML,"lxml")

    def parse_result_to_bot(self):
        page = self._get_html()
        words_div = page.find_all("wc-row")
        print(f"words div {len(words_div)}")
        for word_div in words_div:
            print(f"word div {len(words_div)}")
            for index, letter_div in enumerate(word_div.find_elements(By.TAG_NAME, "div")):
                letter_state = letter_div.get_attribute("class")
                letter = letter_div.get_attribute('innerHTML')
                if letter_state == "letter wrong":
                    self.bot.add_no_contains(letter)
                    print("Nao Contém - "+letter)
                elif letter_state == "letter place":
                    print("Contém algum exatamente - "+letter)
                    self.bot.add_contains(letter)
                    self.bot.add_no_contains_exact(letter)
                else:
                    print("Contém exatamente - "+letter)
                    self.bot.add_contains(letter)
                    self.bot.add_contains_exact(letter, index)

