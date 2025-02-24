print("Kiritilgan sonning kvadatratini qautaruvchi dastur")
savol="istalgan son kiriting "
savol+=("dasturni to'xtatish uchun 'exit' deb yozing:")
ishora=True
while ishora:
    qiymat=input(savol)
    if qiymat=='exit':
        ishora=False
    else:
        print(float(qiymat)**2)
