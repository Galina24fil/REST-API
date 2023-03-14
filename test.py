from requests import get, post, delete

#первое тестирование
print(get('http://localhost:5000/api/jobs').json())

print(get('http://localhost:5000/api/jobs/1').json())

print(get('http://localhost:5000/api/jobs/100').json())

print(get('http://localhost:5000/api/jobs/q').json())

# post запрос
print(post('http://localhost:5000/api/jobs', json={}).json()) # пустой запрос

print(post('http://localhost:5000/api/jobs',
           json={'job': 'Заголовок'}).json()) # неправильный запрос, в кот недостаточно переменных в json

print(post('http://localhost:5000/api/jobs', # запрос на добавление с уже добавленным id
           json={'id': 2,
                 'team_leader': 1,
                 'job': 'Заголовок',
                 'work_size': 1,
                 'collaborators': '1, 2',
                 'is_finished': False}).json())

print(post('http://localhost:5000/api/jobs',  # верный запрос
           json={'id': 20,
                 'team_leader': 1,
                 'job': 'Заголовок',
                 'work_size': 1,
                 'collaborators': '1, 2',
                 'is_finished': False}).json())

print(get('http://localhost:5000/api/jobs').json()) #запись добавилась

#удаление
print(post('http://localhost:5000/api/jobs',  # верный запрос
           json={'id': 20,
                 'team_leader': 1,
                 'job': 'Заголовок',
                 'work_size': 1,
                 'collaborators': '1, 2',
                 'is_finished': False}).json())

print(get('http://localhost:5000/api/jobs').json()) #запись добавилась

print(delete('http://localhost:5000/api/jobs/20').json()) # правильное удаление

print(get('http://localhost:5000/api/jobs').json()) #запись удалилась

print(delete('http://localhost:5000/api/jobs/999').json()) # такой записи нет

print(delete('http://localhost:5000/api/jobs/q').json()) # передано не int

# редактированрие
print(post('http://localhost:5000/api/jobs',  # верный запрос
           json={'id': 20,
                 'team_leader': 1,
                 'job': 'Заголовок',
                 'work_size': 1,
                 'collaborators': '1, 2',
                 'is_finished': False}).json())

print(get('http://localhost:5000/api/jobs/20').json()) #запись добавилась

print(post('http://localhost:5000/api/jobs/20',
          json={'id': 20,
                 'team_leader': 2,
                 'job': 'Заголовок1',
                 'work_size': 1,
                 'collaborators': '1, 2',
                 'is_finished': False}).json())

print(get('http://localhost:5000/api/jobs/20').json()) #запись изменилась

print(post('http://localhost:5000/api/jobs/20', json={}).json()) # пустой запрос
print(post('http://localhost:5000/api/jobs/20', json={'job': 'Заголовок1'}).json()) # недостаточно переменных
print(post('http://localhost:5000/api/jobs/999', json={'job': 'Заголовок1'}).json()) # не существующий id
