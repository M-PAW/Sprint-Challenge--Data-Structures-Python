class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_index = 0
        self.buffer =[]

    def append(self, item):
        # if self.current_index > self.capacity:
        #     if not self.buffer[self.current_index]:
        #         self.buffer.append(item)
        #         self.current_index += 1
        #     else:
        #         self.buffer[self.current_index] = item
        # else:
        #     self.current_index = 0
        #-----------
        # while len(self.buffer) < self.capacity:
        #     self.buffer.append(None)
        #
        # if self.current_index < self.capacity:
        #     if not self.buffer[self.current_index]:
        #         self.buffer.append(item)
        #     else:
        #         self.buffer[self.current_index] = item
        #         self.current_index += 1
        # if self.current_index > (self.capacity - 1):
        #     self.current_index = 0
        #-----------
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)

        self.buffer[self.current_index] = item

        self.current_index += 1

        if self.current_index > (self.capacity - 1):
            self.current_index = 0

        

        

    def get(self):
        return self.buffer