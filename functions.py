normal_chai = 15
total = 0

def chai_bill(cups, *addons, **discount):
    total = normal_chai*cups

    totalAddons = len(addons)
    total += totalAddons*5

    discountpercent = discount.get('discount_percent')
    if(discountpercent):
        total -= (total * discountpercent) / 100

    return total

print(chai_bill(2))                                              
print(chai_bill(3, "ginger", "masala"))                          
print(chai_bill(4, "biscuit", discount_percent=10))              
print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))