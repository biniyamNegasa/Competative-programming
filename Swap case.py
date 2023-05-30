def swap_case(s):
    b=len(s)
    c=""
    for i in range(b):
        if s[i]==s[i].lower():
            c+=s[i].upper()
        elif s[i]==s[i].upper():
            c+=s[i].lower()
    return c
