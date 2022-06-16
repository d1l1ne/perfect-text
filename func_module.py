double_domains = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bo', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'er', 'es', 'ef', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kd', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'рф', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'xk', 'ye', 'yt', 'yu', 'za', 'zm', 'zw']
triple_domains = ['app', 'biz', 'cat', 'com', 'edu', 'eus', 'fun', 'gov', 'int', 'mil', 'net', 'one', 'ong', 'onl', 'ooo', 'org', 'pro', 'red', 'ren', 'tel', 'xxx', 'xyz', 'art', 'moe', 'dev', 'бел', 'мон', 'срб']
quad_domains = ['aero', 'asia', 'army', 'coop', 'info', 'jobs', 'mobi', 'name', 'pics', 'pink', 'plus', 'porn', 'post', 'prof', 'qpon', 'rent', 'rest', 'rich', 'site', 'yoga', 'zone']

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

def fix_separation_wsites(input_text):
        '''
    
    This function takes text string. It fixes lack of spaces and small letters after sentence ending.
    input_text: any string
    function returns fixed text without abovementioned mistakes..
    
    '''
    
    double_domains = ['ac ', 'ad ', 'ae ', 'af ', 'ag ', 'ai ', 'al ', 'am ', 'an ', 'ao ', 'aq ', 'ar ', 'as ', 'at ', 'au ', 'aw ', 'ax ', 'az ', 'ba ', 'bb ', 'bd ', 'be ', 'bf ', 'bg ', 'bh ', 'bo ', 'br ', 'bs ', 'bt ', 'bv ', 'bw ', 'by ', 'bz ', 'ca ', 'cc ', 'cd ', 'cf ', 'cg ', 'ch ', 'ci ', 'ck ', 'cl ', 'cm ', 'cn ', 'co ', 'cr ', 'cu ', 'cv ', 'cx ', 'cy ', 'cz ', 'de ', 'dj ', 'dk ', 'dm ', 'do ', 'dz ', 'ec ', 'ee ', 'eg ', 'er ', 'es ', 'ef ', 'eu ', 'fi ', 'fj ', 'fk ', 'fm ', 'fo ', 'fr ', 'ga ', 'gb ', 'gd ', 'ge ', 'gf ', 'gg ', 'gh ', 'gi ', 'gl ', 'gm ', 'gn ', 'gp ', 'gq ', 'gr ', 'gs ', 'gt ', 'gu ', 'gw ', 'gy ', 'hk ', 'hm ', 'hn ', 'hr ', 'ht ', 'hu ', 'id ', 'ie ', 'il ', 'im ', 'in ', 'io ', 'iq ', 'ir ', 'is ', 'it ', 'je ', 'jm ', 'jo ', 'jp ', 'ke ', 'kg ', 'kh ', 'ki ', 'km ', 'kn ', 'kp ', 'kr ', 'kd ', 'kw ', 'ky ', 'kz ', 'la ', 'lb ', 'lc ', 'li ', 'lk ', 'lr ', 'ls ', 'lt ', 'lu ', 'lv ', 'ly ', 'ma ', 'mc ', 'md ', 'me ', 'mg ', 'mh ', 'mk ', 'ml ', 'mm ', 'mn ', 'mo ', 'mp ', 'mq ', 'mr ', 'ms ', 'mt ', 'mu ', 'mv ', 'mx ', 'my ', 'mz ', 'na ', 'nc ', 'ne ', 'nf ', 'ng ', 'ni ', 'no ', 'np ', 'nr ', 'nu ', 'nz ', 'om ', 'pa ', 'pe ', 'pf ', 'pg ', 'ph ', 'pk ', 'pl ', 'pm ', 'pn ', 'pr ', 'ps ', 'pt ', 'pw ', 'py ', 'qa ', 're ', 'ro ', 'rs ', 'ru ', 'рф ', 'rw ', 'sa ', 'sb ', 'sc ', 'sd ', 'se ', 'sg ', 'sh ', 'si ', 'sj ', 'sk ', 'sl ', 'sm ', 'sn ', 'so ', 'sr ', 'st ', 'su ', 'sv ', 'sy ', 'sz ', 'tc ', 'td ', 'tf ', 'tg ', 'th ', 'tj ', 'tk ', 'tl ', 'tm ', 'tn ', 'to ', 'tp ', 'tr ', 'tt ', 'tv ', 'tw ', 'tz ', 'ua ', 'ug ', 'uk ', 'us ', 'uy ', 'uz ', 'va ', 'vc ', 've ', 'vg ', 'vi ', 'vn ', 'vu ', 'wf ', 'ws ', 'xk ', 'ye ', 'yt ', 'yu ', 'za ', 'zm ', 'zw ']
    triple_domains = ['app ', 'biz ', 'cat ', 'com ', 'edu ', 'eus ', 'fun ', 'gov ', 'int ', 'mil ', 'net ', 'one ', 'ong ', 'onl ', 'ooo ', 'org ', 'pro ', 'red ', 'ren ', 'tel ', 'xxx ', 'xyz ', 'art ', 'moe ', 'dev ', 'бел ', 'мон ', 'срб ']
    quad_domains = ['aero ', 'asia ', 'army ', 'coop ', 'info ', 'jobs ', 'mobi ', 'name ', 'pics ', 'pink ', 'plus ', 'porn ', 'post ', 'prof ', 'qpon ', 'rent ', 'rest ', 'rich ', 'site ', 'yoga ', 'zone ']
    input_text=input_text+''
    temp = len(input_text)-1
    
    for pos in range(0, temp):
        
        if (pos<temp) and (input_text[pos+1] != ' ') and (input_text[pos] in ".!?:;¿¡") and (input_text[pos+1] not in ".!?:;¿¡,"):
            if (input_text[pos+1:pos+4] not in double_domains) and (input_text[pos+1:pos+5] not in triple_domains) and (input_text[pos+1:pos+6] not in quad_domains):
                input_text = input_text[:pos+1] + ' ' + input_text[pos+1:]
                temp+=1
    
    for pos in range(0, temp):
        
        if (pos<temp) and (input_text[pos-1] == ' ') and (input_text[pos-2] in ".!?¿¡"):
            if (input_text[pos+1:pos+4] not in double_domains) and (input_text[pos+1:pos+5] not in triple_domains) and (input_text[pos+1:pos+6] not in quad_domains):
                input_text = input_text[:pos] + input_text[pos].upper() + input_text[pos+1:]
    
    return(input_text) 
