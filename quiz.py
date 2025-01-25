score = 0

print("Twoje nulubione zwierze ?")
print( " A - Lis,  B - Kot,  C- Pies ")
odp1 = input()
if odp1 == "A":
    score +1
elif odp1 == "B":
    score + 2
elif odp1 == "C":
    score +3

print("Twoja ulubiona pora dnia ?")
print( " A - Rano,  B - Południe,  C- Wieczór ")
odp2 = input()
if odp2 == "A":
    score +1
elif odp2 == "B":
   score + 2
elif odp2 == "C":
   score +3

print("Twoje ulubione jedzenie ?")
print( " A - Kiełbasa,  B - Ogórek,  C- Jabłko ")
odp3 = input()
if odp3 == "A":
    score +1
elif odp3 == "B":
    score + 2
elif odp3 == "C":
    score +3

if score > 1 or score <=3:
    print("Jesteś Wilkiem")
elif score > 4 or score <=6:
    print("Jesteś Kangurem")
elif score > 7 or score <=9:
    print ("Jesteś osłem")
else:
    print("Jesteś mało inteligentny")