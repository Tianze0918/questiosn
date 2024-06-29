

def sub(source, target):
    source_index=0
    target_index=0
    counter=0
    while target_index!=len(target):
        index=source.find(target[target_index])
        if (index==-1):
            return -1
        while (source_index<len(source)):
            if (target[target_index]==source[source_index]):
                target_index+=1
                if (target_index==len(target)):
                    return counter
        source_index+=1

    return counter
        