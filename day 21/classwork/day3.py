# დაწერე ლისტი სადაც შეიტან რამდენიმე მოსწავლის სახელს და value ს მიუწერ ქულას,
# შემდეგ get ით გამოიტანე მოსწავლის სახელით მისი ქულა და შემდეგ მხოლოდ მოსწავლეების სახელები დაპრინტე

{}

students = {
    "nika": "6",
    "saba": "8",
    "nini": "9",
    "beqa": "10"
}

total = students.get("saba")

print(total)

print(students.keys())