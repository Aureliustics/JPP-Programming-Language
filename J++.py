'''
Information: 
Tokens are like building blocks that are recognized by the interpreter. They get grouped into 5 categories: identifiers (Like variables),
keywords (stuff like if, else, return, pass), literals (integers, strings, and booleans), operators (mathematical, comparison, and logical operators like +, -, ==, !=)
delimiters (like semicolons, brackets, commas) <- we will be using this to split input into individual object tokens
and for whitespace and comments the interpreter will just cut it out from compiled form.
Inside of our interpreter, we will have a lexer (It will take in the commandline input and turn it into a list of tokens)
We will then put the lexer output into a parser which will remove whitespace and comments, group tokens into individual instructions 
(the source code will end up being 1 line at this stage and is now ready to be inputted by the evaluator)
The evaluator will translate J++ tokens into py commands in codehs. We will do this by using functions that can passthrough values via parameters.

syntax for J++:
1. use ; at the end of every codeblock
2. for multiple line, put ; at the end of each line
3. use () for stuff like move, degrees. There is also direction and alignment for second parameter. Example: move(50, forward); or square(100, center);
4. for mathematical operations, just type the operation like 1+1 or 8*5 and it will be evaluated
5. for loops do:
loop(number here){
    code here
}
6. For comments, the start of # is a comment, to end it put # at the end of the comment. 
Example: # Cool comment! #. You can comment code by putting it inbetween hashtags: # jout< "Help im commented out!" #

Essentially a visual of how it will work: https://accu.org/journals/overload/26/145/balaam_2510/1.png

[!] You can ignore above this was just for me to visualize the project before I started working on it.
'''
import re
speed(0)

def concatXPos():
    fetchXY = str(pos())
    fetchXY = fetchXY[1:] # remove first character which is "("
    subX = fetchXY.split(".")[0] # splits the string into two at the comma, then only take in the first part
    outputX = subX.replace(".", "") # now remove the comma by replacing comma with nothing
    return int(outputX)
    pass

def concatYPos():
    fetchXY = str(pos())
    subY = fetchXY.split(" ")[1][:-1] # splits the string into two at the space after the comma, then only take in the second part
    outputY = subY.split(".")[0] # splits after the decimal point and picks the first cut
    return int(outputY)
    pass

stored_variables = { # wont be using this because using a dict to store variables will only allow for a finite amount of vars. Will likely use a class to handle variables as objects. also allows for appending new vars, editing var names and values.
    'var1': None,
    'var2': None,
    'var3': None,
    'var4': None,
    'var5': None
}

def comment_handler(callback):
    output = []
    Comment = False  # check if inside comment
    
    for current_char in callback:
        if current_char == '#':
            Comment = True
        elif current_char == '#':
            Comment = False
        elif not Comment:
            output.append(current_char)
    return ''.join(output)

class interpreter: # class for input handling
    def __init__(self, value): # when you create a class in py it will always run __init__ function, this initialized the object and handles the inputs
        self.value = value
        
source_code = input("[J++]: ")
fetchedInput = interpreter(source_code) # pass in

def lexer(fetchedToken):
    #fetchedToken = fetchedToken.replace(" ", "") # whitespace is fine for now
    fetchedToken = comment_handler(fetchedToken) # prevents comments from being evaluated
    tokenOutput = " ".join(fetchedToken.strip() for fetchedToken in fetchedToken.splitlines()) # turns into 1 line
    return str(tokenOutput)
jpp_parsed = lexer(fetchedInput.value)
#print(jpp_parsed)

def available_vars(value): # value will be the value we pass into an available variable
    global stored_variables
    for i in stored_variables: # loop through stored_variables dict
        if stored_variables[i] is None: # check if current stored variable is None
            stored_variables[i] = value # set the value of the variable to the value the user entered
            return value
            break # stop after first available variable changed
        
class variable_handler:
    def __init__(self, value): # create an instance of this class, make init return None
        # in future append new variables as objects to this class, which will let you get and set variable name and data
        pass

def jout(value):
    global stored_variables
    #print_value = value[2:-2] # removes the [''] that re module adds
    if isinstance(value, str) is False: # check if its printing a string
        print_value = value[0] if isinstance(value, list) else value # since re.findall(r'"(.*?)"', fetchedToken) returns a list. this makes it so if the first node of the value is a list, only the first element is printed aka our expected print value
        print("[J++ Interpreter]: " + str(print_value))
    elif isinstance(value, str) is True: # if its printing a variable
        print("var here") # this doesnt work yet, not variable support added unfortunately.
    
def jin(value): # value is just the variable
    value = value.split(" ")[0] # cuts endl
    setVariable = input("[J++]: Listening for variable " + str(value) + ": ")
    print(str(value) + " set to " + str(setVariable))
    temp = available_vars(setVariable)
    return str(setVariable)
    
