guests = [1,2,3,4,5,6]
print(f"The old guest list is: {guests}")
didnt_arrive = guests.pop(2)
guests.insert(2,10)
print(f"The new guest list is: {guests}")
print(f"The guest that couldn't arrive was: {didnt_arrive}")