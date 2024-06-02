import os,time,sqlite3
import pygame
import numpy as np

class Manager:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""
    def add(self):
       running = True
       while running:
           os.system("clear")
           print("-------------ADCIONE UM NOVO CONTATO--------")
           print()
           self.name = input("Name : ")
           time.sleep(0.20)

           self.phone = input("Phone : ")
           time.sleep(0.20)

           self.address = input("Address : ")
           db = sqlite3.connect("connection")
           cursor = db.cursor()
           cursor.execute("""INSERT INTO contacts\
                            (Name ,Phone ,Address )VALUES(?,?,?)""",\
                            (self.name,self.phone,self.address))
           db.commit()
           add_more = input("DESEJA ADCIONAR OUTRO CONTATO? (Y/N) :")
           if add_more == "y".lower():
               continue
           else:
               db.close()
               running = False
               print("SAINDO DO MENU!!")
               time.sleep(2)
               self.menu()
               
             
    def remover(self):
        pass

    def update(self):
        pass
    
    
    def get_list(self):
        count = 0 
        count_2 = 0
        db = sqlite3.connect("connection")
        cursor = db.cursor()
        os.system("clear")
        print("................CONTATOS................")
        time.sleep(0.50)
        cursor.execute("SELECT Name, phone,Address FROM contacts")
        results = cursor.fetchall()
        print(results)
        time.sleep(0.20)
    
    def terminate(self):
        pass

    def beep(self):
        # Inicializa o mixer do pygame
        pygame.mixer.init(frequency=44100)

        # Parâmetros do som do beep
        duration = 0.1  # Duração do beep em segundos
        frequency = 440  # Frequência do beep em Hz (440 Hz é a nota A)

        # Gera a onda senoidal para o beep
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        wave = 0.5 * np.sin(2 * np.pi * frequency * t)

        # Cria uma matriz 2D para som estéreo, duplicando a onda para ambos os canais
        stereo_wave = np.column_stack((wave, wave))

        # Converte para o formato adequado do pygame (16-bit signed integer)
        stereo_wave = np.int16(stereo_wave * 32767)

        # Converte a onda para um objeto Sound do pygame
        beep_sound = pygame.sndarray.make_sound(stereo_wave)

        # Toca o som do beep
        beep_sound.play()

        # Mantém o programa em execução até que o som termine de tocar
        pygame.time.wait(int(duration * 1000))

    def menu(self):
        os.system("clear")

        # Toca o beep quando o menu é exibido
        self.beep()

        print("----------------------MENU-----------------------------")

        time.sleep(0.05)
        print()
        print("1 :) Add")
        
        time.sleep(0.05)
        print("2 :) Update")

        time.sleep(0.05)
        print("3 :) Remover")

        time.sleep(0.05)
        print("4 :) Get_list")

        time.sleep(0.05)
        print("5 :) Terminate")
        print()
        
        opcao = input("SELECIONE UMA ACAO : ")
        if opcao == "1":
            self.add()

        elif opcao == "2":
            self.remover()

        elif opcao == "3":
            self.update()

        elif opcao == "4":
            self.get_list()
            
        elif opcao == "5":
            self.terminate()
        else:
            self.beep()
            print("ERRO! TENTA NOVAMENTE AS OPCOES DE 1-5")

            self.menu()
    def main(self):
        os.system("clear")
        if os.path.isfile("connection"):
            db = sqlite3.connect("connection")
            time.sleep(3)
            self.beep()
            print()
            print("CONECTADO AO BANCO DE DADOS!!")

            time.sleep(3)
            self.menu()


        else:
            print("ESSA CONECSÃO NÃO EXISTE!!") 
            print()
            time.sleep(3)
            self.beep()

            print("CRIANDO NOVA CONEXÃO COM O BANCO DE DADOS")
            time.sleep(3)
            db = sqlite3.connect("connection")

            cursor = db.cursor()
            cursor.execute("""CREATE TABLE contacts
                            (Name TEXT ,Phone TEXT,Address TEXT)""")

            self.beep()
            print()
        
            print("conexão criada com sucesso")
            print("conectado com sucesso")
            time.sleep(3)

            self.menu()

        self.menu()
contacts_manager = Manager()
contacts_manager.main()

