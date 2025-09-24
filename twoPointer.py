def twoPointer(text: str) -> str:
    left = 0
    right = len(text) - 1
    text = list(text)

    while left < right:
        text[left], text[right] = text[right], text[left]
        left+=1
        right-=1
    
    return "".join(text)

test1 = twoPointer("Leo")
print(test1)