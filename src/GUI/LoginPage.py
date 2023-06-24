import sys
from functools import partial
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

import GUI.test_support as test_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = LoginPage (root)
    test_support.init(root, top)
    root.mainloop()

w = None
def create_LoginPage(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = LoginPage (w)
    test_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_LoginPage():
    global w
    w.destroy()
    w = None

class LoginPage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 14 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("388x258+555+144")
        top.title("Login")
        top.configure(background="#fafeff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.configure(width="1000")

        self.UsernamePrompt = tk.Label(top)
        self.UsernamePrompt.place(relx=0.026, rely=0.194, height=51, width=154)
        self.UsernamePrompt.configure(activebackground="#9b3cef")
        self.UsernamePrompt.configure(activeforeground="white")
        self.UsernamePrompt.configure(activeforeground="#000000")
        self.UsernamePrompt.configure(background="#d9d9d9")
        self.UsernamePrompt.configure(disabledforeground="#a3a3a3")
        self.UsernamePrompt.configure(font=font9)
        self.UsernamePrompt.configure(foreground="#000000")
        self.UsernamePrompt.configure(highlightbackground="#d9d9d9")
        self.UsernamePrompt.configure(highlightcolor="black")
        self.UsernamePrompt.configure(text='''Username:''')

        self.PasswordPrompt = tk.Label(top)
        self.PasswordPrompt.place(relx=0.026, rely=0.388, height=51, width=154)
        self.PasswordPrompt.configure(activebackground="#30ef00")
        self.PasswordPrompt.configure(activeforeground="#000000")
        self.PasswordPrompt.configure(background="#d9d9d9")
        self.PasswordPrompt.configure(disabledforeground="#a3a3a3")
        self.PasswordPrompt.configure(font=font9)
        self.PasswordPrompt.configure(foreground="#000000")
        self.PasswordPrompt.configure(highlightbackground="#d9d9d9")
        self.PasswordPrompt.configure(highlightcolor="black")
        self.PasswordPrompt.configure(text='''Password:''')

        self.USERNAME_FIELD = tk.Text(top)
        self.USERNAME_FIELD.place(relx=0.438, rely=0.233, relheight=0.132
                , relwidth=0.5)
        self.USERNAME_FIELD.configure(background="white")
        self.USERNAME_FIELD.configure(font="TkTextFont")
        self.USERNAME_FIELD.configure(foreground="black")
        self.USERNAME_FIELD.configure(highlightbackground="#d9d9d9")
        self.USERNAME_FIELD.configure(highlightcolor="black")
        self.USERNAME_FIELD.configure(insertbackground="black")
        self.USERNAME_FIELD.configure(selectbackground="#c4c4c4")
        self.USERNAME_FIELD.configure(selectforeground="black")
        self.USERNAME_FIELD.configure(width=194)
        self.USERNAME_FIELD.configure(wrap='word')

        self.PASSWORD_FIELD = tk.Text(top)
        self.PASSWORD_FIELD.place(relx=0.438, rely=0.426, relheight=0.132
                , relwidth=0.5)
        self.PASSWORD_FIELD.configure(background="white")
        self.PASSWORD_FIELD.configure(font="TkTextFont")
        self.PASSWORD_FIELD.configure(foreground="black")
        self.PASSWORD_FIELD.configure(highlightbackground="#d9d9d9")
        self.PASSWORD_FIELD.configure(highlightcolor="black")
        self.PASSWORD_FIELD.configure(insertbackground="black")
        self.PASSWORD_FIELD.configure(selectbackground="#c4c4c4")
        self.PASSWORD_FIELD.configure(selectforeground="black")
        self.PASSWORD_FIELD.configure(width=194)
        self.PASSWORD_FIELD.configure(wrap='word')

        self.LoginButton = ttk.Button(top)
        self.LoginButton.place(relx=0.387, rely=0.698, height=25, width=76)
        self.LoginButton.configure(command=lambda: test_support.login(self.USERNAME_FIELD.get("1.0", "end-1c"),self.PASSWORD_FIELD.get("1.0","end-1c")));
        self.LoginButton.configure(takefocus="")
        self.LoginButton.configure(text='''Login''')
    def text(self,textBoxName):
        return textBoxName;
if __name__ == '__main__':
    vp_start_gui()