def move(value, direction): # value will be the distance in pixels tracy moves
    if str(direction.lower()) == "forward":
        old_dist_X = concatXPos()
        old_dist_Y = concatYPos()
        value = value[:-1]
        setposition(old_dist_X + (int(value) * 10), old_dist_Y)
        new_dist_X = concatXPos()
        new_dist_Y = concatYPos()
        print("Moved from " + "(" + str(old_dist_X) + "x " + str(old_dist_Y) + "y) " + "to " + "(" + str(new_dist_X) + "x " + str(new_dist_Y) + "y)")
    elif str(direction.lower()) == "backward":
        old_dist_X = concatXPos()
        old_dist_Y = concatYPos()
        value = value[:-1]
        setposition(old_dist_X - (int(value) * 10), old_dist_Y)
        new_dist_X = concatXPos()
        new_dist_Y = concatYPos()
        print("Moved from " + "(" + str(old_dist_X) + "x " + str(old_dist_Y) + "y) " + "to " + "(" + str(new_dist_X) + "x " + str(new_dist_Y) + "y)")
    elif str(direction.lower()) == "up":
        old_dist_X = concatXPos()
        old_dist_Y = concatYPos()
        value = value[:-1]
        setposition(old_dist_X, old_dist_Y + (int(value) * 10))
        new_dist_X = concatXPos()
        new_dist_Y = concatYPos()
        print("Moved from " + "(" + str(old_dist_X) + "x " + str(old_dist_Y) + "y) " + "to " + "(" + str(new_dist_X) + "x " + str(new_dist_Y) + "y)")
    elif str(direction.lower()) == "down":
        old_dist_X = concatXPos()
        old_dist_Y = concatYPos()
        value = value[:-1]
        setposition(old_dist_X, old_dist_Y - (int(value) * 10))
        new_dist_X = concatXPos()
        new_dist_Y = concatYPos()
        print("Moved from " + "(" + str(old_dist_X) + "x " + str(old_dist_Y) + "y) " + "to " + "(" + str(new_dist_X) + "x " + str(new_dist_Y) + "y)")

def degrees(value, direction):
    if str(direction.lower()) == "left":
        left(int(value))
    elif str(direction.lower()) == "right":
        right(int(value))
        
def loop(value, code):
    stack = []
    repeat = int(value)
    if ":" in code:
        for i in range(code.count(":")):
            if i == 0: # because all the lines besides the first will have whitespace due to indent
                stack.append(code.split(":")[i])
            elif i > 0:
                stack.append(code.split(":")[i][1:]) # use [1:] to remove the whitespace
        for each in stack:
            for i in range(repeat):
                syntax_tree(each)
        
def square(value, alignment): # value = length
    seth(0)
    value = int(value)
    if str(alignment.lower()) == "center":
        penup()
        currentX = concatXPos()
        currentY = concatYPos()
        setposition(-value / 2, value / 2)
        pendown()
        for i in range(4):
            forward(int(value))
            right(90)
        penup()
        setposition(currentX, currentY)
    elif str(alignment.lower()) == "bottom":
        pendown()
        for i in range(4):
            forward(int(value))
            right(90)
    elif str(alignment.lower()) == "top":
        pendown()
        for i in range(4):
            forward(int(value))
            left(90)
    else:
        print("[J++ Interpreter]: You must specify alignment. (center, top, bottom)")

def triangle(value, alignment):
    seth(0)
    value = int(value)
    if str(alignment.lower()) == "center":
        penup()
        currentX = concatXPos()
        currentY = concatYPos()
        setposition(currentX - (value / 2), currentY - (value / 3))
        pendown()
        for i in range(3):
            forward(value)
            left(120)
        penup()
        setposition(currentX, currentY)
    if str(alignment.lower()) == "right":
        for i in range(3):
            forward(value)
            left(120)
    if str(alignment.lower()) == "left":
        currentX = concatXPos()
        currentY = concatYPos()
        penup()
        setposition(currentX - value, currentY)
        pendown()
        for i in range(3):
            forward(value)
            left(120)
        penup()
        setposition(currentX, currentY)
    if str(alignment.lower()) == "bottom":
        currentX = concatXPos()
        currentY = concatYPos()
        penup()
        setposition(currentX - (value / 2), currentY - value)
        pendown()
        for i in range(3):
            forward(value)
            left(120)
        penup()
        setposition(currentX, currentY)
        
def add_Operation(value):
    value = str(value)
    if "{" and "}" in value: # need this so it wont try to cut out brackets that dont exist
        value = value.split("{")[1].split("}")[0]  # This extracts the content inside {}
    operand_1 = value.split("+")[0]
    operand_2 = value.split("+")[1]
    result = int(operand_1) + int(operand_2)
    print("[J++ Interpreter]: " + str(result)) #prints by default for now but store it in a variable when variables are supported
    
def subtract_Operation(value):
    value = str(value)
    if "{" and "}" in value: # need this so it wont try to cut out brackets that dont exist
        value = value.split("{")[1].split("}")[0]  # This extracts the content inside {}
    operand_1 = value.split("-")[0]
    operand_2 = value.split("-")[1]
    result = int(operand_1) - int(operand_2)
    print("[J++ Interpreter]: " + str(result)) #prints by default for now but store it in a variable when variables are supported
    
