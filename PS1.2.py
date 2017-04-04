# Helper functions provided:                

def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

def brute_force_cow_transport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    partitionsList = []
    for partitions in get_partitions(cows):
        partitionsList.append(partitions)

    orderedPartitions = sorted(partitionsList, key= len) # Order partitions by number of subsets

    namelist = sorted(cows, key=cows.get, reverse=True)
    total = 0

    for partition in orderedPartitions: 

        total = 0
        lists = len(partition)
        trip = True
        weightlist = []

        for list in partition: 

            total = 0

            for i in list: 
                val = cows[i] 
                total += val 
                
            weightlist.append(total)


        valid = True
        for each in weightlist:
            if each > limit:
                valid = False

        if valid == True:
            return partition            
        
# cows = {'Lotus': 40, 'Milkshake': 40, 'MooMoo': 50, 'Boo': 20, 'Miss Bella': 25, 'Horns': 25}
# print(brute_force_cow_transport(cows, 100))
# Should return --> [['Milkshake', 'Lotus', 'Boo'], ['Miss Bella', 'Horns', 'MooMoo']]

            
