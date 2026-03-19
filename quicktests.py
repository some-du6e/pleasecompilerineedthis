raise SyntaxError("little comment", ["b", 67, 3, "1234567"])

# PS C:\Users\karim\Documents\pleasecompilerineedthis> python .\quicktests.py
# Traceback (most recent call last):
#   File "C:\Users\karim\Documents\pleasecompilerineedthis\quicktests.py", line 1, in <module>
#     raise SyntaxError("a", ["b", 67, 3, "1234567"])
#   File "b", line 67
#     1234567
#       ^^^^^
# SyntaxError: little comment

# i think it stars for line 3 im not sure