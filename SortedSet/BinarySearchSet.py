class BinarySearchSet:

    def __init__(self):
        self.base_array = []  # There is no native arrays. I won't worry about resizing.

    def first(self):
        return self.base_array[0]

    def last(self):
        return self.base_array[len(self.base_array) - 1]

    # Shift the values in the array to the right
    def shift_right(self, index):
        if len(self.base_array) - 1 == index:
            self.base_array.append(self.base_array[index])
            return
        for i in range(len(self.base_array) - 1, index - 1, -1):
            if i == len(self.base_array) - 1:
                self.base_array.append(self.base_array[i])
            else:
                self.base_array[i + 1] = self.base_array[i]

    def add(self, item):
        # If the array was empty
        if len(self.base_array) == 0:
            self.base_array.append(item)
        else:
            low_index = 0
            high_index = len(self.base_array) - 1
            # When the indices cross, you have the right index
            while low_index < high_index:
                middle = low_index + ((high_index - low_index) / 2)
                # if (high_index - low_index + 1) % 2 == 0:
                #     middle += 1
                # If the item is found, return false
                if item == self.base_array[middle]:
                    return False
                else:
                    if item < self.base_array[middle]:
                        high_index = middle - 1
                        continue
                    else:
                        if item > self.base_array[middle]:
                            low_index = middle + 1
                            continue
            # Handle the case where the array size is 1
            if len(self.base_array) == 1:
                if self.base_array[0] == item:
                    return False
                else:
                    if self.base_array[0] < item:
                        self.base_array.append(item)
                        return True
                    else:
                        self.base_array[1] = self.base_array[0]
                        self.base_array[0] = item
                        return True
            # Check to see if when the indices crossed, the correct value was found
            if self.base_array[high_index] == item:
                return False
            # Shift the values to the right
            print(high_index)
            self.shift_right(high_index)
            # Insert the value
            self.base_array[high_index] = item
            return True


bss = BinarySearchSet()
bss.add(5)
print(bss.base_array)
bss.add(7)
print(bss.base_array)
bss.add(6)
print(bss.base_array)
bss.add(7)
print(bss.base_array)
#
bss.add(-12)
print(bss.base_array)
# bss.add(-12)
# print(bss.base_array)
bss.add(0)
print(bss.base_array)
# bss.add(123)
# print(bss.base_array)



