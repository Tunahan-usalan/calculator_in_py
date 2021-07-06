say1 = int(input("Say1 = "))
say2 = int(input("Say2 = "))
islem = str(input("Islemi Giriniz = "))


class Hesap_Makinesi:

    def __init__(self, say1, say2, islem):
        self.say1 = say1
        self.say2 = say2
        self.islem = islem


    if islem == "toplama":
        output = say1 + say2
        print(output)

    if islem == "cikarma":
        output = say1 - say2
        print(output)

    if islem == "carpma":
        output = say1 * say2
        print(output)

    if islem == "bolme":
        output = say1 / say2
        print(output)




