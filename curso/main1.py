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
            print("PRECIONE A TECLA SHIFT + Q PARA CANSELAR")
            print()
            temp_name = input("Name: ")
            if len(temp_name)!= 0 and temp_name != "Q".upper():
                db = sqlite3.connect("connection")
                cursor = db.cursor()
                cursor.execute("SELECT Name FROM contacts")
                results = cursor.fetchall()
                for i in results:
                    if temp_name in i:
                        print("ESTE CONTATO JA EXISTE NO NOSSO BANCO DE DADOS")
                        time.sleep(3)
                        self.add()
                self.name = temp_name 
                temp_name = ""
                    
                time.sleep(0.20)
                self.phone = input("Phone : ")
            
                time.sleep(0.20)
                self.address = input("Address : ")
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
            elif temp_name == "Q".upper():
                print("SAINDO DO MENU PRINCIPAL!!")
                time.sleep(2)
                self.menu()
            else:
                self.beep()
                self.beep()
                print("VAFOR PRENCHER TODOS OS CAMPOS!!!!")
                time.sleep(2)
                self.add()
    def remover(self):
        print()
        print("=========================DELETAR CADASTROS=========================")
        print("")

        name = input("DIGITE O NOME DO CLIENTE PARA DELETAR : ")
        confirm = input("TEM CERTEZA ? (Y/N)")
        if confirm == "y".lower():
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            cursor.execute("DELETE FROM contacts WHERE Name = ?",(name,))
            db.commit()
            print("CADASTRO DELETADO COM SUCESSO...")
            time.sleep(3)
            self.menu()
        else:
            print("SAINDO DO MENU PRINCIPAL..")
            time.sleep(3)
            self.menu()




    def update(self):
        print()
        print("=========================ATUALIZAR CADASTROS=========================")
        name = input("DIGITE O NOME DO CLIENTE PARA ATUALIZAR : ")
        confirm = input("TEM CERTEZA ? (Y/N)")
        if confirm == "y".lower():
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            phone_update = input("ATUALIZAR TELEFONE ? (Y/N)")
            if phone_update == "y".lower():
                phone = input("DIGITE O NUMERO DE TELEFONE : ")
                cursor.execute("UPDATE  contacts SET Phone = ? WHERE Name = ?",(phone,name))
                db.commit()
                print("CADASTRO ATUALIZADO COM SUCESSO...")
                time.sleep(3)
    
            
            address_update = input("ATUALIZAR ENDERECO ? (Y/N)")
            if address_update == "y".lower():
                addrees = input("DIGITE O NOVO ENDEREÇO : ")
                cursor.execute("UPDATE  contacts SET Address = ? WHERE Name = ?",(addrees,name))
                db.commit()
                time.sleep(3)
            if phone_update != "y".lower() and address_update != 'y':
                print("SAINDO DO MENU PRINCIPAL, SEM FAZER ATUALOZAÇÕES")
                time.sleep(3)
                self.menu()
            print("ENDEREÇO ATUALIZADO COM SUCESSO...")
            db.close()
            time.sleep(3)
            self.menu()
        else:
            print("SAINDO DO MENU PRINCIPAL, SEM FAZER ATUALOZAÇÕES")
            time.sleep(3)
            self.menu()


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
        #print(results)
        #time.sleep(0.50)
        for row in results:
            time.sleep(0.50)
            count += 1
            count_2 += 1
            print(count_2,row)
            if count == 5:
                input("PRECIONE QUALQUER TECLA PARA CONTINUAR ...")
                count = 0
            print()
        print()
        print("FINAL DOS RESULTADOS !!")
        db.close()
        print()
        print("PRECIONE QUALQUER TECLA PARA CONTINUAR")
        option = input("APERTE (U) PARA ATUALIZAR (D) PARA DELETAR (M) PARA MENU : ")
        if option == "u".lower():
            self.update()
        elif option == "d".lower():
            self.remover()
        elif option == "m".lower():
            self.menu()

    
    def terminate(self):
        confirm = input("DESEJA SAIR DO SISTEMA? (y/n)")
        if confirm == "y".lower():
            print("SAINDO DO SISTEMA")
            self.beep()
            self.beep()
            self.beep()
            time.sleep(2)
            print("........")
            time.sleep(0.05)
            print(".....")
            time.sleep(0.05)
            print("....")
            time.sleep(0.05)
            print("...")
            time.sleep(0.05)
            print("..")
            time.sleep(0.05)
            print(".")
            exit()
        else:
            print("SAINDO DO MENU PRINCIPAL...")
            time.sleep(1)
            self.menu()
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
        print("1 :) CADASTRAR")
        
        time.sleep(0.05)
        print("2 :) DELETAR")

        time.sleep(0.05)
        print("3 :) ATUALIZAR")

        time.sleep(0.05)
        print("4 :) LISTAR")

        time.sleep(0.05)
        print("5 :) SAIR")
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

