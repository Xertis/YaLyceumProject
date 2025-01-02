class nums:
    @staticmethod
    def in_range(num, min_val, max_val):
        if num < min_val:
            num = max_val
        elif num > max_val:
            num = min_val
        
        return num
