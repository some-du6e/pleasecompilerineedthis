def errorandstacktracemaybe(error: str):
    return error

def evaluatefr(line: str, filename: str = "not defined!"):
    # check if that shi is alr done
    if line.startswith("print") or "input" in line:
        return line
    # really long if statement im sorry
    if line.startswith("log"):
        return line.replace("log", "print")
    elif line.startswith("plz "): # do plz first cuz of the ask thing
        return line.replace("plz ", "")
    elif line.startswith("ask ") or "ask(" in line:
        return line.replace("ask", "input")
    else:
        raise SyntaxError(errorandstacktracemaybe("SyntaxError: "+line), [filename, 0, 0, line])
    



def plstopython(line: str, filename: str = "not defined!"):
    """ONLY 1 LINE AT A TIME"""
    if "ask(" in line:
        # repeat that shi twice
        evalutedline = line
        for i in range(2):
            evalutedline = evaluatefr(evalutedline, filename)
        
        return evalutedline
    
    evalutedline = evaluatefr(line, filename)
    return evalutedline
