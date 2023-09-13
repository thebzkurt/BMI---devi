import tkinter as tk
from tkinter import ttk

def isFloat(val) :
    try :
        float(val)
        return True
    except ValueError :
        return False

def hesaplama():
    weightParam = A1_Entry.get()
    heightParam = A2_Entry.get()
    
    if  isFloat(weightParam) == False or isFloat(heightParam) == False:
        X2_Label.config(text= "zort")
        return
    
    weight = float(weightParam)
    height = float(heightParam)

    if height == 0 :
        X2_Label.config(text= "zort")
        return
    
    index = weight / (height * height)

    if index <= 18.4:
        X2_Label.config(text= "Underweight")
    elif  index > 18.4 and index <= 24.9:
        X2_Label.config(text= "Normal")
    elif index > 24.9 and index <= 39.9:
        X2_Label.config(text="Overweight")
    else :
        X2_Label.config(text="Obese")
    
window = tk.Tk()
window.title("BMI")
window.geometry("300x150")

A1_Label = tk.Label(text= "Entrey your weight (KG)")
A1_Label.pack()

A1_Entry = tk.Entry()
A1_Entry.pack()

A2_Label = tk.Label(text= "Entry your height (M)")
A2_Label.pack()

A2_Entry = tk.Entry()
A2_Entry.pack()

X1_Button = tk.Button(text="hesapla",command= hesaplama)
X1_Button.pack()

X2_Label = tk.Label()
X2_Label.pack()




print(A1_Entry)
window.mainloop()