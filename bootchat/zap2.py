from selenium import webdriver
import time

class whatsappBot:
     def __init__(self):
        self.mensagem = " Bom dia pessoal está é uma mesangem de teste do chat boot que estou tentando fazer bjo"
        self.grupos = ["My grop"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        #self.drive = webdriver.Chrome(executable_path=r'./chromedriver.exe',chrome_options=options)
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)


        

    def EnviarMensagens(self):
        self.drive.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupos in self.grupos:
            grupo = self.drive.fimd_element_by_xpath(f"//spam[@title='{grupo}']")
            time.sleep(3)
            chat_box = self.drive.fimd_element_by_class_name('_1wjpf _3NFp9 _3FXB1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botão_enviar = self.drive.fimd_element_by_xpath("//spam [@data-icone='send']")
            time.sleep(3)
            botão_enviar.click()
            time.sleep(5)

bot = whatsappBot()
bot.EnviarMensagens()
