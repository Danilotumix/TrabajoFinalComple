class City:
    def __init__(self):
	    self.connections = []
    
    def addConnection(self, pair):
        for p in self.connections:
            if p.city == pair.city:
                return
        
        self.connections.append(pair)