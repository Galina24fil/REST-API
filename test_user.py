from requests import get, post, delete

print(get('http://localhost:5000/api/users').json())
print(get('http://localhost:5000/api/users/5').json())
#print(delete('http://localhost:5000/api/users/1').json())
print(post('http://localhost:5000/api/users/5',
           json={'id': 5,
            'surname': 'Фамилия',
            'name': 'name',
            'age': 2,
            'position': 'position',
            'speciality': 'speciality',
            'address': 'address',
            'email': 'email5@email',
            'password': 'Qazqwer5'}).json())

print(get('http://localhost:5000/api/users').json())

print(get('http://localhost:5000/api/jobs').json())