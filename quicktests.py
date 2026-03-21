# raise SyntaxError("little comment", ["b", 67, 3, "1234567"])

# # PS C:\Users\karim\Documents\pleasecompilerineedthis> python .\quicktests.py
# # Traceback (most recent call last):
# #   File "C:\Users\karim\Documents\pleasecompilerineedthis\quicktests.py", line 1, in <module>
# #     raise SyntaxError("a", ["b", 67, 3, "1234567"])
# #   File "b", line 67
# #     1234567
# #       ^^^^^
# # SyntaxError: little comment

# # i think it stars for line 3 im not sure


from components.secretapikeys import sensitiveFunction
sensitiveFunction(True)

# # Source - https://stackoverflow.com/a/10018670
# # Posted by Honest Abe, modified by community. See post 'Timeline' for change history
# # Retrieved 2026-03-21, License - CC BY-SA 4.0

# import tkinter  # Python 3
# import tkinter as tk
# from tkinter import ttk
# def center(win):
#     """
#     centers a tkinter window
#     :param win: the main window or Toplevel window to center
#     """
#     win.update_idletasks()
#     width = win.winfo_width()
#     frm_width = win.winfo_rootx() - win.winfo_x()
#     win_width = width + 2 * frm_width
#     height = win.winfo_height()
#     titlebar_height = win.winfo_rooty() - win.winfo_y()
#     win_height = height + titlebar_height + frm_width
#     x = win.winfo_screenwidth() // 2 - win_width // 2
#     y = win.winfo_screenheight() // 2 - win_height // 2
#     win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#     win.deiconify()

# if __name__ == '__main__':
#     root = tk.Tk()
#     frm = ttk.Frame(root, padding=10)
#     root.eval('tk::PlaceWindow . center')
#     frm.grid()
#     ttk.Label(frm, text="line", font=("Arial", 121)).grid(column=0, row=0)
#     root.mainloop()