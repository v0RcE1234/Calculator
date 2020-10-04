operation=input('Addition, subtraction, multiplication, division, exponential operator, modulo operator, or floor division?(a, s, m, d, e, mo, f) ')
if operation=='a' or operation=='s' or operation=='m' or operation=='d' or operation=='e' or operation=='mo' or operation=='f':
    x=input('What should the first number be? ')
    y=input('What should the second number be? ')
    math_x=int(x)
    math_y=int(y)
    if operation=='a':
        outcome=str(math_x+math_y)
        print(x+' plus '+y+' equals '+outcome)
    if operation=='s':
        outcome=str(math_x-math_y)
        print(x+' minus '+y+' equals '+outcome)
    if operation=='m':
        outcome=str(math_x*math_y)
        print(x+' times '+y+' equals '+outcome)
    if operation=='d':
            outcome=str(math_x/math_y)
            print(x+' divided '+y+' equals '+outcome)
    if operation=='e':
        outcome=str(math_x**math_y)
        print(x+' to the power of '+y+' equals '+outcome)
    if operation=='mo':
        outcome=str(math_x%math_y)
        print(x+' mod '+y+' is '+outcome)
    if operation=='f':
        outcome=str(math_x//math_y)
        print("The floor of "+x+"/"+y+" is "+outcome)
else:
    print('Thats not a valid input!')
