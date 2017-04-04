class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        
        Initially, no tiles in the room have been cleaned.
        
        width: an integer > 0
        height: an integer > 0
        """        
        self.width = width
        self.height = height
        tiles = {}
        for i in range(width):
            for j in range(height):
                key = (i, j)
                tiles[key] = False
        self.tiles = tiles

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        
        Assumes that POS represents a valid position inside this room.
        
        pos: a Position
        """
        xval = int(pos.x)
        yval = int(pos.y)
        self.tiles[xval, yval] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        
        Assumes that (m, n) represents a valid tile inside the room.
        
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        m = int(m)
        n = int(n)
        if self.tiles[(m, n)]:
            return True
        else:
            return False    
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        
        returns: an integer
        """
        return (self.width * self.height)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.
        
        returns: an integer
        """        
        count = 0
        for each in self.tiles:
            if self.tiles[each] == True:
                count += 1
        return count            

    def getRandomPosition(self):
        """
        Return a random position inside the room.
        
        returns: a Position object.
        """
        xcord = random.randint(0, (self.width-1))
        ycord = random.randint(0, (self.height-1))
        return Position(xcord, ycord)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.
        
        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """        
        if (0 <= pos.x < self.width ) and (0 <= pos.y < self.height):
            return True
        else:
            return False
