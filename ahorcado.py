import random
import os 


def words():
    words=[]
    with open(r"C:\Users\ADMIN\Desktop\PLATZI\CURSO_INTERMEDIO_PYTHON\final_project\data.txt", "r",encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            words.append((line))    
    selected_word = random.choice(words)
    lst = []
    guion = "_"
    blanks = len(selected_word)
    lst.append(guion*blanks)
    lst = "".join(lst)
    lives = 10
    print("Tienes " + str(lives) + " vidas.Buena suerte!")
    print(lst)
    letter = input("Escribe una letra: ")
    letter = letter.lower()

    while letter != selected_word:
        inicio = 0
        final = 1
        for i in selected_word:
            if i == letter:
                lst = lst[:inicio] + letter + lst[final:]
                inicio +=1
                final += 1
            else:
                inicio +=1
                final += 1
                lives = (lives-1)
                continue
        lives = (lives + (blanks-1))
        os.system("cls")
        print("Te quedan " + str(lives) + " vidas")
        if lives == 9:
            print(cuerda)
        if lives == 8:
            print(head)
        if lives == 7:
            print(body)
        if lives == 6:
            print(arm_1)
        if lives == 5:
            print(arm_2)
        if lives == 4:
            print(leg_1)
        if lives == 3:
            print(leg_2)
        if lives == 2:
            print(eye_1)
        if lives == 1:
            print(eye_2)                  
        if lives == 0:
            print(mouth)
            print(lose)
            print("La palabra era " + selected_word + " :(")
            break
        print(lst)
        letter = input("Escribe otra letra: ")
        letter = letter.lower()
    if letter == selected_word:
                print(win)
                print("Muy bienn, la palabra era " + selected_word + " :D")



start="""
    -- -- -- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
    
    Bienvenido al juego del ahorcado
    Escoje S para empezar
    Escoje I para leer las instrucciones 
    Escoje E para salir

    -- -- -- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
"""

def instructions():
    print("""
    -- -- -- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
    
    !!INSTRUCCIONES!!

    El juego del ahorcado es muy sencillo!Se mostraran espacios
    En cada uno de estos espacios va una letra
    Estas letras conforman una palabra que tendras que adivinar
    Solo puedes usar letras, algunas letras llevan tilde y una misma letra puede estar en varios espacios de la palabra

    !!!Si pierdes todas tus vidas seras ahorcado!!!

    -- -- -- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
    """)
    while True:
        volver = input("Pulsa B para volver\n ")
        if volver == "B":
            run()
            break
        else:
            print("Debes ingresar una opcion valida")
            continue
    

    
    
    


menu = """
$$$$$$$$\ $$\        $$$$$$\  $$\                                                    $$\                                        
$$  _____|$$ |      $$  __$$\ $$ |                                                   $$ |                                       
$$ |      $$ |      $$ /  $$ |$$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$\   $$$$$$$ | $$$$$$\         $$$$$$\      $$$$$$\  
$$$$$\    $$ |      $$$$$$$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  _____|\____$$\ $$  __$$ |$$  __$$\       $$  __$$\    $$  __$$\ 
$$  __|   $$ |      $$  __$$ |$$ |  $$ |$$ /  $$ |$$ |  \__|$$ /      $$$$$$$ |$$ /  $$ |$$ /  $$ |      $$$$$$$$ |   $$$$$$$$ |
$$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |      $$   ____|   $$   ____|
$$$$$$$$\ $$ |      $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ |      \$$$$$$$\\$$$$$$$ |\$$$$$$$ |\$$$$$$  |      \$$$$$$$\ $$\\$$$$$$$\ 
\________|\__|      \__|  \__|\__|  \__| \______/ \__|       \_______|\_______| \_______| \______/        \_______|\__|\_______|


                         |/| /¯)
                         |/|/\/
                         |/|\/
                        (¯¯¯)
                        (¯¯¯)
                        (¯¯¯)
                        (¯¯¯)
                        /¯¯/\.
                       / ,^./\.
                      / /   \/\.
                     / /     \/\.
                    ( (       )/)
                    | |       |/|
                    | |       |/|
                    ( (       )/)
                     \ \     / /
                      \ `---' /
                       `-----'


"""
win = """
  _ _ ______       _                     _                            _ _       
 | | |  ____|     | |                   | |                          | | |      
 | | | |__   _ __ | |__   ___  _ __ __ _| |__  _   _  ___ _ __   __ _| | |      
 | | |  __| | '_ \| '_ \ / _ \| '__/ _` | '_ \| | | |/ _ \ '_ \ / _` | | |      
 |_|_| |____| | | | | | | (_) | | | (_| | |_) | |_| |  __/ | | | (_| |_|_|      
 (_|_)______|_| |_|_| |_|\___/|_|  \__,_|_.__/ \__,_|\___|_| |_|\__,_(_|_)
 
                                                 _  
 | |  | |                                       | |        _|  __ \ 
 | |__| | __ _ ___    __ _  __ _ _ __   __ _  __| | ___   (_) |  | |
 |  __  |/ _` / __|  / _` |/ _` | '_ \ / _` |/ _` |/ _ \    | |  | |
 | |  | | (_| \__ \ | (_| | (_| | | | | (_| | (_| | (_) |  _| |__| |
 |_|  |_|\__,_|___/  \__, |\__,_|_| |_|\__,_|\__,_|\___/  (_)_____/ 
                      __/ |                                                     
                     |___/   


"""

lose = """
  _____             _ _     _                 __
 |  __ \           | (_)   | |             _ / /
 | |__) |__ _ __ __| |_ ___| |_ ___       (_) | 
 |  ___/ _ \ '__/ _` | / __| __/ _ \        | | 
 | |  |  __/ | | (_| | \__ \ ||  __/       _| | 
 |_|   \___|_|  \__,_|_|___/\__\___|      (_) | 
                                             \_\
                                               

"""

cuerda = """
  _                                _ 
 | |___ ___ ___ ___ ___ ___ ____ _| |
 | |___|___|___|___|___|___|____|_| |
 | |                              | |
 |_|                              |_|
 | |                             
 | |                                          
 | |                        
 |_|                         
 | |                          
 | |                            
 | |                                    
 |_|                                  
 | |                              
 | |                                   
 | |                                  
 |_|                                  
 | |                                  
 | |                                  
 | |                                  
 |_|                                  
 | |                                  
 | |                                  
 | |                                  
 |_|                              
                                
 
"""
head = """
  _                                _ 
 | |___ ___ ___ ___ ___ ___ ____ _| |
 | |___|___|___|___|___|___|____|_| |
 | |                              | |
 |_|                              |_|
 | |                             *   *  
 | |                          *         *                  
 | |                         *           *
 |_|                         *           *
 | |                          *         *
 | |                             *   *
 | |                                    
 |_|                                  
 | |                              
 | |                                   
 | |                                  
 |_|                                  
 | |                                  
 | |                                  
 | |                                  
 |_|                                  
 | |                                  
 | |                                  
 | |                                  
 |_|                              
          
"""
body = """
  _                                _ 
 | |___ ___ ___ ___ ___ ___ ____ _| |
 | |___|___|___|___|___|___|____|_| |
 | |                              | |
 |_|                              |_|
 | |                             *   *  
 | |                          *         *                  
 | |                         *           *
 |_|                         *           *
 | |                          *         *
 | |                             *   *
 | |                               *     
 |_|                               *   
 | |                               *
 | |                               *   
 | |                               *  
 |_|                               *  
 | |                               *  
 | |                               *  
 | |                               *   
 |_|                                  
 | |                                  
 | |                                  
 | |                                  
 |_|     

"""

arm_1 = """
  _                                _ 
 | |___ ___ ___ ___ ___ ___ ____ _| |
 | |___|___|___|___|___|___|____|_| |
 | |                              | |
 |_|                              |_|
 | |                             *   *  
 | |                          *         *                  
 | |                         *           *
 |_|                         *           *
 | |                          *         *
 | |                             *   *
 | |                               *     
 |_|                             * *   
 | |                           *   *
 | |                         *     *   
 | |                       *       *  
 |_|                               *  
 | |                               *  
 | |                               *  
 | |                               *   
 |_|                                  
 | |                                  
 | |                                  
 | |                                  
 |_|     

"""
arm_2 = """
  _                                _ 
 | |___ ___ ___ ___ ___ ___ ____ _| |
 | |___|___|___|___|___|___|____|_| |
 | |                              | |
 |_|                              |_|
 | |                             *   *  
 | |                          *         *                  
 | |                         *           *
 |_|                         *           *
 | |                          *         *
 | |                             *   *
 | |                               *     
 |_|                             * * *  
 | |                           *   *   *
 | |                         *     *     *
 | |                       *       *       *
 |_|                               *  
 | |                               *  
 | |                               *  
 | |                               *   
 |_|                                  
 | |                                  
 | |                                  
 | |                                  
 |_|     

"""
leg_1 = """
  _                                _ 
 | |___ ___ ___ ___ ___ ___ ____ _| |
 | |___|___|___|___|___|___|____|_| |
 | |                              | |
 |_|                              |_|
 | |                             *   *  
 | |                          *         *                  
 | |                         *           *
 |_|                         *           *
 | |                          *         *
 | |                             *   *
 | |                               *     
 |_|                             * * *  
 | |                           *   *   *
 | |                         *     *     *
 | |                       *       *       *
 |_|                               *  
 | |                               *  
 | |                               *  
 | |                               *   
 |_|                              *    
 | |                             *     
 | |                            *      
 | |                           *       
 |_|                          *

"""
leg_2 = """
  _                                _ 
 | |___ ___ ___ ___ ___ ___ ____ _| |
 | |___|___|___|___|___|___|____|_| |
 | |                              | |
 |_|                              |_|
 | |                             *   *  
 | |                          *         *                  
 | |                         *           *
 |_|                         *           *
 | |                          *         *
 | |                             *   *
 | |                               *     
 |_|                             * * *  
 | |                           *   *   *
 | |                         *     *     *
 | |                       *       *       *
 |_|                               *  
 | |                               *  
 | |                               *  
 | |                               *   
 |_|                              * *  
 | |                             *   *  
 | |                            *     * 
 | |                           *       *
 |_|                          *         *

"""
eye_1 = """
  _                                _ 
 | |___ ___ ___ ___ ___ ___ ____ _| |
 | |___|___|___|___|___|___|____|_| |
 | |                              | |
 |_|                              |_|
 | |                             *   *  
 | |                          * \/      *                  
 | |                         *  /\       *
 |_|                         *           *
 | |                          *         *
 | |                             *   *
 | |                               *     
 |_|                             * * *  
 | |                           *   *   *
 | |                         *     *     *
 | |                       *       *       *
 |_|                               *  
 | |                               *  
 | |                               *  
 | |                               *   
 |_|                              * *  
 | |                             *   *  
 | |                            *     * 
 | |                           *       *
 |_|                          *         *

"""
eye_2 = """
  _                                _ 
 | |___ ___ ___ ___ ___ ___ ____ _| |
 | |___|___|___|___|___|___|____|_| |
 | |                              | |
 |_|                              |_|
 | |                             *   *  
 | |                          * \/   \/ *                  
 | |                         *  /\   /\  *
 |_|                         *           *
 | |                          *         *
 | |                             *   *
 | |                               *     
 |_|                             * * *  
 | |                           *   *   *
 | |                         *     *     *
 | |                       *       *       *
 |_|                               *  
 | |                               *  
 | |                               *  
 | |                               *   
 |_|                              * *  
 | |                             *   *  
 | |                            *     * 
 | |                           *       *
 |_|                          *         *

"""
mouth = """
  _                                _ 
 | |___ ___ ___ ___ ___ ___ ____ _| |
 | |___|___|___|___|___|___|____|_| |
 | |                              | |
 |_|                              |_|
 | |                             *   *  
 | |                          * \/   \/ *                  
 | |                         *  /\   /\  *
 |_|                         *    _ _    *
 | |                          *  /   \  *
 | |                             *   *
 | |                               *     
 |_|                             * * *  
 | |                           *   *   *
 | |                         *     *     *
 | |                       *       *       *
 |_|                               *  
 | |                               *  
 | |                               *  
 | |                               *   
 |_|                              * *  
 | |                             *   *  
 | |                            *     * 
 | |                           *       *
 |_|                          *         *

"""


def run():
    print(menu)
    while True:
            choise = input(start)
            os.system("cls")
            if choise == "S":
                words()
                break
            elif choise == "E":
                print("Gracias por jugar")
                break
            elif choise == "I":
                instructions()
            else:
                print("Debes escoger una opcion valida\n")
                continue
            
    
    


if __name__ == "__main__":
    run()     
        