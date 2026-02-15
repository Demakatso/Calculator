import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg='#1a1a2e')
        
        # Create main frame
        main_frame = tk.Frame(root, bg='#1a1a2e', padx=10, pady=10)
        main_frame.grid(row=0, column=0)
        
        # Entry widget for display with modern styling
        self.entry = tk.Entry(
            main_frame, 
            width=16, 
            font=('Segoe UI', 28, 'bold'), 
            justify='right', 
            bd=0,
            bg='#16213e',
            fg='#ffffff',
            insertbackground='#00d9ff',
            relief='flat',
            highlightthickness=2,
            highlightbackground='#0f3460',
            highlightcolor='#00d9ff'
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=(5, 15), ipady=15)
        
        # Button configurations with different styles
        number_style = {
            'bg': '#16213e',
            'fg': '#ffffff',
            'activebackground': '#0f3460',
            'activeforeground': '#ffffff',
            'width': 5,
            'height': 2,
            'font': ('Segoe UI', 14, 'bold'),
            'bd': 0,
            'relief': 'flat',
            'cursor': 'hand2'
        }
        
        operator_style = {
            'bg': '#0f3460',
            'fg': '#00d9ff',
            'activebackground': '#1a1a2e',
            'activeforeground': '#00d9ff',
            'width': 5,
            'height': 2,
            'font': ('Segoe UI', 14, 'bold'),
            'bd': 0,
            'relief': 'flat',
            'cursor': 'hand2'
        }
        
        equals_style = {
            'bg': '#00d9ff',
            'fg': '#1a1a2e',
            'activebackground': '#00b8d4',
            'activeforeground': '#1a1a2e',
            'width': 5,
            'height': 2,
            'font': ('Segoe UI', 14, 'bold'),
            'bd': 0,
            'relief': 'flat',
            'cursor': 'hand2'
        }
        
        clear_style = {
            'bg': '#e94560',
            'fg': '#ffffff',
            'activebackground': '#c23b52',
            'activeforeground': '#ffffff',
            'width': 5,
            'height': 2,
            'font': ('Segoe UI', 14, 'bold'),
            'bd': 0,
            'relief': 'flat',
            'cursor': 'hand2'
        }
        
        # Button layout with styles
        buttons_layout = [
            ('7', number_style), ('8', number_style), ('9', number_style), ('/', operator_style),
            ('4', number_style), ('5', number_style), ('6', number_style), ('*', operator_style),
            ('1', number_style), ('2', number_style), ('3', number_style), ('-', operator_style),
            ('C', clear_style), ('0', number_style), ('=', equals_style), ('+', operator_style),
            ('^', operator_style), ('√', operator_style), ('%', operator_style), ('⌫', clear_style)
        ]
        
        row_val = 1
        col_val = 0
        
        for button_text, style in buttons_layout:
            if button_text == '=':
                btn = tk.Button(main_frame, text=button_text, command=self.calculate, **style)
            elif button_text == 'C':
                btn = tk.Button(main_frame, text=button_text, command=self.clear, **style)
            elif button_text == '⌫':
                btn = tk.Button(main_frame, text=button_text, command=self.backspace, **style)
            elif button_text == '√':
                btn = tk.Button(main_frame, text=button_text, command=self.sqrt_operation, **style)
            elif button_text == '^':
                btn = tk.Button(main_frame, text=button_text, command=lambda: self.click('**'), **style)
            else:
                btn = tk.Button(main_frame, text=button_text, command=lambda b=button_text: self.click(b), **style)
            
            # Add hover effect
            self.add_hover_effect(btn, style)
            
            btn.grid(row=row_val, column=col_val, padx=3, pady=3, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        # Make buttons expand proportionally
        for i in range(4):
            main_frame.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            main_frame.grid_rowconfigure(i, weight=1)
    
    def add_hover_effect(self, button, original_style):
        """Add hover effect to buttons."""
        def on_enter(e):
            if original_style['bg'] == '#16213e':  # number buttons
                button['bg'] = '#1e2e4a'
            elif original_style['bg'] == '#0f3460':  # operator buttons
                button['bg'] = '#1a4a7a'
            elif original_style['bg'] == '#00d9ff':  # equals button
                button['bg'] = '#00b8d4'
            elif original_style['bg'] == '#e94560':  # clear/backspace
                button['bg'] = '#c23b52'
        
        def on_leave(e):
            button['bg'] = original_style['bg']
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
    
    def click(self, value):
        """Append the clicked button's value to the entry."""
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + str(value))
    
    def clear(self):
        """Clear the entry."""
        self.entry.delete(0, tk.END)
    
    def backspace(self):
        """Remove the last character."""
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])
    
    def calculate(self):
        """Evaluate the expression safely."""
        expression = self.entry.get()
        try:
            # Replace common mathematical symbols
            expression = expression.replace('^', '**')
            
            # Use eval with restricted namespace for safety
            result = eval(expression, {"__builtins__": {}}, {"math": math})
            
            self.entry.delete(0, tk.END)
            # Format result to remove unnecessary decimals
            if isinstance(result, float) and result.is_integer():
                self.entry.insert(0, str(int(result)))
            else:
                self.entry.insert(0, str(round(result, 10)))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
    
    def sqrt_operation(self):
        """Compute square root of the current number."""
        try:
            value = float(self.entry.get())
            if value < 0:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
            else:
                result = math.sqrt(value)
                self.entry.delete(0, tk.END)
                if result.is_integer():
                    self.entry.insert(0, str(int(result)))
                else:
                    self.entry.insert(0, str(round(result, 10)))
        except (ValueError, TypeError):
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()