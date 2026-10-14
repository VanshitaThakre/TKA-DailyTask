
# Task 01: Shopping Bill - GST First, Discount After

def calculateElectronicsGST(a, b):
    subtotal = a + b
    gst = subtotal * 18 / 100
    return subtotal + gst


def calculateFashionGST(c, d):
    subtotal = c + d
    gst = subtotal * 13 / 100
    return subtotal + gst


def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount


# Sample test values
a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)
total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print("Electronics after GST:", f"{electronics:.2f}")
print("Fashion after GST:", f"{fashion:.2f}")
print("Food after GST:", f"{food:.2f}")
print("Total after GST:", f"{total:.2f}")
print("20% Discount:", f"{discount:.2f}")
print("Final Payable Amount:", f"{final_amount:.2f}")
