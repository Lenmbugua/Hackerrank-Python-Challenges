def is_leap(year):
    # Check if the year is evenly divisible by 4
    if year % 4 == 0:
        # Check if the year is evenly divisible by 100
        if year % 100 == 0:
            # Check if the year is also evenly divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Example usage:
year = int(input())
print(is_leap(year))
