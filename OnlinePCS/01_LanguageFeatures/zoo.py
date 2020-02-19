animals = {        
    'Question' : 'Does it live on land?',
    'No' : 'Fish',
    'Yes' : {
        'Question': 'Does it fly?',
        'Yes' : 'Bird',
        'No' : 'Cow'
        }    
}

def getYesNo(prompt):
    ret = input(prompt).capitalize()[0]
    if ret=='Y':
        return 'Yes'
    return 'No'

node = animals
while True:
    ans = getYesNo(node['Question']+' ')
    
    next_node = node[ans]
            
    if type(next_node) is not str:
        node = next_node
        continue    
    
    got_it = getYesNo('Is it a '+next_node+'? ')
    
    if got_it == 'Yes':
        print("Let's play again.")
        node = animals
        continue
    
    print('You stumped me.')
    new_animal = input('What were you thinking of? ')
    new_ques = input('Give me a question to separate '+next_node+' from '+new_animal+': ')
    yn = getYesNo('And what would the Y/N answer be for '+new_animal+'? ')
    
    new_node = {'Question':new_ques}    
    if yn=='Yes':
        new_node['Yes'] = new_animal
        new_node['No'] = next_node
    else:
        new_node['Yes'] = next_node
        new_node['No'] = new_animal
     
    node[ans] = new_node    
   
    print('Let\'s play again.')
    node = animals 
    