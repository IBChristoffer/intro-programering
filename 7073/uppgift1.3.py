tal1 = float(input("Mata in det första talet: "))
tal2 = float(input("Mata in det andra talet: "))


if tal1 > tal2:
    print(f"{tal1} är större än {tal2}")
elif tal2 > tal1:
    print(f"{tal2} är större än {tal1}")
else:
    print("Talen är lika stora")