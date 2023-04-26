print("Pierwsza liczba.")
liczba1=int(input())
print("Druga liczba.")
liczba2=int(input())

print("Co robimy szefie? Proszę o pomoc, bo jestem zagubiony.")
odp=input()

if odp == "dodawanie":
    dodawanie= liczba1+liczba2
    print("Wynikiem dodawania jest: ", dodawanie)

elif odp=="odejmowanie":
    odejmowanie= liczba1-liczba2
    print("Wynikiem odejmowania jest: ", odejmowanie)

elif odp=="mnożenie":
    mnożenie=liczba1*liczba2
    print("Wynikiem mnożenia jest: ", mnożenie)

elif odp=="dzielenie":
    dzielenie=liczba1/liczba2
    print("Wynikiem dzielenia jest: ", dzielenie)
else:
    print("Bruh. WOAAAH It's really bad.")
#piekny kalkulator 10/10 pozdrawiam z rodzinką :*
