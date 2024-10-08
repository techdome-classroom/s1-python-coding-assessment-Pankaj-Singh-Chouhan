
def decode_message(s: str, p: str) -> bool:
    
    

    i = 0  
    j = 0  

    while i < len(s) and j < len(p):
        if p[j] == '*':  
            while i < len(s) and s[i] != p[j + 1]:
                i += 1
            if i == len(s):
                return False  
            j += 1
        elif p[j] == '?':  
            i += 1
            j += 1
        elif s[i] != p[j]:
            return False  
        else:
            i += 1
            j += 1


    return i == len(s) and j == len(p)
  
