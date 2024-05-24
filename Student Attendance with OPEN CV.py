from tkinter import *
#import xlwt
import csv
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

window = Tk()
window.title("Absensi Mahasiswa")
window.geometry("400x500")
label1 = Label(window, text="Nama")
label1.grid(column=0, row=0)
text1 = Text(window, width=50, height=5)
text1.grid(column=1, row=0)
label2 = Label(window, text="NIM")
label2.grid(column=0, row=1)
text2 = Text(window, width=50, height=5)
text2.grid(column=1, row=1)
label3 = Label(window, text="Mata Kuliah")
label3.grid(column=0, row=2)
text3 = Text(window, width=50, height=5)
text3.grid(column=1, row=2)


def savexcl():
    f = open('abs.csv', 'a')
    w = csv.writer(f)
    inputValue1 = text1.get("1.0", "end-1c")
    inputValue2 = text2.get("1.0", "end-1c")
    inputValue3 = text3.get("1.0", "end-1c")
    w.writerow(['Nama', 'NIM', 'Matkul', 'Jam Absen'])
    w.writerow([str(inputValue1), str(inputValue2), str(inputValue3), str(current_time)])
    f.close()

Btn = Button(window, text="Submit Absensi", command=savexcl)
Btn.grid(column=1, row=3)

window.mainloop()