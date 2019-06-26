class Pair:
    def __init__(self, city, weight):
	    self.city = city
	    self.weight = weight
    
    def __lt__(self, other):
        return self.weight < other.weight