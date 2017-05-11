def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)    
    """
    viruses = list(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses))
    totalv = [0] * 300
    resisv = [0] * 300

    for i in range(numTrials):
        patient = TreatedPatient(viruses, maxPop)

        for i in range(0,150):
            patient.update()
            totalv[i] += (patient.getResistPop([]))
            resisv[i] += (patient.getResistPop(['guttagonol']))

        patient.addPrescription('guttagonol')

        for i in range(150,300):
            patient.update()
            totalv[i] += (patient.getResistPop([]))
            resisv[i] += (patient.getResistPop(['guttagonol']))

    for i in range(300):
        totalv[i] = totalv[i] / (numTrials)
        resisv[i] = resisv[i] / (numTrials)

    pylab.plot(totalv, label = 'Virus Population')
    pylab.plot(resisv, label = 'Resistant Virus Vopulation')
    pylab.title('Simulation Without Drug')
    pylab.xlabel('Timestep')
    pylab.ylabel('Virus Population')
    pylab.legend(loc='best')
    
    pylab.show()

simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
