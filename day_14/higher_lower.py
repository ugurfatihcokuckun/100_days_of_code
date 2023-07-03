from game_data import data
import random
from art import logo, vs
import os   #os.system('cls')

def chech_follower():
    if data_2_4 > data_1_4:
        return data_2_4
    elif data_1_4 > data_2_4:
        return data_1_4

end_of_game = True
score = 0
while end_of_game:
    print(logo)
    data_rand_1 = random.randint(0,49)
    data_rand_2 = random.randint(0,49)

    data_1_1 = data[data_rand_1]["name"]
    data_1_2 = data[data_rand_1]["description"]
    data_1_3 = data[data_rand_1]["country"]
    data_1_4 = data[data_rand_1]["follower_count"]

    data_2_1 = data[data_rand_2]["name"]
    data_2_2 = data[data_rand_2]["description"]
    data_2_3 = data[data_rand_2]["country"]
    data_2_4 = data[data_rand_2]["follower_count"]

    A =print(f"Compare A: {data_1_1}, {data_1_2} from {data_1_3} ")
    print(vs)
    B = print(f"Compare A: {data_2_1}, {data_2_2} from {data_2_3} ")

    chose =  input("Chose 'a' or 'b': ")

    if chose == 'a':
        if chech_follower() == data_1_4:
            os.system('cls')
            score += 1
            print(f"You win your score is {score}")
            
        else:
            os.system('cls')
            print("You lose")
            end_of_game = False
            print(f"score {score}")
            
    if chose == 'b':
        if chech_follower() == data_2_4:
            os.system('cls')
            score += 1
            print(f"You win your score is {score}")
            
        else:
            os.system('cls')
            print("You lose")
            end_of_game = False
            print(f"score {score} ")
            

