def hero(bullets, dragons):
    if (bullets*2)>dragons:
        return (True)
    elif bullets==dragons:
        return (False)
    else:
        return (False)
bullets=int(input("enter the bullets number: "))
dragons=int(input("entre the dragons number: "))
print(hero(bullets,dragons))

