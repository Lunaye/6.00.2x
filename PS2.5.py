class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        pos = self.getRobotPosition()

        new_pos = pos.getNewPosition(self.direction, self.speed)

        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(new_pos)
            self.direction = random.randint(0,360)
        else:
            self.direction = random.randint(0, 360)

