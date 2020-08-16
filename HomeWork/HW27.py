class Counter:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.count = 0

    def set_min(self, min_value):
        self.min_value = min_value

    def set_max(self, max_value):
        self.max_value = max_value

    def increase(self):
        if self.count <= self.max_value:
            self.count += 1

    def get_current_value(self):
        self.count
