def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    pop = [0] * 300
    for i in range(numTrials):

        viri = []
        for i in range(numViruses):
            viri.append( SimpleVirus(maxBirthProb, clearProb) )
        
        patient = Patient(viri, maxPop)
        for i in range(1,301):
            patient.update()
            pop[i-1] += (patient.getTotalPop())

    population = [i/numTrials for i in pop]

    pylab.plot(population)
    pylab.title('Simulation Without Drug')
    pylab.xlabel('Timestep')
    pylab.ylabel('Virus Population')
    
    pylab.show()
