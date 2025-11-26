# LIST Example
print("-------------------------------")
products_list = [
    "Shirt", "Jeans", "Jacket", "Shoes", "Belt",
    "Socks", "Watch", "Cap", "Sunglasses", "Wallet"
]

print("\nLIST EXAMPLE")
print("Original List:", products_list)

products_list.append("Backpack")
print("After append:", products_list)

products_list.insert(2, "Scarf")
print("After insert at index 2:", products_list)

products_list.remove("Belt")
print("After remove 'Belt':", products_list)

products_list.pop()
print("After pop():", products_list)

products_list.sort()
print("After sort():", products_list)

products_list.reverse()
print("After reverse():", products_list)


# TUPLE Example
print("-------------------------------")
products_tuple = (
    "Shirt", "Jeans", "Jacket", "Shoes", "Belt",
    "Socks", "Watch", "Cap", "Sunglasses", "Wallet"
)

print("\nTUPLE EXAMPLE")
print("Tuple:", products_tuple)
print("Count of 'Shirt':", products_tuple.count("Shirt"))
print("Index of 'Watch':", products_tuple.index("Watch"))


# SET Example
print("-------------------------------")
products_set = {
    "Shirt", "Jeans", "Jacket", "Shoes", "Belt",
    "Socks", "Watch", "Cap", "Sunglasses", "Wallet"
}

print("\nSET EXAMPLE")
print("Original Set:", products_set)

products_set.add("Backpack")
print("After add:", products_set)

products_set.discard("Watch")
print("After discard 'Watch':", products_set)


# DICTIONARY Example
print("-------------------------------")
products_dict = {
    1: "Shirt",
    2: "Jeans",
    3: "Jacket",
    4: "Shoes",
    5: "Belt",
    6: "Socks",
    7: "Watch",
    8: "Cap",
    9: "Sunglasses",
    10: "Wallet"
}

print("\nDICTIONARY EXAMPLE")
print("Original Dictionary:", products_dict)

print("Get key 3:", products_dict.get(3))
print("All Keys:", products_dict.keys())
print("All Values:", products_dict.values())

products_dict.update({11: "Backpack"})
print("After update:", products_dict)

products_dict.pop(5)
print("After pop key 5:", products_dict)
