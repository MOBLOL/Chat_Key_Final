abc = "абвгдеёжзийклмнопрстуфхцчщъыьэюя1234567890qwertyuiopasdfghjklzxcvbnmАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧЩЪЫЬЭЮЯQWERTYUIOPASDFGHJKLZXCVBNM!*/-+@#%$№ ."
abc_arr, new_arr = list(abc), list(abc)



def EnCode(text):
    file = open('Key.txt', 'r')
    content = file.readlines()
    file.close()
    key = content[0]
    Cyp = ''
    text_Cyp = list(text)
    for i in text_Cyp:
        for sim in abc_arr:
            if i == sim:
                index = abc_arr.index(sim)
                Cyp = f'{Cyp}{key[index]}'
    return Cyp
    # return cyp

def DeCode(text):
    DeCyp = ''
    file = open('Key.txt', 'r')
    content = file.readlines()

    file.close()
    key = content[0]
    DeCyp = f'{text.split(" ")[0]}'
    text = text.split(" ")[1]
    text = list(text)
    for i in text:
        for sim in key:
            if i == sim:
                index = key.index(i)
                DeCyp = f'{DeCyp}{abc_arr[index]}'

    return DeCyp
