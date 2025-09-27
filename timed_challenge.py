def remove_duplicates_keep_order(values):

    seen = set()
    result = []
    for v in values:
        if v not in seen:
            seen.add(v)
            result.append(v)
    return result

print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))



#Remove Duplicates (Keep Order)
#Return the values in the order they first appeared, without duplicates.
#Input: ["apple", "banana", "apple", "kiwi", "banana"]
#Output: ["apple", "banana", "kiwi"]
