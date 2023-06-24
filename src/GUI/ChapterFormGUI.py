import sys
from tkinter import IntVar

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI.tempsel_support as tempsel_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    tempsel_support.set_Tk_var()
    top = Toplevel1 (root)
    tempsel_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    tempsel_support.set_Tk_var()
    top = Toplevel1 (w)
    tempsel_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 15 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI Black} -size 14 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 18 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("600x450+650+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        self.C0V,self.C1V,self.C2V,self.C3V,self.C4V,self.C5V,self.C6V= [IntVar() for i in range(0,7)];
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.317, rely=0.067, height=38, width=203)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Choose Chapters:''')

        self.C0 = tk.Checkbutton(top,variable = self.C0V)
        self.C0.place(relx=0.1, rely=0.222, relheight=0.091, relwidth=0.188)
        self.C0.configure(activebackground="#d9d9d9")
        self.C0.configure(activeforeground="#000000")
        self.C0.configure(background="#d9d9d9")
        self.C0.configure(disabledforeground="#a3a3a3")
        self.C0.configure(font=font10)
        self.C0.configure(foreground="#000000")
        self.C0.configure(highlightbackground="#d9d9d9")
        self.C0.configure(highlightcolor="black")
        self.C0.configure(justify='left')
        self.C0.configure(text='''Vectors''')
        #self.C0.configure(variable=tempsel_support.che44)
        self.C0.configure(width=113)

        self.C1 = tk.Checkbutton(top,variable = self.C1V)
        self.C1.place(relx=0.092, rely=0.311, relheight=0.091, relwidth=0.388)
        self.C1.configure(activebackground="#d9d9d9")
        self.C1.configure(activeforeground="#000000")
        self.C1.configure(background="#d9d9d9")
        self.C1.configure(disabledforeground="#a3a3a3")
        self.C1.configure(font=font10)
        self.C1.configure(foreground="#000000")
        self.C1.configure(highlightbackground="#d9d9d9")
        self.C1.configure(highlightcolor="black")
        self.C1.configure(justify='left')
        self.C1.configure(text='''Units And Dimenions''')
        #self.C1.configure(variable=tempsel_support.che44)
        self.C1.configure(width=233)

        self.C3 = tk.Checkbutton(top,variable = self.C3V)
        self.C3.place(relx=0.583, rely=0.222, relheight=0.091, relwidth=0.272)
        self.C3.configure(activebackground="#d9d9d9")
        self.C3.configure(activeforeground="#000000")
        self.C3.configure(background="#d9d9d9")
        self.C3.configure(disabledforeground="#a3a3a3")
        self.C3.configure(font=font10)
        self.C3.configure(foreground="#000000")
        self.C3.configure(highlightbackground="#d9d9d9")
        self.C3.configure(highlightcolor="black")
        self.C3.configure(justify='left')
        self.C3.configure(text='''Motion in 2D''')
        #self.C3.configure(variable=tempsel_support.che44)
        self.C3.configure(width=163)

        self.C4 = tk.Checkbutton(top,variable = self.C4V)
        self.C4.place(relx=0.583, rely=0.311, relheight=0.091, relwidth=0.305)
        self.C4.configure(activebackground="#d9d9d9")
        self.C4.configure(activeforeground="#000000")
        self.C4.configure(background="#d9d9d9")
        self.C4.configure(disabledforeground="#a3a3a3")
        self.C4.configure(font=font10)
        self.C4.configure(foreground="#000000")
        self.C4.configure(highlightbackground="#d9d9d9")
        self.C4.configure(highlightcolor="black")
        self.C4.configure(justify='left')
        self.C4.configure(text='''Laws of Motion''')
        #self.C4.configure(variable=tempsel_support.che44)
        self.C4.configure(width=183)

        self.C5 = tk.Checkbutton(top,variable = self.C5V)
        self.C5.place(relx=0.583, rely=0.4, relheight=0.091, relwidth=0.438)
        self.C5.configure(activebackground="#d9d9d9")
        self.C5.configure(activeforeground="#000000")
        self.C5.configure(background="#d9d9d9")
        self.C5.configure(disabledforeground="#a3a3a3")
        self.C5.configure(font=font10)
        self.C5.configure(foreground="#000000")
        self.C5.configure(highlightbackground="#d9d9d9")
        self.C5.configure(highlightcolor="black")
        self.C5.configure(justify='left')
        self.C5.configure(text='''Work,Power and Energy''')
        #self.C5.configure(variable=tempsel_support.che44)
        self.C5.configure(width=263)

        self.C2 = tk.Checkbutton(top,variable = self.C2V)
        self.C2.place(relx=0.1, rely=0.4, relheight=0.091, relwidth=0.272)
        self.C2.configure(activebackground="#d9d9d9")
        self.C2.configure(activeforeground="#000000")
        self.C2.configure(background="#d9d9d9")
        self.C2.configure(disabledforeground="#a3a3a3")
        self.C2.configure(font=font10)
        self.C2.configure(foreground="#000000")
        self.C2.configure(highlightbackground="#d9d9d9")
        self.C2.configure(highlightcolor="black")
        self.C2.configure(justify='left')
        self.C2.configure(text='''Motion in 1D''')
        #self.C2.configure(variable=tempsel_support.che44)
        self.C2.configure(width=163)

        self.C6 = tk.Checkbutton(top,variable = self.C6V)
        self.C6.place(relx=0.35, rely=0.511, relheight=0.091, relwidth=0.388)
        self.C6.configure(activebackground="#d9d9d9")
        self.C6.configure(activeforeground="#000000")
        self.C6.configure(background="#d9d9d9")
        self.C6.configure(disabledforeground="#a3a3a3")
        self.C6.configure(font=font10)
        self.C6.configure(foreground="#000000")
        self.C6.configure(highlightbackground="#d9d9d9")
        self.C6.configure(highlightcolor="black")
        self.C6.configure(justify='left')
        self.C6.configure(text='''Rotation''')
        #self.C6.configure(variable=tempsel_support.che44)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.133, rely=0.711, height=34, width=149)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Learning Rate:''')
        self.Label2.configure(width=149)

        self.rate = tk.Text(top)
        self.rate.place(relx=0.383, rely=0.711, relheight=0.076, relwidth=0.107)
        self.rate.configure(background="white")
        self.rate.configure(font=font10)
        self.rate.configure(foreground="black")
        self.rate.configure(highlightbackground="#d9d9d9")
        self.rate.configure(highlightcolor="black")
        self.rate.configure(insertbackground="black")
        self.rate.configure(selectbackground="#c4c4c4")
        self.rate.configure(selectforeground="black")
        self.rate.configure(width=64)
        self.rate.configure(wrap='word')

        self.Start = tk.Button(top)
        self.Start.place(relx=0.767, rely=0.844, height=42, width=80)
        self.Start.configure(activebackground="#d9d9d9")
        self.Start.configure(activeforeground="#000000")
        self.Start.configure(background="#3ad86f")
        self.Start.configure(command=lambda: tempsel_support.startProg([[0,self.C0V.get()],[1,self.C1V.get()],[2,self.C2V.get()],[3,self.C3V.get()],[4,self.C4V.get()],[5,self.C5V.get()],[6,self.C6V.get()]]))
        self.Start.configure(disabledforeground="#a3a3a3")
        self.Start.configure(font=font11)
        self.Start.configure(foreground="#000000")
        self.Start.configure(highlightbackground="#d8cfcf")
        self.Start.configure(highlightcolor="#000000")
        self.Start.configure(pady="0")
        self.Start.bind("<Enter>", lambda x: self.setColor(self.Start,"#25d8a8"));
        self.Start.bind("<Leave>", lambda x: self.setColor(self.Start,"#3ad86f"))
        self.Start.configure(text='''START''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
    def setColor(self,itemName,Color):
        itemName.configure(background=Color);
        
if __name__ == '__main__':
    vp_start_gui()