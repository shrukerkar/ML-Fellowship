
s=[{'id': 1, 'success': True, 'name': 'Lary'},
   {'id': 2, 'success': False, 'name': 'Rabi'},
   {'id': 3, 'success': True, 'name': 'Alex'}]

print(sum(d['success'] for d in s))