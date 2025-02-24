mahsulotlar={'olma':45,
             'nok':74,
             'behi':65}
sum=0
while True:
    mahsulot=input("nima kerak:")
    if mahsulot in mahsulotlar.keys():
        narx=mahsulotlar[mahsulot]
        print(f"{mahsulot} narxi { narx}")
        sum+=narx
    else:
        print("Bizda bunday mahsulot yo'q")
    a=input("Yana mahsulot ketremi(ha/yo'q?:")
    if a=="yo'q":
        break
print(f" sizdan  {sum} so'm bo'ldi")
