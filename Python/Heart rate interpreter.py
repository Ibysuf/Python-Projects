heart_rate = 90

too_low = heart_rate < 60
too_high = heart_rate > 110
healthy_range = 110 > heart_rate > 60

print("Heart rate too low:")
print(too_low)

print("Heart rate too high:")
print(too_high)

print("Heart rate healthy:")
print(healthy_range)
