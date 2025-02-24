print("Do'stlaringiz yoshini saqlaymiz.")
dostlar={}
ishora=True
while ishora:
    ism=input("do'stlarizzi ismini kiriting :")
    yosh=input(f"{ism.titl()} ning yoshini kiriting:")
    dostlar[ism]=int(yosh)

    javob=("Yana malumot kiritiaszmi:")
    if javob=="yo'q":
        ishora=False

for  ism,yosh  in dostlar.itmes():
    print(f" {ism.title()} {yosh} yoshda")
