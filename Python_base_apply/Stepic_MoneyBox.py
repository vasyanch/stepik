class MoneyBox:
    def __init__(self, capacity, quantity=0):
        self.capacity = capacity
        self.quantity = quantity
    def add(self, v):
        self.quantity += v
    def can_add(self, v):
        if (self.quantity + v) <= self.capacity:
            return True
        else:
            return False 
