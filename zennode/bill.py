import discount

# initializing the variables
price_a, price_b, price_c = 20, 40, 50
aw, bw, cw = "no", "no", "no"

bulk_5, bulk_10, tie_50, flat_10 = 0, 0, 0, 0
applied_discount = 0

# reciving the quantity and wrap details from user
quantity_a = int(input("Enter the quantity of Product A: "))
if quantity_a > 0:
    aw = input("Do you want gift wrapping? (yes/no): ")
print()

quantity_b = int(input("Enter the quantity of Product B: "))
if quantity_b > 0:
    bw = input("Do you want gift wrapping? (yes/no): ")
print()

quantity_c = int(input("Enter the quantity of Product C: "))
if quantity_c > 0:
    cw = input("Do you want gift wrapping? (yes/no): ")
print()

print()
print("                 Cart details")
print("----------------------------------------------")  # list of  cart details
print()

print("product  |   quantity    |   price")
print("     A        " + str(quantity_a) + "        " + str(price_a * quantity_a))
print("     B        " + str(quantity_b) + "        " + str(price_b * quantity_b))
print("     C        " + str(quantity_c) + "        " + str(price_c * quantity_c))

print()
print()

# Calculating the total amount and items
total_cost = (price_a * quantity_a) + (price_b * quantity_b) + (price_c * quantity_c)
total_quantity = quantity_a + quantity_b + quantity_c

print("The available coupons and claimable amount for you")  # showing available coupons details
print("----------------------------------------------------")

if total_cost > 200:
    flat_10 = 10
    print("flat_10 claimable amount : " + str(flat_10))

if quantity_a > 10 or quantity_b > 10 or quantity_c > 10:

    bulk_5_a, bulk_5_b, bulk_5_c = 0, 0, 0

    if quantity_a > 10:
        item_total = quantity_a * price_a
        bulk_5_a = discount.bulk5(item_total)

    if quantity_b > 10:
        item_total = quantity_b * price_b
        bulk_5_b = discount.bulk5(item_total)

    if quantity_c > 10:
        item_total = quantity_c * price_c
        bulk_5_c = discount.bulk5(item_total)

    bulk_5 = bulk_5_a + bulk_5_b + bulk_5_c
    print("bulk_5 claimable amount : " + str(bulk_5))

if total_quantity > 20:
    bulk_10 = discount.bulk10(total_cost)
    print("bulk_10 claimable amount : " + str(bulk_10))

if total_quantity > 30 and (quantity_a > 15 or quantity_b > 15 or quantity_c > 15):

    tie_50_a, tie_50_b, tie_50_c = 0, 0, 0

    if quantity_a > 15:
        disc_a = quantity_a - 15
        item_total = disc_a * price_a
        tie_50_a = discount.tie50(item_total)

    if quantity_b > 15:
        disc_b = quantity_b - 15
        item_total = disc_b * price_b
        tie_50_b = discount.tie50(item_total)

    if quantity_c > 15:
        disc_c = quantity_c - 15
        item_total = disc_c * price_c
        tie_50_c = discount.tie50(item_total)

    tie_50 = tie_50_a + tie_50_b + tie_50_c

    print("tiered_50 claimable amount : " + str(tie_50))

print()
print()
# checking which coupon is better

if tie_50 > bulk_5 and tie_50 > bulk_10 and tie_50 > flat_10:
    applied_discount = tie_50
    print("tiered_50_discount is applied and the discounted amount is :" + str(tie_50))

elif bulk_5 > tie_50 and bulk_5 > bulk_10 and bulk_5 > flat_10:
    applied_discount = bulk_5
    print("bulk_5_discount is applied and the discounted amount is :" + str(bulk_5))

elif bulk_10 > tie_50 and bulk_10 > bulk_5 and bulk_10 > flat_10:
    applied_discount = bulk_10
    print("bulk_10_discount is applied and the discounted amount is :" + str(bulk_10))

elif flat_10 > bulk_10 and flat_10 > bulk_5 and flat_10 > tie_50:
    applied_discount = flat_10
    print("bulk_10_discount is applied and the discounted amount is :" + str(flat_10))

else:
    print("No discount coupons are available")

print()
print()
# applied_discount = max(tie_50, bulk_10, flat_10, bulk_5)

# if applied_discount == 0:
#     print("no discount options are available")
#
# elif applied_discount == tie_50:
#
#
# elif applied_discount == bulk_5:
#     print("bulk_5_discount is applied and the discounted amount is :" + bulk_5)
#
# elif applied_discount == bulk_10:
#     print("bulk_10_discount is applied and the discounted amount is :" + bulk_10)
#
# elif applied_discount == flat_10:
#     print("bulk_10_discount is applied and the discounted amount is :" + str(flat_10))

wrap = 0
# Calculate cost of gift wrapping
if aw.lower() == "yes":
    wrap += quantity_a
if bw.lower() == "yes":
    wrap += quantity_b
if cw.lower() == "yes":
    wrap += quantity_c

package = total_quantity / 10
# print(package)
no_of_packs = discount.package_no(package)
# print(no_of_packs)
print("Total amount :         $" + str(total_cost))  # total amount
print("discount amount :      $" + str(applied_discount))  # discount amount
print("packing charge :       $" + str(no_of_packs * 5))  # packing charge
print("Gift Wrapping charge : $" + str(wrap))  # wrapping charge
print("Final amount :         $" + str(total_cost-applied_discount + wrap + (no_of_packs * 5)))  # final price
