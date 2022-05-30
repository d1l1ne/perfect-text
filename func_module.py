

def del_punctuation_spaces(input_text):
    '''
    
    This function takes text string and removes useless spaces before
    punctuation marks
    input_text: any string
    function returns text without useless spaces before
    punctuation marks

    '''
    temp = len(input_text)-1
    for pos in range(0, temp):
        
        if (pos < temp) and (input_text[pos] == ' ') and (input_text[pos+1] in ".,!?:;¿¡"):
                input_text = input_text[:pos] + input_text[pos+1:]
                temp-=1
                
    return input_text
    

def del_brackets_spaces(input_text):
    '''
    
    This function takes text string and removes useless spaces before and after
    brackets and quotation marks.
    input_text: any string
    function returns text without useless spaces before and after
    brackets
    
    '''
    temp = len(input_text)-1
    
    for pos in range(0, temp):
        
        if (pos<temp) and (input_text[pos] == ' ') and (input_text[pos-1] in "([{<«\'\""):
            input_text = input_text[:pos] + input_text[pos+1:]
            temp-=1
  
        if (pos<temp) and (input_text[pos] == ' ') and (input_text[pos+1] in ")]}>»\'\""):
            input_text = input_text[:pos] + input_text[pos+1:]
            temp-=1

            
    for pos in range(0, temp):
        
        if (pos<temp) and (input_text[pos+1] in "([{<«\'\"") and (input_text[pos] != " "):
            input_text = input_text[:pos+1] + ' ' + input_text[pos+1:]
            temp+=1
            
        if (pos<temp) and (input_text[pos-1] in ")]}>»\'\"") and (input_text[pos] != " ") and (input_text[pos] not in ".,!?:;¿¡)"):
            input_text = input_text[:pos] + ' ' + input_text[pos:]
            temp+=1
            
            
    return input_text


def fix_separation_of_sentences(input_text):
    '''
    
    This function takes text string. It fixes lack of spaces and small letters after sentence ending.
    input_text: any string
    function returns fixed text without abovementioned mistakes. DO NOT USE THIS FUNCTION IF YOUR
    TEXT CONTAINS EMAILS OR WEBSITE ADDRESSES. Also it will be better if you use this function
    after deleting all multi spaces.
    
    '''
    temp = len(input_text)-1
    
    for pos in range(0, temp):
        
        if (pos<temp) and (input_text[pos+1] != ' ') and (input_text[pos] in ".!?:;¿¡") and (input_text[pos+1] not in ".!?:;¿¡,"):
            input_text = input_text[:pos+1] + ' ' + input_text[pos+1:]
            temp+=1
    
    for pos in range(0, temp):
        
        if (pos<temp) and (input_text[pos-1] == ' ') and (input_text[pos-2] in ".!?¿¡"):
            input_text = input_text[:pos] + input_text[pos].upper() + input_text[pos+1:]
    
    return(input_text)


def del_multi_spaces(input_text):
    '''
    
    This function takes text string and fixes multi spaces
    input_text: any string
    function returns text without multi spaces
    
    '''
    temp = len(input_text)-1 
    spaces = 0
    for pos in range(0, temp):
        if input_text[pos] == ' ' and input_text[pos+1] == ' ':
            spaces+=1
    for count in range(0, spaces):
        for pos in range(0, temp):
            if(pos<temp) and (input_text[pos] == ' ') and (input_text[pos+1] == ' '):
                input_text = input_text[:pos] + input_text[pos+1:]
                temp-=1
            
    return input_text


def fix_dashes(input_text):
    '''
    
    This function takes text string and fixes dashes issues
    input_text: any string
    function returns text without dashes issues

    '''
    temp = len(input_text)-1
    for pos in range(0, temp):
        
        if (pos < temp) and (input_text[pos] in '-—') and (input_text[pos-1] != ' ') and (input_text[pos+1] == ' '):
                input_text = input_text[:pos] + ' ' + input_text[pos:]
                temp+=1
                
        if (pos < temp) and (input_text[pos] in '-—') and (input_text[pos+1] != ' ') and (input_text[pos-1] == ' '):
                input_text = input_text[:pos+1] + ' ' + input_text[pos+1:]
                temp+=1
                
    return input_text
    