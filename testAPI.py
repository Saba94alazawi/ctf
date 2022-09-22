import requests
from requests.auth import HTTPBasicAuth
import random
import time
from sendingData import dataSend
from checkConnectivity import connecting



# tokens = ['2b2ed22eb6f18aa723067f1d9bc387452d552740','d156f58a2f860a195f4702b79a0a24687023a81e','e7a053feb7de1daf5d27cdc2bf5b946f878988aa','9eb601151f17858acfc206e41b9e7935db7dd598']
# devices = ['8f17f84e-efb6-4732-a6b6-73ba411640e2','e0ccbc3c-d8b1-413e-968b-025a1b6013e5','b2256692-0ac7-482f-99b3-69d599910eae']

users = [('adminF', 'ctf12345'),
        ('aliali', '1qw23er45t'),
        ('basim90', '1qw23er45t'),
        ('mahaali', '1qw23er45t')]

# print(users[1][0])


# for i in range(20):
#     data = {
#         "Latitude": '',
#         "Longitude": '',
#         "speed": 0,
#         "fine": 0,
#         "deviceID": ''
#     }
#     speeds = random.randint(50,100)
#     fines = random.randint(20,80)
#     if speeds >=70:
#         # randToken = random.choice(tokens)
#         randDevices = random.randint(1,3)
#         randUsers = random.choice(users)
#         # randDevices = random.choice(devices)
#         randLat = round(random.uniform(33.36000, 33.46000), 6)
#         randLon = round(random.uniform(44.360000, 44.46000), 6)

#         data['Latitude'] = randLat
#         data['Longitude'] = randLon
#         data['speed'] = speeds
#         data['fine'] = fines
#         # data['deviceID'] = randDevices

#         # access_token = randToken
#         # HTTPBasicAuth('aliali', '1qw23er45t')
#         # header = {'Authorization' : ''}
#         # header['Authorization'] = 'Bearer '+ randToken
#         # auths = 'HTTPBasicAuth('+randUsers[0]+','+randUsers[1]+')'
#         # r = requests.post(url=url, headers=header, data=data)



#         url = 'http://127.0.0.1:8000/fine/'
#         r = requests.post(url=url, auth=HTTPBasicAuth('aliali', '1qw23er45t'), data=data)
#         print(data)
#         print('SENT')
#         time.sleep(3)
# print('DONE')


connecting


num = 1

data = {
        "Latitude": '',
        "Longitude": '',
        "speed": 0,
        "fine": 0,
    }

def checkSpeed(speed, num):
        if speed > 80 and num == 3:
            print(f'You got a ticket speed!!')
            return 'Bad'
        elif speed > 80 and num < 3:
            print(f'{speed} KM/H is over limit, slow down!!!')
            print(f'This is your {num} warning')
            return 'Good'
        else:
            return 'All good!!'



connecting(users[1][0],users[1][1])

for i in range(10):

    speeds = random.randint(50,150)
    fines = random.randint(50,150)
    randLat = round(random.uniform(33.36000, 33.46000), 6)
    randLon = round(random.uniform(44.360000, 44.46000), 6)
    
    data['Latitude'] = randLat
    data['Longitude'] = randLon
    data['speed'] = speeds
    data['fine'] = fines

    print(speeds)
    time.sleep(3)
    checking = checkSpeed(speeds, num)
    
    
    print('num=',num)
    if checking == 'Good':
        num += 1
    elif checking == 'Bad':
        dataSend(users[1][0],users[1][1],data)
        print(data)
        num = 1
        data = {
                "Latitude": '',
                "Longitude": '',
                "speed": 0,
                "fine": 0,
                }
    print(checking)







