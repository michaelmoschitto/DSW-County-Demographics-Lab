import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for c in counties:
        if c["County"] < first:
            first = c["County"]
    return first


def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    highest = counties[0]["Age"]["Percent Under 18 Years"]
    county = counties[0]["County"]
    state = counties[0]["State"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highest:
            highest = c["Age"]["Percent Under 18 Years"]
            county = c["County"]
            state = c["State"]
    return county, state



def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    highest = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highest:
            highest = c["Age"]["Percent Under 18 Years"]
    return str(highest) + " Percent"




def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    list = [counties[0]["County"],counties[0]["State"],counties[0]["Age"]["Percent Under 18 Years"]]
    highest = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highest:
            list[0] = c["County"]
            list[1] = c["State"]
            list[2] = c["Age"]["Percent Under 18 Years"]
            highest = c["Age"]["Percent Under 18 Years"]
    return list

def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    #Find the state in the dictionary with the most counties
    #Return the state with the most counties
    dict = {}
    highest = 0
    state = ""
    for c in counties:
        if c["State"] not in dict:
            dict[c["State"]] = 1
        else:
            dict[c["State"]] += 1
    for stateN,num in dict.items():
        if num > highest:
            highest = num
            state = stateN
    return state + " " + str(highest)


def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    list = []
    for c in counties:
        list.append(c["Income"]["Per Capita Income"])
    return "The average Percapita Income is " + str(sum(list)/len(list))
if __name__ == '__main__':
    main()
