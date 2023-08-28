import tkinter as tk

LIGHT_GREY = "#F5F5F5"
LABLE_COLOR = "#25265E"
WHITE = '#FFFFFF'
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = "#1E90FF"


SMALL_FONT_SIZE = ("Arial", 16)
LARGE_FONT_SIZE = ("Arial", 40)
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(True, True)
        self.window.title("Calculator")
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_expression = '0'
        self.regular_expression = '0'
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '.': (4, 1), 0: (4, 2)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=2)
            self.buttons_frame.columnconfigure(x,weight=2)

        self.create_display_label()
        self.create_digit_buttons()
        self.create_operator_button()
        self.create_special_button()
    
    def create_special_button(self):
        self.clear_buttons=self.create_clear_buttons()
        self.equal_buttons=self.create_equal_buttons()


    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GREY,
                               fg=LABLE_COLOR, padx=24, font=SMALL_FONT_SIZE)
        total_label.pack(expand=True, fill="both")

        regular = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GREY,
                           fg=LABLE_COLOR, padx=24, font=LARGE_FONT_SIZE)
        regular.pack(expand=True, fill="both")

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GREY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABLE_COLOR, font=DIGIT_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
    
    def create_clear_buttons(self):
        
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABLE_COLOR, font=DIGIT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=[0], column=[0], columnspan=4,sticky=tk.NSEW)
        return button 
    
    def create_equal_buttons(self):
        
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABLE_COLOR, font=DIGIT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=[4], column=[3], columnspan=4,sticky=tk.NSEW)
        return button 

    def create_operator_button(self):
        i=0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABLE_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
# ksduhfk

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
