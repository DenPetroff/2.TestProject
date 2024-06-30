import csv
from geopy.distance import geodesic as GD


def dist(zipcode1, zipcode2):
    city1 = ()
    city2 = ()
    with open('zip_codes_states.csv', mode='r') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            if zipcode1 == row['zip_code']:
                city1 = (float(row['latitude']), float(row['longitude']))
            elif zipcode2 == row['zip_code']:
                city2 = (float(row['latitude']), float(row['longitude']))
            distance = GD(city1, city2).miles
        print(f'The distance between {zipcode1} and {zipcode2} is {distance:.2f} miles')


def zip(city, state):
    zip_cd = []
    with open('zip_codes_states.csv', mode='r') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            if row["state"] == state and row["city"] == city:
                zip_cd.append(row['zip_code'])
    print('The following ZIP Code(s) found for', city, state, zip_cd)


def loc(code):
    with open('zip_codes_states.csv', mode='r') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            if row["zip_code"] == code:
                print('Zip Code:', row['zip_code'], 'is in', row['city'], row['state'], row['county'])
                print('coordinates:', (row['longitude'], 'N', row['latitude'], 'W'))


def main():
    command = input('Command (loc, zip, dist, end): ').lower()
    while True:
        if command == 'end':
            print('Done')
            break

        elif command == 'loc':
            code = input('Enter a ZIP Code to lookup: ')
            loc(code)

        elif command == 'zip':
            city = input('Enter a city name to lookup: ').lower()
            state = input('Enter the state name to lookup: ').lower()
            zip(city, state)

        elif command == 'dist':
            zipcode1 = input('Enter the first ZIP Code: ')
            zipcode2 = input('Enter the second ZIP Code: ')
            dist(zipcode1, zipcode2)

        else:
            print('Invalid command, ignoring')
            break


# code = input('Enter a ZIP Code to lookup: ')
if __name__ == '__main__':
    main()
