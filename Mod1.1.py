#my-variable = "Alan"
#_variable = "Alan"
#2nd_variable = "Two"
#variable__5 = "Five"

#print(my-variable)
#print(_variable)
#print(2nd_variable)
#print(variable__5)

#list = [1,2,1,3,2]
#list.remove(2)
#print(list)

#favourite_fruits = {}
#favourite_fruits['Alex']='Apple'
#favourite_fruits['Alex']='Satsuma'
#print(favourite_fruits)

#favourite_colours={'Alice':'Purple','Bob':'Green','Charlie':'Scarlet'}
#del favourite_colours['Green']
#print(favourite_colours)


#def run_apple_guessing_game(target):
#    while True:
#        guess = int(input('Guess How Many Apples I Have!'))
#        if guess < target:
#            print('Too Few!')
#            continue
#        elif guess > target: 
#            print('Too Many!')
#            continue
#        else:
#            print('You\'re Right!')
#            return
#run_apple_guessing_game(5)           

#list = ['fourteen','fifteen',16,'seventeen']
#for item in list:
#    try:
#        msg = 'processing ' + item
#        print(msg)
#        continue
#    except TypeError:
#        print('something went wrong!')
#        break
#    finally:
#        print('finally block')
#    print('next item please!')    

#def format_string(msg, prefix='String: ', postfix) -> int:
#    print(prefix + msg + postfix)
#format_string('hello', postfix=".")

bool = not False and False or not 1 == 0
print(bool)
bool = (((not False) and False) or (not 1)) == 0
print(bool)