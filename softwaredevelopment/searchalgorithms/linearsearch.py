# class
class search_algorithm:
    def __init__(self, item, lst):
        self.item = item
        self.lst = lst
    
    def linear_search(self):
        if self.item in self.lst:
            return True
        else:
            return False

# data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# main
def main():
    item = int(input("Enter the item you need to find: "))
    
    arbitrary = search_algorithm(item, numbers)
    found = arbitrary.linear_search()
    
    if found:
        print(item, "is in the list")
    else:
        print(item, "is not in the list")

main()