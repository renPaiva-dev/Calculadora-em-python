from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        buttons = [
            ('(', 0, 50), (')', 90, 50), ('%', 180, 50), ('/', 270, 50),
            ('7', 0, 125), ('8', 90, 125), ('9', 180, 125), ('*', 270, 125),
            ('4', 0, 200), ('5', 90, 200), ('6', 180, 200), ('-', 270, 200),
            ('1', 0, 275), ('2', 90, 275), ('3', 180, 275), ('+', 270, 275),
            ('C', 0, 350), ('0', 90, 350), ('.', 180, 350), ('=', 270, 350),
        ]

        for (text, x, y) in buttons:
            if text == 'C':
                Button(master, width=11, height=4, text=text, relief='flat', bg='white', command=self.clear).place(x=x, y=y)
            elif text == '=':
                Button(master, width=11, height=4, text=text, relief='flat', bg='white', command=self.solve).place(x=x, y=y)
            else:
                Button(master, width=11, height=4, text=text, relief='flat', bg='white', command=lambda t=text: self.show(t)).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            expression = self.entry_value.replace('%', '/100')
            result = eval(expression)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()
