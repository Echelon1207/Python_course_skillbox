def check(line):
    name, mail, age = line.split(" ")
    age = int(age)
    if name.isalpha() is False:
        raise NameError("Поле «Имя» содержит НЕ только буквы")
    if age not in range(10, 100):
        raise ValueError("Поле «Возраст» НЕ является числом от 10 до 99")
    if '@' not in mail and '.' not in mail:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и . (точку)")
    return line

with open("registrations.txt", "r", encoding="utf-8") as file, \
        open('registration_bad.log', 'a', encoding='utf-8') as error, \
        open('registrations_good.log', 'a', encoding='utf-8') as good:
    for line in file:
        try:
            str_file = check(line)
        except (NameError, ValueError, SyntaxError) as e:
            error.write(str(e))
        else:
            good.write(line)