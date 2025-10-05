# Simple Calculator 

import tkinter as tk

SMALL_FONT_STYLE = ("Arial",16)
LARGE_FONT_STYLE = ("Arial",40,"bold")
DIGIT_FONT_STYLE = ("Arial",24,"bold")
DEFAULT_FONT_STYLE = ("Arial",20)
OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_GREY = "#F5F5F5"
LABEL_COLOR = '#25265E'
LIGHT_BLUE = "#CCEDFF"
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        self.TotalExp=""
        self.CurrentExp=""
        self.DisplayFrame = self.CreateDisplayFrame()

        self.l1, self.l2 = self.CreateDisplayLabel()

        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,1),'.':(4,2)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.ButtonFrame = self.CreateButtonFrame()

        self.ButtonFrame.columnconfigure(0,weight=0)

        for x in range(1,5):
            self.ButtonFrame.rowconfigure(x,weight=1)
            self.ButtonFrame.columnconfigure(x,weight=1)
        
        self.CreateDigitButton()
        self.CreateOperatorButton()
        self.CreateClearButton()
        self.CreateEqualButton()

    def run(self):
        self.window.mainloop()

    def CreateDisplayLabel(self):
        l1 = tk.Label(self.DisplayFrame, text=self.TotalExp, anchor=tk.E, bg=LIGHT_GREY,fg=LABEL_COLOR,font=SMALL_FONT_STYLE,padx=24)
        l1.pack(expand=True,fill="both")
        l2 = tk.Label(self.DisplayFrame, text=self.CurrentExp, anchor=tk.E, bg=LIGHT_GREY,fg=LABEL_COLOR,font=LARGE_FONT_STYLE,padx=24)
        l2.pack(expand=True,fill="both")
        return l1,l2

    def UpdateTotalLabel(self):
        self.l1.config(text=self.TotalExp)

    def UpdateCurrentLabel(self):
        self.l2.config(text=self.CurrentExp)
    

    def CreateDisplayFrame(self):
        df = tk.Frame(self.window, height=221,bg=LIGHT_GREY)
        df.pack(expand=True,fill="both")
        return df
    
    def CreateButtonFrame(self):
        bf = tk.Frame(self.window)
        bf.pack(expand=True,fill="both")
        return bf

    def AddToExpression(self,value):
        self.CurrentExp += str(value)
        self.UpdateCurrentLabel()

    def CreateDigitButton(self):
        for digit,gridValue in self.digits.items():
            button = tk.Button(self.ButtonFrame, text=str(digit),bg=WHITE,font=DIGIT_FONT_STYLE,borderwidth=0,command=lambda x=digit: self.AddToExpression(x))
            button.grid(row=gridValue[0],column=gridValue[1],sticky=tk.NSEW)
    
    def AppendOperator(self,operator):
        self.CurrentExp += operator
        self.TotalExp += self.CurrentExp
        self.CurrentExp = ""
        self.UpdateTotalLabel()
        self.UpdateCurrentLabel()

    def CreateOperatorButton(self):
        i=0
        for oper,symbols in self.operations.items():
            button=tk.Button(self.ButtonFrame, text=symbols,bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0,command=lambda x=oper: self.AppendOperator(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    
    def ClearOper(self):
        self.CurrentExp=""
        self.TotalExp=""
        self.UpdateCurrentLabel()
        self.UpdateTotalLabel()

    def CreateClearButton(self):
        button=tk.Button(self.ButtonFrame, text="C",bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0,command=lambda: self.ClearOper())
        button.grid(row=0,column=1,columnspan=3,sticky=tk.NSEW)

    def EvalOper(self):
        self.TotalExp += self.CurrentExp
        self.UpdateTotalLabel()
        self.CurrentExp = str(eval(self.TotalExp))
        self.TotalExp=""
        self.UpdateCurrentLabel()

    def CreateEqualButton(self):
        button=tk.Button(self.ButtonFrame, text="=",bg=LIGHT_BLUE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0,command=lambda:self.EvalOper())
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)

if __name__=='__main__':
    app = Calculator() 
    app.run()