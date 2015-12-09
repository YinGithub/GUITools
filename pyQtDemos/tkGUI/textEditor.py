import Tkinter as tk




class textEditor():
    def __init__(self):
        self.root = tk.Tk()
        # config main window 
        #self.root.minsize(500,500)
        self.root.title('notePad')
        self.root.rowconfigure(0,weight = 1)
        self.root.columnconfigure(0, weight = 1)
        # control layout 
        self._layout()
        self.root.mainloop()
        
    def _layout(self):
        f1  = tk.Frame(self.root)
        f1.grid(column = 0,row = 0,sticky=tk.E +tk.N +tk.S + tk.W)
        
        f1.rowconfigure(0, weight = 1)
        f1.rowconfigure(1, weight = 200)
        
        f1.columnconfigure(0,weight = 1)
        f1.columnconfigure(1,weight = 1)
        f1.columnconfigure(2,weight = 1)
        f1.columnconfigure(3,weight = 60)
        
        # row 1
        mb1 = tk.Menubutton(f1,text = 'File',height = 1,relif = tk.RAISED)
        mb1.menu  = tk.Menu(self.mb1, tearoff=0)
        
self.mb.menu = tk.Menu(self.mb, tearoff=0)
self.mb['menu'] = self.mb.menu
self.mayoVar = tk.IntVar()
self.ketchVar = tk.IntVar()
self.mb.menu.add_checkbutton(label='mayo',
variable=self.mayoVar)
self.mb.menu.add_checkbutton(label='ketchup',
variable=self.ketchVar)
        
        
        
        
        
        mb2 = tk.Menubutton(f1,text = 'mb2')
        mb3 = tk.Menubutton(f1,text = 'mb3')
        mb1.grid(column = 0,row = 0)
        mb2.grid(column = 1,row = 0)
        mb3.grid(column = 2,row = 0)
        
        # row 2
        t1 = tk.Text(f1)
        t1.grid(column = 0,row = 1, columnspan = 4,sticky=tk.E +tk.N +tk.S + tk.W)
        
            
    def layout(self):

        f1  =  tk.Frame(self.root,bg = 'green')
        mb1 = tk.Menubutton(f1,text = 'mb1')
        mb2 = tk.Menubutton(f1,text = 'mb2')
        mb3 = tk.Menubutton(f1,text = 'mb3')

        
        f2 =  tk.Frame(self.root,bg  = 'black')
        #t1 = tk.Text(f2)
        t1 =  tk.Label(f2,bg = 'blue')
        # Grid
        f1.grid(row = 0,column = 0,sticky=tk.E+tk.N + tk.W)
        f2.grid(row = 1,column = 0,sticky=tk.E+tk.S+ tk.W)
        f2.columnconfigure(0, weight =  1)
        

        
        # menuButton
        mb1.grid(row = 0, column = 0)
        mb2.grid(row = 0, column = 1)
        mb3.grid(row = 0, column = 2)
        
        # text 
        t1.grid(row = 0,column = 0,sticky=tk.E +tk.N +tk.S + tk.W)
        print 'f1: ',f1.grid_size()
        print 'f2: ',f2.grid_size()
        print 'root ',self.root.grid_size()
        
        
        
if __name__ == '__main__':
    text = textEditor()
    