# Change __init__() - so that attributes initialized with the list
#
# class mysample:
#    def __init__(self):
#         self.L = []
#         i=0
#         while(i<10):
#             p=int(input("element"))
#             self.L.append(p)
#             i+=1
#     def show(self):
#         print(self.L)
#         print("maximim - ", max(self.L), "minimum -",  min(self.L))
#
# obj = mysample()
# obj.show()

class mysample:
    def __init__(self, list):
        self.L = list

    def show(self):
        print(self.L)
        print("maximim - ", max(self.L), "minimum -", min(self.L))


input_list = []
i = 0
while i < 10:
    p = int(input("Enter element:"))
    input_list.append(p)
    i += 1

obj = mysample(input_list)
obj.show()
