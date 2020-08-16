class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        for elem in a:
            self.buffer.append(elem)
            if len(self.buffer) == 5:
                print(self.buffer)
                self.buffer = []

    def get_current_part(self):
        return self.buffer
