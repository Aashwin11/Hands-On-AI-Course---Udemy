#Generator Comprehension

#Behind the scene:
#Generators are used for saving memory

#SYNTAX: (expression for item in iterable if condition)

# How it works:
    # (x for x in items) - this gives 1 item at a time
    # [x for x in items] -  this makes entire list in memory

daily_sales=[5,10,12,7,3,8,9,15,27,89,98,123]

total_cups_above5_rs=sum(x for x in daily_sales if x>20)
print(total_cups_above5_rs)