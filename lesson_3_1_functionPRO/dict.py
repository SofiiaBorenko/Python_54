books = {
    'Lev Tolstoy': 'Anna Karenina',
    'anton Chekhov': 'the Cherry Orchard'
}

books2 ={
    "Lev Tolstoy",
        'Anna Karenina'
}
print(books2)

response ={
    'statusCode':'200',
    'user':{
        "id":1,
        "name":"Sofia"
    }
}
print(response['user']["name"])

data =[1,2,33]
print(isinstance(data,list))

value = 22.4
print(isinstance(value,int))

value = 22
print(isinstance(value,int))

value = 22.0
print(isinstance(value,int))

team_ages ={
    'Sofia':21,
    "Vadim":24,
    "Tatiana":54,
    "Andrey":44,
    "Vladimir":65,
}
print(team_ages.keys())
print(team_ages.values())

team_names =  'Sofia',"Vadim","Tatiana","Andrey","Vladimir"
team_num =[21,24,54,44,65]
team_ages = {name:age for  name,age in zip(team_names,team_num)}
print(team_ages)




