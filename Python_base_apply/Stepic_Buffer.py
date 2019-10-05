class Buffer:
    def __init__(self):
        self.spisok = []
    def add(self, *a):
        for i in a:
            self.spisok.append(i)
            if len(self.spisok) ==  5:
                print(sum(self.spisok[:5]))
                self.spisok = []
            
    def get_current_part(self):
        return self.spisok
