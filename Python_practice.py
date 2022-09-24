from turtle import clear
from winsound import PlaySound


print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])



counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else: 
    print("El Paso is not the list of counties.")
clear
if"Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
counties = "El Paso"
clear

for county in counties_dict.keys():
    print(county)
voting_data = [{"counties":"Arapahoe","registered_voters":422829},
                {"countty":"Denver","registered_voters":463353}
                {"county":"Jefferson","registered_voters":432438}]
for county_dict in voting_data:
    print(county_dict)
     

