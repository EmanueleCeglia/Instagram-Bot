from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random 

class InstaBot:
    def __init__(self, username, pw):
        self.options = Options()
        self.options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.driver = webdriver.Chrome(chrome_options = self.options, executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        #self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        sleep(2)
        #self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        #sleep(2)
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()   #ricerca del pulsante login da xpath
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)    #creca il nome username e invia il parametro username
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)          #come sopra
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()                   #cerca il pulsante submit e clicca
        sleep(15)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()   #chiude il pop up della pagina successiva 
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()   #chiude il pop up della pagina successiva

    def get_names(self):    #prende i nomi dalla lista followers o following 
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")   #assegna alla variabile scroll_box l'elemento barra di navigazione verticale
        last_ht = 0
        ht = 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script(""" arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight; """, scroll_box)  #esegue uno script JS di scrolling
        links = scroll_box.find_elements_by_tag_name('a')       #assegna a links il nome 
        names = [name.text for name in links if name != '']     #inserisce nel vettore names tutti i nomi
        #close buttion
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
        return names

    def get_unfollowers(self):   #confronta le liste following e followers e ritorno chi non ti segue 
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a').click()      #ricerca da href con nome passato da format
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        following = self.get_names()
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        followers = self.get_names()

        not_following_back = []
        for user in following:
            if user not in followers:
                not_following_back.append(user)
                
        return not_following_back
    
    def pick_unfollower(self, persona):
        num = random.randrange(0, len(persona))
        person = persona[num]
        
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(person)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/ul/div[1]/a/div/div[2]/div[1]/div/div').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[1]/div/button').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys('PLATA O PLOMO!!')
        
        
my_bot = InstaBot('emanuele_ceglia','******')
persona = my_bot.get_unfollowers()
ciao = my_bot.pick_unfollower(persona)



