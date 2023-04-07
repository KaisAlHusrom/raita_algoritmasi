# calculate bmbc
def Bmbc(pattern):
    bmbc_a = len(pattern) - 1
    bmbc = []
    for i in range(len(pattern)):
        bmbc.append(bmbc_a - i)
    return bmbc


def raita_algoritma(pattern, text):
    bmbc = Bmbc(pattern=pattern)
    found = 0

    # aranacak satırın harflerin sayısı pattern'in harfların sayısının katlarında olmazsa
    # fazla harfleri silenecek
    while len(text) % len(bmbc) != 0:
        if text[len(text) - len(bmbc):] == pattern:
            found += 1
        text = text[:-1]

    control = False
    # Pattern aranack satırın içinde araması
    for char_i in range(0, len(text), len(bmbc)):
        for i in range(len(bmbc)):
            if pattern[len(bmbc) - 1 - i] == text[(char_i + len(bmbc) - 1) - i]:
                control = True
            else:
                control = False
                break
        if control == True:
            found += 1

    return int(found)


def main():

    print(f"simdi upon, sigh, Dormouse, jury-box ve swim kelimelerin alice_in_wonderland metnin icinde Raita Algoritmasi kullanarak arancaklar")
    txt = open("alice_in_wonderland.txt", "r")
    all_lines = txt.readlines()
    aranacak = {
        "upon": 0,
        "sigh": 0,
        "Dormouse": 0,
        "jury-box": 0,
        "swim": 0
    }

    for word in aranacak:
        for line in all_lines:
            aranacak[word] += raita_algoritma(word, line)
        print(f"{word} {aranacak[word]} kez tekrarlandi")

    print("kendin denemek istiyorsan")
    text = input("bit metin yaz\n")
    pattern = input("metnin icinde aramak istedigin kelimeyi yaz\n")
    count = raita_algoritma(pattern=pattern, text=text)
    print(f"{pattern} {count} kez bulundu")


main()
