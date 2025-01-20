# შექმენი ლისტი cart სადაც append ფუნქციის გამოყენებით
# დაამატებ სამ განსხვავებულ მნიშვნელობას, insert ით ჩაამატებ პირველ
# ინდექსზე ელემენტს ბოლოში კი გამოიტანე len() ის დახმარებით ელემენტების რაოდენობა


lis = ["interstellar", "dark matter", "the boys", "inception"]

lis.append("squid game")
lis.insert(0,"movies")
lis.append("series")
lis.append("final")



print(len(lis))
print(lis)