import random


def words():
    word=[]
    with open(r"C:\Users\ADMIN\Desktop\PLATZI\CURSO_INTERMEDIO_PYTHON\final_project\data.txt", "r",encoding="utf-8") as f:
        for line in f:
            word.append(str(line))
            
    pala = random.choice(word)
    
    print(pala)
        
def run():
    words()


if __name__ == "__main__":
    run()     
        