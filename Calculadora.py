from tkinter import *;
from tkinter import messagebox;

def actionauthor():
    messagebox.showinfo("Autor", "Pedro Ribeiro")

def is_number(s):
    if(s != ''):
        if (s.replace('.', '', 1).isdigit()):
            return True
        if (s.isdigit()):
            return True;
        if s[0] in ['-', '+', '.', '0', ' ']:
            if (s[1] == '.'):
                if (s[2:].isdigit()):
                    return True
            if (s[1] == '0' and s[2] == '.'):
                if (s[3:].isdigit()):
                    return True
            if s[1:].isdigit():
                return True;
        return False;

def casting(num):
    if('.' in num):
        return float(num);
    else:
        return int(num)


#Função de sinal de mais
def actionPlus():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='red', bg='#9ed8ee')
    Showtemplabel.insert(0, 'Soma');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')
    ans = "0";
    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();

    if(is_number(num1) == True and is_number(num2) == True and num1 != ' ' and num2 != ' '):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 + num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='white', bg='#000000')
        Showtemplabel.insert(0, 'Soma');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Erro"," Digite um número válido\ne.g. 123, 0.123, .123, -0.123, 123.456")

#Função de sinal de menos
def actionMinus():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='white', bg='#000000')
    Showtemplabel.insert(0, 'Subtração');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0";

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();

    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 - num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='white', bg='#000000')
        Showtemplabel.insert(0, 'Subtração');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Erro"," Digite um número válido\ne.g. 123, 0.123, .123, -0.123, 123.456")

#Função de sinal de multiplicação
def actionMul():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='white', bg='#000000')
    Showtemplabel.insert(0, 'Multiplicação');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();
    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 * num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='white', bg='#000000')
        Showtemplabel.insert(0, 'Multiplicação');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Erro"," Digite um número válido\ne.g. 123, 0.123, .123, -0.123, 123.456")

#Divisão
def actionDiv():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='white', bg='#000000')
    Showtemplabel.insert(0, 'Divisão');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();
    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 / num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='white', bg='#000000')
        Showtemplabel.insert(0, 'Division');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
       messagebox.showerror("Erro"," Digite um número válido\ne.g. 123, 0.123, .123, -0.123, 123.456")

root = Tk();
root.title('Minha primeira calculadora Python');
root.geometry('380x300+200+250');
Titlelabel = Label(root, fg = 'green' , font = 'none 10 bold underline' ,text = 'Calculadora Python', compound = CENTER)
Titlelabel.place(relx=0.5, rely=0.1, anchor='center')
Showlabel = Entry(root);
Showtemplabel = Entry(root);
Numberentry1 = Entry(root);
Numberentry2 = Entry(root);
Numberentry1.place(relx=0.5, rely=0.3, anchor='center')
Numberentry2.place(relx=0.5, rely=0.4, anchor='center')

plusbutton = Button(root, text="+", width = 5, command = actionPlus);
plusbutton.place(relx=0.1, rely=0.7)

minusbutton = Button(root, text="-", width = 5, command = actionMinus);
minusbutton.place(relx=0.3, rely=0.7)

mulbutton = Button(root, text="*", width = 5, command = actionMul);
mulbutton.place(relx=0.5, rely=0.7)

divbutton = Button(root, text="/", width = 5, command = actionDiv);
divbutton.place(relx=0.7, rely=0.7)

authorbutton = Button(root, text='Autor', width=6, command = actionauthor);
authorbutton.place(relx = 0.5, rely=0.95, anchor='center');

root.resizable(False, False);
root.mainloop();