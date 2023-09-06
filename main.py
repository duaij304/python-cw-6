# write your code here

person={
    'name':'Duaij',
    'age':'17',
    'hobbies':['Programing','Pentration testing','football']
}
print(person['name'])
print(person['age'])

person['age']=17
person['country']='Kuwait'
print(person)
print(len(person))

person['hobbies'].append('reading')

def check_hobby(person):
    if len(person['hobbies']) >= 3:
        print('WOW you are amazing!')

check_hobby(person)