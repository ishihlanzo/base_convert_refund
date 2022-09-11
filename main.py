# made by ø
import tkinter

# creation of the windows
root = tkinter.Tk()
root.title("base converter")
root.geometry("250x350+15+274")
root.resizable(width=False, height=False)

# program for converting


def convert():
    # creation of all variable for later
    nb_ini = [i for i in nb_init.get()]
    nb_ini_inter = []
    base_ini = int(base_init.get())
    base_end = int(base_final.get())
    base_10 = 0
    nb_final_l = []
    nb_final_l_inter = []
    nb_end = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(nb_ini)):
        nb_ini_inter.append(nb_ini[len(nb_ini)-i-1])

    nb_ini = list(nb_ini_inter)

    for i in range(len(nb_ini)):
        if nb_ini[i].lower() in alphabet:
            nb_ini[i] = nb_ini[i].lower()
    # convert the entered number to base 10

    for i in range(len(nb_ini)):
        if nb_ini[i] in number:
            base_10 += int(nb_ini[i]) * (base_ini ** i)
        elif nb_ini[i] in alphabet:
            base_10 += (ord(nb_ini[i])-87) * (base_ini ** i)

    # make some magick with that

    while base_10 > 0:
        nb_final_l.append(base_10 % base_end)
        base_10 = base_10 // base_end

    for i in range(len(nb_final_l)):
        nb_final_l_inter.append(nb_final_l[len(nb_final_l)-i-1])

    nb_final_l = list(nb_final_l_inter)

    for i in range(len(nb_final_l)):
        nb_end += str(nb_final_l[i])

    # change the '10' in 'A' (and every other letter)
    if base_end > 10:
        for i in range(10, 36):
            nb_end = nb_end.replace(str(i), str(chr(i+55)))

    # show the result on the windows in the entry 'result'
    result.delete(0, tkinter.END)
    result.insert(0, nb_end)


# creation of objet in the windows
title = tkinter.Label(root, text='\nBASE CONVERTER', font=25)
ini = tkinter.Label(root, text='insert the initial number')
ibi = tkinter.Label(root, text='insert the initial base\n[min : 2 max : 35]')
ibf = tkinter.Label(root, text='insert the final base\n[min : 2 max : 35]')
r = tkinter.Button(root, text='Result\n↓ ↓ ↓', command=convert)
nb_init = tkinter.Entry(root)
base_init = tkinter.Entry(root)
base_final = tkinter.Entry(root)
result = tkinter.Entry(root)

# display objects
pad = 5
title.pack()
ini.pack(pady=pad)
nb_init.pack(pady=2)
ibi.pack(pady=pad)
base_init.pack(pady=2)
ibf.pack(pady=pad)
base_final.pack(pady=2)
r.pack(pady=pad, ipadx=35)
result.pack(ipadx=50, pady=10)

# show the windows
root.mainloop()
