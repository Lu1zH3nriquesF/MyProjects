import os
game_list = {'Minecraft': 210, 'Subnautica': 62, 'Terraria': 173}

buy = input('Would you like buy a game?: [Y]es / [N]o \n').upper()

game_buying = []
price = 0
while buy == 'Y':
    
    for game, game_value in game_list.items():
        print(f'{game}: {game_value}')
    
    choice_game = str(input('Which the game will do you buy: \n').capitalize())
    n = game_buying.append(choice_game)
    if choice_game in game_list:
        print(f'{choice_game}: {game_list[choice_game]}')
        continue_shopping = input('Do you continue with the purchase?: [Y]es / [N]o \n').upper()
        if continue_shopping == 'Y':
            price += game_list[choice_game]
            print(f'Games in your cart: {game_buying} {price}')
            
            buy = input('Do you continue shopping?: [Y]es / [N]o \n').upper()
            os.system('cls')
        else:
            print('Thanks for the visit.')
            break
    
    else:
        print('Select a game in the list.')

else:
    print(f'Your purchase: {game_buying}')
    print(f'Total value: {price}')
    print('Goodbye, thanks for the visit.')
        


