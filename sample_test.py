import requests

# Register
response = requests.post('http://localhost:8000/api/auth/register/', json={
    'username': 'testuser',
    'password': 'testpass123',
    'email': 'test@example.com'
})
token = response.json()['token']

# Create workout
headers = {'Authorization': f'Token {token}'}
workout = {
    'workout_type': 'running',
    'title': 'Evening Run',
    'start_time': '2024-01-15T18:00:00Z',
    'end_time': '2024-01-15T18:30:00Z',
    'total_distance': 4.0,
    'total_calories': 350
}
response = requests.post('http://localhost:8000/api/workouts/', 
                        json=workout, headers=headers)
print(response.json())

# Get statistics
response = requests.get('http://localhost:8000/api/workouts/statistics/',
                       headers=headers)
print(response.json())