# შექმენი ცვლადი რომელიც შეინახავს წინადადებას რომელსაც შენ გამოიტან: პატარა ასოებით, დიდი ასოებით, მხოლოდ პირველი დიდი ასოთი


value = 'classwork YOUTUBE twitch mouse RED can'


print(value.upper())
print(value.capitalize())
print(value.lower())




# ცვლადში მოცემული წინადადებაში find() ის გამოყენებით შეამოწმე თუ არსებობს რომელიმე კონკრეტული სიტყვა



value1 = 'home wifi monitor feather'

print(value1.find('monitor'))




# შექმენი ლისტი სადაც შეინახავ ელემენტებს, ამ ელემენტებს append ით დაუმატე სამი სიტყვა, შემდეგ insert ის
# გამოყენებით მეორე ინდექსზე რაიმე სიტყვა კიდევ ჩაამატე, ხოლო საბოლოოდ pop ით რომელიმე ელემენტი ამოაგდე


list = ['mouse', 'guitar', 'chair', 'window', 'iphone']

list.append('chaos')

list.append('video')

list.append('file')
list.insert(-2,'table')

list.pop(2)

print(list)


