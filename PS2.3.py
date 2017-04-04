class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        pos = self.getRobotPosition()

        new_pos = pos.getNewPosition(self.direction, self.speed)

        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(new_pos)
        else:
            self.direction = random.randint(0, 360)
