from tkinter import*
import tkinter.messagebox
from tkinter import ttk
from fpdf import FPDF

window = Tk()

window.title("Absent Letter Program")
window.geometry("1000x500")
window.config(bg = "#9768ba")


#Option Section
Font_1 = ("Aharoni",28,"normal")
Font_2 = ("Aharoni",28,"bold")
Font_3 = ("Aharoni",20,"normal")
Grey = "#969696"
Gold = "#fbd78b"
Purple = "#9768ba"

#Variable Section
Name = StringVar()
Description = StringVar()
Cause = StringVar(value = "Sick/Personal")
Day_Start = StringVar(value = "Day")
Month_Start = StringVar(value = "Month")
Year_Start = StringVar(value = "Year")
Day_Stop = StringVar(value = "Day")
Month_Stop = StringVar(value = "Month")
Year_Stop = StringVar(value = "Year")

#List Section
List_Cause = ("Sick Leave","Personal Leave")
List_Day_Start = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
List_Month_Start = ("January","February","March","April","May","June","July","August","September","October","November","December")
List_Year_Start = list(range(2022,2026))
List_Day_Stop = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
List_Month_Stop = ("January","February","March","April","May","June","July","August","September","October","November","December")
List_Year_Stop = list(range(2022,2026))



#Function Section
def Submit():
    #Get Value of Variables
    Name_Surname = str(Name.get())
    Leave = Cause.get()
    Inform = Description.get()
    D_Start = Day_Start.get()
    M_Strat = Month_Start.get()
    Y_Start = Year_Start.get()
    D_Stop = Day_Stop.get()
    M_Stop = Month_Stop.get()
    Y_Stop = Year_Stop.get()


    #Create PDF
    My_PDF = FPDF()
    My_PDF.add_page()
    My_PDF.set_font("Arial", size = 16)
    My_PDF.cell(200, 10, txt = "BCC Absence Letter", ln = 1, align = "C")
    #Create text
    Text_0 = " "
    Text_1 = "Student Name - Surname:                       " + Name_Surname
    Text_2 = "I'm writing this letter to inform you that:   " + Leave
    Text_3 = "Absent from school on the following:          " + Inform
    Text_4 = "From:                                                       " + D_Start + "/" + M_Strat + "/" + Y_Start
    Text_5 = "To:                                                           " + D_Stop + "/" + M_Stop + "/" + Y_Stop

    #Align Text in PDF
    My_PDF.cell(200, 10, txt = Text_0, ln = 2, align = "L")
    My_PDF.cell(200, 10, txt = Text_1, ln = 3, align = "L")
    My_PDF.cell(200, 10, txt = Text_2, ln = 2, align = "L")
    My_PDF.cell(200, 10, txt = Text_3, ln = 3, align = "L")
    My_PDF.cell(200, 10, txt = Text_4, ln = 2, align = "L")
    My_PDF.cell(200, 10, txt = Text_5, ln = 3, align = "L")
    #PDF Output
    My_PDF.output(Name_Surname + "_Absent.pdf")
    #Messagebox Warning
    tkinter.messagebox.showinfo("Thank you","File has benn downloaded")








def Delete():
    Name.set("")
    Description.set("")




#Label Section
Label_1 = Label(text = "Absence Letter",font = Font_1,bg = Gold).grid(row = 0,column = 2)
Label_2 = Label(text = "Name-Surname",font = Font_1,bg = Grey).grid(row = 1,column = 0)
Label_3 = Label(text = "Leave",font = Font_1,bg = Grey).grid(row = 2,column = 0)
Label_4 = Label(text = "Cause",font = Font_1,bg = Grey).grid(row = 3,column = 0)
Label_5 = Label(text = "From",font = Font_1,bg = Grey).grid(row = 4,column = 0)
Label_6 = Label(text = "To",font = Font_1,bg = Grey).grid(row = 5,column = 0)
Label_7 = Label(text = " ",font = Font_1,bg = Purple).grid(row = 6,column = 0)
Label_8 = Label(text = " ",font = Font_1,bg = Purple).grid(row = 7,column = 0)


#Entry Section
Entry_1 = Entry(window,textvariable = Name,font = Font_2,bg = Grey,width = 10).grid(row = 1,column = 1)
Entry_2 = Entry(window,textvariable = Description,font = Font_2,bg = Grey,width = 10).grid(row = 3,column = 1)


#Combobox Section
Combo_1 = ttk.Combobox(textvariable = Cause,value = List_Cause,font = Font_3,width = 13).grid(row = 2,column = 1)
Combo_2 = ttk.Combobox(textvariable = Day_Start,value = List_Day_Start,font = Font_1,width = 10).grid(row = 4,column = 1)
Combo_3 = ttk.Combobox(textvariable = Month_Start,value = List_Month_Start,font = Font_1,width = 10).grid(row = 4,column = 2)
Combo_4 = ttk.Combobox(textvariable = Year_Start,value = List_Year_Start,font = Font_1,width = 10).grid(row = 4,column = 3)
Combo_5 = ttk.Combobox(textvariable = Day_Stop,value = List_Day_Stop,font = Font_1,width = 10).grid(row = 5,column = 1)
Combo_6 = ttk.Combobox(textvariable = Month_Stop,value = List_Month_Stop,font = Font_1,width = 10).grid(row = 5,column = 2)
Combo_7 = ttk.Combobox(textvariable = Year_Stop,value = List_Year_Stop,font = Font_1,width = 10).grid(row = 5,column = 3)

#Button Section
Button_1 = Button(text = "Submit",font = Font_1,bg = Grey,command = Submit).grid(row = 8,column = 1)
Button_2 = Button(text = "Clear",font = Font_1,bg = Grey,command = Delete).grid(row = 8,column = 3)


window.mainloop()