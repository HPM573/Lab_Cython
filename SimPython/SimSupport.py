

class Ave:

    def __init__(self, data):
        self.data = data

    def get_ave(self):
        return sum(self.data)/len(self.data)
