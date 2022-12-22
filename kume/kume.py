###################SETS####################
"""
kume = set()
kume = {}

kume = {11, 22, 33, 44, 55, 66}

kume.add(77) set'te olan bir elamanı tekrar eklemek gerkesizdir. sadece bu elaamndan bir tane gözükür
print(kume)
kume.discard(44) #set içindeki elemanı çıkartır
kume.remove

kume1 = {1, 11, 10, 33, 55, 66, 90}
kume2 = {10, 90, 66}
kumefark = kume1 - kume2 # kumeden data çıkarma
kumefark2 = kume1.difference(kume2) #Aynı şey xd
print(kumefark)
"""


kume1 = {1, 11, 10, 33, 55, 66, 90}
kume2 = {10, 90, 66, 100, 98, 5}
kumeKesisim = kume1 & kume2
kumeKesisim2 = kume1.intersection(kume2) # same things
kumebirlesim = kume1.union(kume2) # Birleştime
print(kumeKesisim)
print(f'Kume1 kumeBirşleşim"in alt kümesimi ?{kume1.issubset(kumebirlesim)}')
print(f'Kume1 kume2"in üst kümesimi ?{kume1.issuperset(kumebirlesim)}')
print(f'Kume1 kume2 ayrık kümelermi ?{kume1.isdisjoint(kumebirlesim)}')


