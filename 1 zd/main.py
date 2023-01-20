import random  
minChoice = int(input("Введите мин: "))
maxChoice = int(input("Введите макс: "))
NumberToGuess=random.randrange(minChoice,maxChoice)  
forHelp = random.randint(1,3)
help1 = NumberToGuess+forHelp
help2=NumberToGuess-forHelp
help3 = NumberToGuess+forHelp+1
helps = ''
userGuess = 0
tryScore=0
print(NumberToGuess)

while userGuess != NumberToGuess:
    userGuess=int(input("Угадай число: " ))   
    tryScore=tryScore+1
    if userGuess > NumberToGuess:   
        print("Число должно быть меньше!Попыток:",tryScore)

        if tryScore>7:
            print("Ты лох!")
            break     
    elif userGuess< NumberToGuess-5:{ 
       print("Подсказка число больше чем:",help2)}      
    elif userGuess<NumberToGuess-7:{
        print('hui')
    }
   
    
    elif userGuess < NumberToGuess:       
        print("Число должно быть больше!Попыток",tryScore) 
        if tryScore>7:
            print("Ты лох!")
            break
    elif userGuess>NumberToGuess+6:
        print("Подскахка: число меньше чем:",help3) 
    
    elif userGuess>NumberToGuess+8:
        print("Подскахка: число меньше чем:",help1) 

    elif userGuess == NumberToGuess:      
        print("Вы угадали, это число = " , NumberToGuess,'Понадобилось попыток:',tryScore)
        nextTry= input("Еще играем? д/н")
        if nextTry == 'д':
            print()
        else:
            break
    
