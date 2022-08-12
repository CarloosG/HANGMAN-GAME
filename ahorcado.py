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
    lst = print("".join(lst))
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
    words()
    print("ENHORABUENA! HAS GANADO :D")


if __name__ == "__main__":
    run()     
        