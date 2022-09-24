voting_data = [{"counties":"Arapahoe","registered_voters":422829},
                {"countty":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}]
for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dic.values():
        print(value)    
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
message_to_candidate = (
    f"{county} county has {voters:,} registered voters")

