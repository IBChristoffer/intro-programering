
månad = int(input("Mata in din födelsemånad (1-12): "))


if månad in [12, 1, 2]:
    årstid = "vinter"
elif månad in [3, 4, 5]:
    årstid = "vår"
elif månad in [6, 7, 8]:
    årstid = "sommar"
elif månad in [9, 10, 11]:
    årstid = "höst"
else:
    årstid = "ogiltig månad"


print(f"Du är född på {årstid}.")