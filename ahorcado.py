import random


def words():
    word=[]
    with open(r"C:\Users\ADMIN\Desktop\PLATZI\CURSO_INTERMEDIO_PYTHON\final_project\data.txt", "r",encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            word.append((line))    
         
    # pala = random.choice(word)
    pala = "solución"
    lst = []
    guion = "_"
    spaces = len(pala)
    lst.append(guion*spaces)
    lst = "".join(lst)
    vidas = 15
    print("Tienes " + str(vidas) + " vidas.Buenas suerte!")
    print(lst)
    letter = input("Escribe una letra: ")

    while letter != pala:
        inicio = 0
        final = 1
        for i in pala:
            if i == letter:
                lst = lst[:inicio] + letter + lst[final:]
                inicio +=1
                final += 1
            else:
                inicio +=1
                final += 1
                continue
        vidas = vidas-1
        print("Te quedan " + str(vidas) + " vidas")
        if vidas == 0:
            print(lose)
            print("La palabra era " + pala + " :(")
            break
        print(lst)
        letter = input("Escribe otra letra: ")
    if letter == pala:
                print(win)
                print("Muy bienn, la palabra era " + pala + " :D")



def instrucciones():
    print("""
    -- -- -- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
    
    !!INSTRUCCIONES!!

    El juego del ahorcado es muy sencillo!Se mostraran espacios
    En cada uno de estos espacios va una letra
    Estas letras conforman una palabra que tendras que adivinar
    Solo puedes usar letras y una misma letra puede estar en varios espacios de la palabra

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
 
                                                                        ____  
 | |  | |                                                   | |        _|  __ \ 
 | |__| | __ _ ___    __ _  __ _ _ __   __ _ _ __   __ _  __| | ___   (_) |  | |
 |  __  |/ _` / __|  / _` |/ _` | '_ \ / _` | '_ \ / _` |/ _` |/ _ \    | |  | |
 | |  | | (_| \__ \ | (_| | (_| | | | | (_| | | | | (_| | (_| | (_) |  _| |__| |
 |_|  |_|\__,_|___/  \__, |\__,_|_| |_|\__,_|_| |_|\__,_|\__,_|\___/  (_)_____/ 
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
  _                                    
 | |                                   
 | |______ ______ ______ ______ ______ 
 | |______|______|______|______|______|
 | |                                   
 | |                                   
 | |                                   
 |_|                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 |_|                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 |_|                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 |_|                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 | |                                   
 
"""
head = """
        *  *            
     *        *            
    *          *           
    *          *             
     *        *             
        *  *      
"""




def run():
    print(menu)
    while True:
            choise = input("Bienvenido al juego del ahorcado\n Escoje S para empezar\n Escoje I para leer las instrucciones \n Escoje E para salir\n ")
            if choise == "S":
                words()
                break
            elif choise == "E":
                print("Thanks for playing")
                break
            elif choise == "I":
                instrucciones()
            else:
                print("Debes escoger una opcion valida\n")
                continue
            
    
    


if __name__ == "__main__":
    run()     
        