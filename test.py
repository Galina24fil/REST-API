from requests import get, post, delete, put


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