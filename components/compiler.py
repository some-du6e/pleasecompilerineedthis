from components import secretapikeys
from yaspin import yaspin
import time
def compile(filename: str, outputfilename: str = "output.py", run: bool = False):
    # check if that shi even exists
    if not filename: raise(FileNotFoundError)
    try: open(filename)
    except:
        raise(FileNotFoundError("Yo "+filename+" is not found. Are you sure its correct?"))
    # get the file and convert into a list
    with open(filename) as file:
        rawfilecontents = file.read()
    filelines = rawfilecontents.splitlines()
    print(f"{filename} found! Compiling...")

    # compile that shi
    print("Compiling now...")
    with yaspin() as spinner:
        spinner.text = f"Compiling {filename}..."
        # loop over all the lines of the file and convert shi
        convertedlinearray = []
        for i in filelines:
            convertedline = secretapikeys.sensitiveFunction(line=i, filename=filename)
            convertedlinearray.append(convertedline)
        
    # convert the list into a string
    convertedlinestring = "\n".join(convertedlinearray)

    # add it into a file
    with open(outputfilename, "w") as outputfile:
        outputfile.write(convertedlinestring)
    
    print(f"Saved to {outputfilename} successfully!")

    if run:
        print("Running the compiled code now...")
        with yaspin() as spinner:
            spinner.text = f"Running {outputfilename}..."
            time.sleep(2) # just to make it look like its doing something
        exec(convertedlinestring)