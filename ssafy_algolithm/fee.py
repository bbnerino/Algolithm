def tax(won):
    if won <= 1200:
        return (won*0.06)
    elif 1200 <won <= 4600:
        result = (won-1200)*0.15 + 1200*(0.06)
        return (result)
    elif 4600<won<= 8800:
        result = 582 + (won-4600)*(0.35)
        return (result)

print(tax(1200))
print(tax(4600))
print(tax(5000))