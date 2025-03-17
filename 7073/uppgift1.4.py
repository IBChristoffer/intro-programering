tal = int(input("Ange ett tal: "))

if tal > 0 and tal <= 9:
    print("talet är ensiffrigt")
elif tal > 9 and tal <= 99: 
    print("talet är tvåsiffrigt")
elif tal > 99 and tal <= 999:
    print("talet är tresiffrigt")
else: 
    print("talet är fyrsiffrigt eller större")

print("klar")