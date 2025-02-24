def katta_harf(ismlar):
    new=list(range(len(ismlar)))
    for a in range(len(ismlar)):
       new[a]=ismlar[a].title()
    return new
        
    
ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)

print(katta_harf(ismlar))
