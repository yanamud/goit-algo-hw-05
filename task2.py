def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    i = 0
    upper_value = arr[-1]
    if upper_value < x :
        return (i, -1)
    
    while low <= high:
 
        mid = (high + low) // 2
        i += 1
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_value = arr[mid]
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return (i, arr[mid])
 
    # якщо елемент не знайдений
    return (i, upper_value)
    
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result[1] != -1 and arr[0] <= x:
    print (result)
    print (f"where '{result[0]}' is the total number of iterations and '{result[1]}' is the upper limit for the element '{x}'")
elif result[1] != -1 and arr[0] > x:
    print (result)
    print (f"where '{result[0]}' is the total number of iterations and '{result[1]}' is the upper limit for the element '{x}', but this element is outside the array")
else:
    print (result)
    print(f"The element '{x}' is outside the array")