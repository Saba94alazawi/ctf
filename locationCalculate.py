import random
import json
from pathlib import Path
from addedStreets import addedCoordinates


# Calculate the orginal line #

A = True
i = 0

try:
    while True:

        print('''
                1: Add/Update street dataset.
                2: Monitoring the speed.
                3: Quit the program.
            ''')

        choosen = input('What do you want to do:')

        if choosen == '1':
            if not Path('coordinates.json').is_file():
                        with open('coordinates.json', 'w') as coords:

                            while A:
                                i+=1
                                print('Give the street coordinates\n')
                                Xa = float(input('Give me the start X: '))
                                Ya = float(input('Give me the start Y: '))
                                Xb = float(input('Give me the end X: '))
                                Yb = float(input('Give me the end Y: '))
                                speed = int(input('Give the limit speed:'))
                                fine = int(input('Insert the fine amount:'))

                                # Xa = round(random.uniform(33.36000, 33.46000), 6)
                                # Ya = round(random.uniform(44.360000, 44.46000), 6)
                                # Xb = round(random.uniform(33.36000, 33.46000), 6)
                                # Yb = round(random.uniform(44.360000, 44.46000), 6)

                                info = addedCoordinates(Xa,Ya,Xb,Yb,speed,fine,i)

                                c = input('Do you want to added more (y) or (n)? ')
                                if c == 'No' or c == 'N' or c == 'n':
                                    A = False
                                    json.dump(info, coords)
                        coords.close()

            else:
                with open('coordinates.json', 'r') as coordsUpdate:
                    update = json.load(coordsUpdate)
                    i = update[-1]['id']
                    coordsUpdate.close()

                    

                    while A:
                        i+=1
                        print('Give the street coordinates\n')
                        Xa = float(input('Give me the start X: '))
                        Ya = float(input('Give me the start Y: '))
                        Xb = float(input('Give me the end X: '))
                        Yb = float(input('Give me the end Y: '))
                        speed = int(input('Give the limit speed:'))
                        fine = int(input('Insert the fine amount:'))

                        # Xa = round(random.uniform(33.36000, 33.46000), 6)
                        # Ya = round(random.uniform(44.360000, 44.46000), 6)
                        # Xb = round(random.uniform(33.36000, 33.46000), 6)
                        # Yb = round(random.uniform(44.360000, 44.46000), 6)

                        info = addedCoordinates(Xa,Ya,Xb,Yb,speed,fine,i)

                        c = input('Do you want to added more (y) or (n)? ')
                        if c == 'No' or c == 'N' or c == 'n':
                            A = False
                            for new in info:
                                update.append(new)

                            with open('coordinates.json', 'w') as coords:
                                json.dump(update, coords)
                    coords.close()

        elif choosen == '2':

            ########################################################

            # Check if the coordinates inside the line #

            lst = []

            X = float(input('Give me the X: '))
            Y = float(input('Give me the Y: '))

            # X = round(random.uniform(33.36000, 33.46000), 6)
            # Y = round(random.uniform(44.360000, 44.46000), 6)

            with open('coordinates.json', 'r') as street:
                contents = json.load(street)


            for d in contents:
                if (X >= d['xA'] or Y >= d['yA']) or (X <= d['xB'] and Y <= d['yB']) or (X <= d['xA'] or Y <= d['yA']) or (X >= d['xB'] and Y >= d['yB']):
                    point = Y - d['Slope'] * X - d['Shift']
                    z = [d['id'], abs(point)]
                    lst.append(z)

            closeset = min(lst, key=lambda x: x[1])
            print(closeset)

            for line in contents:
                if closeset[0] == line['id']:
                    print(line)
        
        elif choosen == '3':
            break
        
        else:
            print('Please, Choose (1) or (2)')
            continue

except ValueError:
        pass
        
        