def division_Operation(value):
    value = str(value)
    if "{" and "}" in value: # need this so it wont try to cut out brackets that dont exist
        value = value.split("{")[1].split("}")[0]  # This extracts the content inside {}
    operand_1 = value.split("/")[0]
    operand_2 = value.split("/")[1]
    result = float(operand_1) / float(operand_2)
    print("[J++ Interpreter]: " + str(result)) #prints by default for now but store it in a variable when variables are supported
    
def multiplication_Operation(value):
    value = str(value)
    if "{" and "}" in value: # need this so it wont try to cut out brackets that dont exist
        value = value.split("{")[1].split("}")[0]  # This extracts the content inside {}
    operand_1 = value.split("*")[0]
    operand_2 = value.split("*")[1]
    result = float(operand_1) * float(operand_2)
    print("[J++ Interpreter]: " + str(result)) #prints by default for now but store it in a variable when variables are supported
        
def syntax_tree(each): # this would be easier if only codehs supported match case statements
    try:
        fetchedToken = each
        if "loop(" in fetchedToken: # allow multi line by taking the code input and parsing it in a loop function into multiple commands to be looped
            value = re.search(r'loop\((.*?)\)', each) # value\( matches loop(, (.*?) matches anything inside the brackets, \) matches closing bracket
            value = value.group(1)
            each = each.split("{")[1]
            code = each.split("}")[0]
            loop(value, code)
        elif "move(" in fetchedToken:
            each = each[:-1]
            first_part = "move("
            each = each[each.index(first_part) + len(first_part):]
            if "," in each:
                argSpliter = each.split(",") # split multi arguements
                arg1 = argSpliter[0] # get first arguement which will be the value
                arg2 = argSpliter[1] # get second arguement which will be the direction
                arg2 = arg2.replace(" ", "") # remove whitespace
                move(arg1, arg2) # arg1 = value/length arg2 = alignment
            elif "," not in each:
                move(each, "forward") # default to forward if no 2nd arguement is defined
        elif "degrees(" in fetchedToken:
            each = each[:-1]
            first_part = "degrees("
            each = each[each.index(first_part) + len(first_part):]
            if "," in each:
                argSpliter = each.split(",") # split multi arguements
                arg1 = argSpliter[0] # get first arguement which will be the value
                arg2 = argSpliter[1] # get second arguement which will be the direction
                arg2 = arg2.replace(" ", "") # remove whitespace
                degrees(arg1, arg2) # arg1 = value/length arg2 = alignment
            elif "," not in each:
                degrees(each, "left") # default to left if no 2nd arguement is defined
        elif "+" in fetchedToken:
            add_Operation(each)
        elif "-" in fetchedToken:
            subtract_Operation(each)
        elif "/" in fetchedToken:
            division_Operation(each)
        elif "*" in fetchedToken:
            multiplication_Operation(each)
        elif "jout" in fetchedToken and "loop(" not in fetchedToken: # if it includes jout...
            # get value first
            value = re.findall(r'"(.*?)"', fetchedToken) # r'"(.*?)"' will look for text inside quotes we are using the re module. Might needa change this so it can accept vars. It assumes all prints will have quotes.
            for i in value:
                jout(value)
        elif "jin" in fetchedToken:
            getVar = "jin << "
            value = each[each.index(getVar) + len(getVar):]
            jin(value)
        elif "square(" in fetchedToken:
            each = each[:-1]
            first_part = "square("
            each = each[each.index(first_part) + len(first_part):]
            if "," in each:
                argSpliter = each.split(",") # split multi arguements
                arg1 = argSpliter[0] # get first arguement which will be the value
                arg2 = argSpliter[1] # get second arguement which will be the direction
                arg2 = arg2.replace(" ", "") # remove whitespace
                square(arg1, arg2) # arg1 = value/length arg2 = alignment
            elif "," not in each:
                square(each, "center") # default to center if no 2nd arguement is defined
        elif "triangle(" in fetchedToken:
            each = each[:-1]
            first_part = "triangle("
            each = each[each.index(first_part) + len(first_part):]
            if "," in each:
                argSpliter = each.split(",") # split multi arguements
                arg1 = argSpliter[0] # get first arguement which will be the value
                arg2 = argSpliter[1] # get second arguement which will be the direction
                arg2 = arg2.replace(" ", "") # remove whitespace
                triangle(arg1, arg2) # arg1 = value/length arg2 = alignment
            elif "," not in each:
                triangle(each, "center") # default to center if no 2nd arguement is defined
    except Exception as err:
        print("[J++ Interpreter]: Caught unexpected error: " + str(err) + "\n")
def evaluator(jpp_parsed): #cut at semicolon for individual commands
    splitCommands = jpp_parsed.split(";")
    lineNumber = 0
    print("\n")
    for each in splitCommands:
        if len(each) > 0: # so it wont print if each has nothing aka no code left
            lineNumber += 1
            print("Evaluating Instruction " + str(lineNumber) + ": " + str(each))
            syntax_tree(each)
evaluator(jpp_parsed)
