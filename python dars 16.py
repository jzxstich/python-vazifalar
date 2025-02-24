davlatlar={
    "o'zbekiston":{ 'poytaxt':'toshkent',
                    'hudud':448978,
                    'aholi':33_000_000,
                    'pul':'so\'m'},
    'rossiya':{'poytaxt':'moskva',
               'hudud':17098246,
               'aholi':1444000000,
               'pul':'rubl'},
    'aqsh':{'poytaxt':'vashington',
            'hudud':9631418,
            'aholi':327000000,
            'pul':'dollar'},
    'malayziya':{'poytaxt':'KUla-lumpur',
                 'hudud':329750,
                 'aholi':25000000,
                 'pul':'rinngit'}}
davlat=davlatlar.get(input("Davlat nomini kiriting: ").lower(),"\nBizda bunday davlat yo'q ")


if davlat=="\nBizda bunday davlat yo'q":
    print(davlat)
else:
    print(f" 
