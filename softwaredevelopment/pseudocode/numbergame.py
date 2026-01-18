class NumberCheck: 
    def run(self): 
        nums = [] 
        for i in range(1, 4): 
            nums.append(float(input(f"Enter number {i}: "))) 
        if sum(nums) < 10 or nums[1] > 5: 
            print("invalid") 
        else: 
            print("valid") 

NumberCheck().run() 