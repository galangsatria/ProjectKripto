from tkinter import *
from random import *
import tkinter as tk
import numpy as np

# membuat popup aplikasi
window = Tk()

# Mengatur ukuran popup window
window.geometry("900x450")

# Mengatur nama program pada popup
window.title("Enkripsi dan Dekripsi SHIFT TRIANGLE Cipher")

## setting the background color

window.configure(bg = 'lightblue')


rand = StringVar()
Msg = StringVar()
key = IntVar()
mode = StringVar()
Result = StringVar()

# Fungsi untuk keluar
def qExit():
    window.destroy()

# Fungsi untuk mereset windows
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# adding entries
entry_the_text = Entry(window, width = 40, textvariable = Msg)
entry_the_text.place(x = 350, y = 160)

entry_key = Entry(window, width = 40, textvariable = key)
entry_key.place(x = 350, y = 200)

entry_ED = Entry(window, width = 40, textvariable = mode)
entry_ED.place(x = 350, y = 240)

entry_the_converted_text = Entry(window, width = 40, textvariable = Result)
entry_the_converted_text.place(x = 350, y = 360)


# labels
Label(window, text = 'Program Enkripsi dan Dekripsi', bg='lightgreen', fg = 'grey', font=('montserrat', 25)).place(x = 180, y = 25)
Label(window, text = 'SHIFT & TRIANGLE', bg='lightgreen', fg = 'grey', font=('montserrat', 25)).place(x = 240, y =75)
Label(window, text = 'Plain Text/Cipher Text:', bg='lightblue', fg = 'grey', font=('montserrat', 15)).place(x = 50, y = 160)
Label(window, text = 'Key (integer):' , bg='lightblue', fg = 'grey', font = ('montserrat', 15)).place(x = 50, y = 200)
Label(window, text = 'e untuk enkripsi / d untuk dekripsi' , bg='lightblue', fg = 'grey', font=('montserrat', 15)).place(x = 50, y = 240)
Label(window, text = 'Hasil:' , bg='lightblue', fg = 'grey', font = ('montserrat', 15)).place(x = 50, y = 360)


#Fungsi Shift Cipher
def enkripsi(k, clear):


    result = ""
    #transverse the plain text
    for i in range(len(clear)):
        char = clear[i]
    # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) + k - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif char == " ":
            result += " "
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)

    return result

def dekripsi(k, clear):
    hasil = []
    for d in clear:
        clear = (clear-k) % 26
    
        hasil.append(clear)
    return "".join(hasil)
    clear = decode_triangle


#Function triangle encryption
def encode_triangle(k, clear):
    row = 0
    min = 1
    huruf = []
    plaintext = enkripsi(k, clear)
    panjang = len(plaintext)
    while (panjang > 0):
        panjang -= min
        huruf.append(min)
        min += 2
        row += 1
    col = min - 2

    for i in range (panjang, 0):
        plaintext += "x"
    segitiga = np.full((row, col), None)

    count = 0
    for i in range(row):
        tempcol = int(((col-1)/2)-i)
        for j in range(huruf[i]):
            segitiga[i][tempcol] = plaintext[count]
            count += 1
            tempcol +=1

    enc = ""
    for i in range(col):
        for j in range(row):
            if segitiga[j][i] == None:
                continue
            else:
                enc += segitiga[j][i]
    return enc


#Function triangle decryption
def decode_triangle(clear):
    row = 0
    min = 1
    huruf = []
    panjang = len(clear)
    while (panjang > 0):
        panjang -= min
        huruf.append(min)
        min += 2
        row += 1
    col = min - 2
    segitiga = np.full((row, col), None)

    count = 0
    for i in range(row):
        tempcol = int(((col-1)/2)-i)
        for j in range(huruf[i]):
            segitiga[i][tempcol] = clear[count]
            count += 1
            tempcol +=1

    count = 0
    for i in range(col):
        for j in range(row):
            if segitiga[j][i] == None:
                continue
            else:
                segitiga[j][i] = clear[count]
                count += 1

    dec = ""
    for i in range(row):
        for j in range(col):
            if segitiga[i][j] == None:
                continue
            else:
                dec += segitiga[i][j]
    return dec

def Ref():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode_triangle(k, clear))
    else:
        Result.set(dekripsi(k, clear))
## adding buttons

btn_Show_message  = Button( fg = "black",
                        font = ('montserrat', 16, 'bold'), width = 10,
                    text = "Show", bg = "green", command = Ref).place(x = 700, y = 110 )



btn_reset = Button( fg = "black",
                        font = ('montserrat', 16, 'bold'), width = 10,
                    text = "Reset", bg = "yellow", command = Reset).place(x = 700, y = 200 )



btn_exit = Button( fg = "black",
                        font = ('montserrat', 16, 'bold'), width = 10,
                    text = "Exit", bg = "red", command = qExit).place(x = 700, y = 290)

# keeps window alive
window.mainloop()

#chipertext contoh : gixytxvxx