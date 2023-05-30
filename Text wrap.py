def wrap(string, max_width):
    x=[string[i:i+max_width] for i in range(0,len(string),max_width)]
    x='\n'.join(x)

    return x

