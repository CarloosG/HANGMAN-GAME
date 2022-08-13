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
        print(lst)
        letter = input("Escibre otra letra: ")
    
    print(pala)


def instrucciones():
    print("""
    El juego del ahorcado es muy sencillo!Se mostraran espacios
    En cada uno de estos espacios va una letra
    Estas letras conforman una palabra que tendras que adivinar
    Solo puedes usar letras y una misma letra puede estar en varios espacios de la palabra

    !!!Si pierdes todas tus vidas seras ahorcado!!!
    """)
    volver = input("Pulsa B para volver\n Pulsa E para salir ")
    while True:
        if volver == "B":
            run()
        elif volver == "E":
            print("Thanks for playing")
        else:
            print("Debes ingresar una opcion valida")
    

    
    
    


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
      
def run():
    print(menu)
    choise = input("Bienvenido al juego del ahorcado\n Escoje S para empezar\n Escoje I para leer las instrucciones \n Escoje E para salir ")
    while True:
        if choise == "S":
            words()
            print("ENHORABUENA! HAS GANADO :D")
        elif choise == "E":
            print("Thanks for playing")
        elif choise == "I":
            instrucciones()
        else:
            print("Debes escoger una opcion valida")
    
    


if __name__ == "__main__":
    run()     
        