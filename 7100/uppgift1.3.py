def till_rovorspraket(ord):
    vokaler = "aeiouyåäö"
    rovar_ord = ""

    for bokstav in ord:
        if bokstav.lower() not in vokaler:
            rovar_ord += bokstav + "o" + bokstav.lower()
        else:
            rovar_ord += bokstav
    
    return rovar_ord


ord = input("Mata in ett ord: ")
rovarspraket = till_rovorspraket(ord)
print(f"Ordet i rövarspråket är: {rovarspraket}")