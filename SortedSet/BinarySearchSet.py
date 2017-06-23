class BinarySearchSet:

    def __init__(self):
        self.base_array = []  # There is no native arrays. I won't worry about resizing.

    def first(self):
        return self.base_array[0]

    def last(self):
        return self.base_array[len(self.base_array) - 1]

    def shift_right(self, index):
        for i in range(len(self.base_array) - 1, index):
            self.base_array[i + 1] = self.base_array[i]

    def add(self, item):
        if len(self.base_array) == 0:
            self.base_array.append(item)
        else:
            low_index = 0
            high_index = len(self.base_array) - 1
            while low_index < high_index:
                middle = (high_index + low_index) / 2
                if item == self.base_array[middle]:
                    return False
                else:
                    if item < self.base_array[middle]:
                        high_index /= 2 + 1
                        continue
                    else:
                        if item > self.base_array[middle]:
                            low_index += (high_index / 2) + 1
                            continue
            self.shift_right(low_index + high_index / 2)
            self[low_index + high_index / 2]  = item
            return True



bss = BinarySearchSet()
bss.base_array.append(4)
bss.base_array.append(5)
bss.base_array.append(7)
print(bss.first())
print(bss.last())
