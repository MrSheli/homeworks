# შექმენი სია სადაც შეიტან მოსწავლეების ქულებს append ით შემდგომ
# გამოიტან ვინ მიიღო ყველაზე მაღალი და დაბალი
# ქულები და ბოლოს დაალაგებ ამ შედეგებს ცუდიდან კარგის მხრივ
# [ყველაზე ცუდი ----> ყველაზე კარგი]


list = []

list.append(-4)
list.append(6452)
list.append(12312)
list.append(-435623)
list.append(-343)


print(sorted(list))
print(min(list))
print(max(list))