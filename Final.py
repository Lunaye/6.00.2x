# Problem 3

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    success = 0
    for i in range(numTrials):
        bucket = ['red', 'blue']*4
        drawn = []
        b = 5        
        for i in range(3):
            ind = random.randint(0,b)
            drawn.append(bucket[ind])
            del bucket[ind]
            b -= 1
               
        if all(x == drawn[0] for x in drawn):
            success += 1

    return (success/numTrials)

# Problem 8

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    
    for i in range(CURRENTRABBITPOP):

        prob_rep = 1.0 - (CURRENTRABBITPOP / float(MAXRABBITPOP))

        if random.random() <= prob_rep and CURRENTRABBITPOP < MAXRABBITPOP:
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for i in range(CURRENTFOXPOP):
        prob_eat =  CURRENTRABBITPOP/MAXRABBITPOP        

        if random.random() <= prob_eat and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() < (1/3):
                CURRENTFOXPOP += 1
        else:
            if random.random() <= 0.1:
                CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    global MAXRABBITPOP
    
    rabbit_populations = []
    fox_populations = []

    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)

    #pylab.plot(rabbit_populations, label='Rabbit Population')
    #pylab.plot(fox_populations, label='Fox Population')
    #pylab.legend()
    #pylab.show()

    return((rabbit_populations, fox_populations))

      
        
