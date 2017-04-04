def greedy_cow_transport(cows, limit):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    vallist = sorted(cows.values(), reverse=True)
    namelist = sorted(cows, key=cows.get, reverse=True)
    
    def get_trip(namelist, vallist, limit): 

        current_lim = limit 
        current_trip = []
        pointer = 0

        while pointer < len(namelist):
            
            if (current_lim - vallist[pointer]) >= 0:
                current_trip.append(namelist[pointer])
                current_lim -= vallist[pointer]
            else:
                pass

            pointer += 1
            
        for each in current_trip:
            
            delindex = namelist.index(each)
            del vallist[delindex]
            del namelist[delindex]
        
        return current_trip
    
    alltrips = []    

    while len(namelist) != 0:
        alltrips.append(get_trip(namelist, vallist, limit))

    return alltrips          

#cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
#should return --> [["Jesse", "Maybel"], ["Maggie", "Callie"]]
#print (greedy_algorithm(cows, 10))    

