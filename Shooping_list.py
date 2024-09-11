import os
def Shooping_list(*args):
    if len(*args) > 1:
        for index, product in enumerate(*args):
            print('='*40)
            print(index, product)
            print('='*40)
    elif len(*args) <= 1:
        print('='*40)
        print(*args)
        print('='*40)
shooping = []       
while True:
    option_buy = input('Which do you want?:\n1.Buy a product\n2.See your shooping\n3.Delete a product\n4.End the shooping\n')
    
    if option_buy == '1':
        os.system('cls')
        buy_product = input('What do you buy?: \n')
        shooping.append(buy_product)
    elif option_buy == '2':
        os.system('cls')
        Shooping_list(shooping)
    
    elif option_buy == '3':
        try:    
            if len(shooping) >= 1:
                os.system('cls')
                Shooping_list(shooping)
                option_delete = (input('What do you delete?: \n'))
                if option_delete in shooping:
                    shooping.remove(option_delete)
                
                else:
                    print("This item isn't in the shooping list.")
            elif len(shooping) < 1:
                print("You don't have products.")
        except ValueError:
            print('Invalid value')
            
    
    elif option_buy == '4':
        os.system('cls')
        Shooping_list(shooping)
        print('-'*40)
        print('Thanks for the visit.')
        print('-'*40)
        break
        
    
        