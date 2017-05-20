trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(number):
    '''
    Takes an integer 0-99
    Returns the mandarin pronounciation of the number
    '''
    numeric = str(number)
    count = 0
    translation = ""
    for e in numeric:
        if trans[e] == 'ling' and len(numeric) > 1:
            count += 1
        elif trans[e] == "yi" and len(numeric) == 2:
            count += 1
            if numeric =="11":
                return "shi yi"
            else:
                translation += "shi"          
        else:
            count += 1
            if count - 1 != len(numeric) and count != 1:
                translation += " "
            
            translation += trans[e]              
            if count != len(numeric):
                translation += " shi"  
    return translation

convert_to_mandarin()
