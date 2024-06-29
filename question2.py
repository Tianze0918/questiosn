


def paren(input):
    stackl=[]
    stackr=[]
    index=0
    output=['']*len(input)
    while index<len(input):
        if (input[index]=="("):
            stackl.append(index)
        if (input[index]==")"):
            if (not stackl):
                stackr.append(index)
            else:
                stackl.pop()

    while (stackl):
        top_element=stackl.pop()
        output[top_element]="x"
    
    while (stackr):
        top_element=stackr.pop()
        output[top_element]="?"

    return ''.join(output) 