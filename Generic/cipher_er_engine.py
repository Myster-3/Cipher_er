

def encrypt_decrypt(text,key):
    
    out_text=''
    key=key.split('!')
    flag=key[-1]
    t_flag=int(flag.split('_')[-1])

    if t_flag<0:
        flag=2
    else: 
        flag=1
    
    text=text[::-1]
    text=text.split('\n')

    for t in range(len(text)): 
        t_a=key[t%5]
        a=t_a.split('_')[0]
        N=t_a.split('_')[1]
        
        t_a=text[t]
        for character in t_a:
            N=int(N)
            a=int(a)
            if flag==2:
                character=chr(ord(character)-int(N/10))


            if (ord(character) in range(32,47,1)) or(ord(character) in range(58,64,1)) or (ord(character) in range(91,96,1)) or(ord(character) in range(123,126,1)) and flag==1:
                pass
            else: 
                if character.isupper()==character: 
                    character=ord(character)-96
                    f=1
                else: 
                    character=ord(character)-64
                    f=0

                character=((character**a)%N)
                if f==1:
                    character=chr(character+96)
                elif f==0: 
                    character=chr(character+64)        
            
            if flag==1:
                character=chr(ord(character)+int(N/10))
            
            out_text+=character
        out_text+='\n'
    out_text=out_text[::-1]
    out_text=out_text[1:]
    return out_text
    

