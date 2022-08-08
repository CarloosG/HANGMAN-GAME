import random


def words():
    word=[]
    with open(r"C:\Users\ADMIN\Desktop\PLATZI\CURSO_INTERMEDIO_PYTHON\final_project\data.txt", "r",encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            word.append((line))     #tengo que solucionar el problema de que las palabras las guarda con un \n
    print(word)        
    # pala = random.choice(word)
    # letter = input("Escribe una letra: ")
    # while letter != pala:
    #     if letter in pala:
    #         print(letter)
    #         letter = input("Bien!, Escoje otra letra: ")
    #     else:
    #         letter = input("Escoje otra letra: ")
    

        
def run():
    words()


if __name__ == "__main__":
    run()     
        