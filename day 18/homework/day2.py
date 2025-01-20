# მომხმარებელს შემოატანინე რამე სიტყვა და შემდეგ if ის გამოყენებით შეამოწმე ეს სიტყვა დიდი ასოებითაა დაწერილი თუ პატარა ასოებით ()

word = input("enter a word: ")

if word.isupper():
    print("the word is in uppercase")
elif word.islower():
    print("the word is in lowercase")
else:
    print("The word is neither fully uppercase nor fully lowercase")