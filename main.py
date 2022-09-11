import tkinter


root = tkinter.Tk()
root.title("basic converter")
root.geometry("300x400")


def convert():
    nb_ini = [i for i in nb_init.get()]
    nb_ini_inter = []
    base_ini = int(base_init.get())
    base_end = int(base_final.get())
    base_10 = 0
    for i in range(len(nb_ini)):
        nb_ini_inter.append(nb_ini[len(nb_ini)-i-1])

    nb_ini = list(nb_ini_inter)
    nb_final_l = []
    nb_final_l_inter = []
    nb_end = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(nb_ini)):
        if nb_ini[i].lower() in alphabet:
            nb_ini[i] = nb_ini[i].lower()

    for i in range(len(nb_ini)):
        if "1" in nb_ini[i]:
            base_10 += 1 * (base_ini ** i)
        if "2" in nb_ini[i]:
            base_10 += 2 * (base_ini ** i)
        if "3" in nb_ini[i]:
            base_10 += 3 * (base_ini ** i)
        if "4" in nb_ini[i]:
            base_10 += 4 * (base_ini ** i)
        if "5" in nb_ini[i]:
            base_10 += 5 * (base_ini ** i)
        if "6" in nb_ini[i]:
            base_10 += 6 * (base_ini ** i)
        if "7" in nb_ini[i]:
            base_10 += 7 * (base_ini ** i)
        if "8" in nb_ini[i]:
            base_10 += 8 * (base_ini ** i)
        if "9" in nb_ini[i]:
            base_10 += 9 * (base_ini ** i)
        if "a" in nb_ini[i]:
            base_10 += 10 * (base_ini ** i)
        if "b" in nb_ini[i]:
            base_10 += 11 * (base_ini ** i)
        if "c" in nb_ini[i]:
            base_10 += 12 * (base_ini ** i)
        if "d" in nb_ini[i]:
            base_10 += 13 * (base_ini ** i)
        if "e" in nb_ini[i]:
            base_10 += 14 * (base_ini ** i)
        if "f" in nb_ini[i]:
            base_10 += 15 * (base_ini ** i)
        if "g" in nb_ini[i]:
            base_10 += 16 * (base_ini ** i)
        if "h" in nb_ini[i]:
            base_10 += 17 * (base_ini ** i)
        if "i" in nb_ini[i]:
            base_10 += 18 * (base_ini ** i)
        if "j" in nb_ini[i]:
            base_10 += 19 * (base_ini ** i)
        if "k" in nb_ini[i]:
            base_10 += 20 * (base_ini ** i)
        if "l" in nb_ini[i]:
            base_10 += 21 * (base_ini ** i)
        if "m" in nb_ini[i]:
            base_10 += 22 * (base_ini ** i)
        if "n" in nb_ini[i]:
            base_10 += 23 * (base_ini ** i)
        if "o" in nb_ini[i]:
            base_10 += 24 * (base_ini ** i)
        if "p" in nb_ini[i]:
            base_10 += 25 * (base_ini ** i)
        if "q" in nb_ini[i]:
            base_10 += 26 * (base_ini ** i)
        if "r" in nb_ini[i]:
            base_10 += 27 * (base_ini ** i)
        if "s" in nb_ini[i]:
            base_10 += 28 * (base_ini ** i)
        if "t" in nb_ini[i]:
            base_10 += 29 * (base_ini ** i)
        if "u" in nb_ini[i]:
            base_10 += 30 * (base_ini ** i)
        if "v" in nb_ini[i]:
            base_10 += 31 * (base_ini ** i)
        if "w" in nb_ini[i]:
            base_10 += 32 * (base_ini ** i)
        if "x" in nb_ini[i]:
            base_10 += 33 * (base_ini ** i)
        if "y" in nb_ini[i]:
            base_10 += 34 * (base_ini ** i)
        if "z" in nb_ini[i]:
            base_10 += 35 * (base_ini ** i)

    while base_10 > 0:
        nb_final_l.append(base_10 % base_end)
        base_10 = base_10 // base_end

    for i in range(len(nb_final_l)):
        nb_final_l_inter.append(nb_final_l[len(nb_final_l)-i-1])

    nb_final_l = list(nb_final_l_inter)

    for i in range(len(nb_final_l)):
        nb_end += str(nb_final_l[i])
    if base_end > 10:
        for i in range(10, 36):
            nb_end = nb_end.replace(str(i), str(chr(i+55)))

    result.delete(0, tkinter.END)
    result.insert(0, nb_end)


ini = tkinter.Label(root, text='insert the initial number')
ibi = tkinter.Label(root, text='insert the initial base')
ibf = tkinter.Label(root, text='insert the final base')
r = tkinter.Button(root, text='Result', command=convert)


nb_init = tkinter.Entry(root)
base_init = tkinter.Entry(root)
base_final = tkinter.Entry(root)
result = tkinter.Entry(root)

ini.pack()
nb_init.pack()
ibi.pack()
base_init.pack()
ibf.pack()
base_final.pack()
r.pack()
result.pack()

root.mainloop()
