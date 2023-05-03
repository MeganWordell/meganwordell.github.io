import csv

# Read the county distances from the CSV file
county_distances = []
with open('county_distances.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        county_distances.append(row)

# Get the current location from user input
county_name = input("Enter county: ")
state = input("Enter state abbreviation: ")

# Find the distance to the store for the current county
distance_to_store = None
for county in county_distances:
    if county['\ufeffCounty'] == county_name:
        distance_to_store = float(county['Distance'])
        break

# Display the distance to the store, or "none" if not found
if distance_to_store is not None:
    print("The closest abortion-providing clinic from {} county is {} miles away".format(county_name, distance_to_store))
else:
    print("Distance to store from {} county: none".format(county_name))
