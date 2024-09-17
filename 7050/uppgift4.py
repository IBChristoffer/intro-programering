
tal = int(input("Mata in ett tal: "))


if tal < 0:
    print(f"{tal} är ett negativt tal.")
elif 0 <= tal <= 9:
    print(f"{tal} är ett ensiffrigt tal.")
elif 10 <= tal <= 99:
    print(f"{tal} är ett tvåsiffrigt tal.")
elif 100 <= tal <= 999:
    print(f"{tal} är ett tresiffrigt tal.")
else:
    print(f"{tal} är ett minst fyrsiffrigt tal.")