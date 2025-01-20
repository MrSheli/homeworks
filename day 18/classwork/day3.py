#შექმენი ლისტი guests სადაც append ით ჩაამატებ სამ განსხვავებულ
#სახელს, შემდეგ len ით დაბეჭდე რამდენი მნიშვნელობაა ამ ლისტში,
#მაგრამ ვთქვათ ბოლო სტუმარი არ მოვიდა ამიტომ pop ის
#გამოყენებით ამოაკელი ის ლისტიდან, ამის შემდეგ კი ხელახლა დაბეჭდე

guests = ['luka', 'nika', 'beqa', 'giorgi']

guests.append('natia')
guests.append('nino')
guests.append('avto')

print(len(guests))

guests.pop()

print(len(guests))