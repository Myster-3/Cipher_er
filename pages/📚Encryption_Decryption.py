import streamlit as st
import Generic.cipher_er_engine as c_engine
st.title('Encryption/Decryption: ')
def cipher_er_main(text,k):
    k=int(k)
    output_text=''
    for i in text: 
        i=chr(ord(i)+k)
        output_text+=i
    return output_text
    

'''
### Encrypt or Decrypt your text

Enter your input text put your key(Private or public ) and as output get 
normal text or cipher text depending upon your input
'''
input_text=st.text_area('Enter input Text: ')
key=st.text_input('Enter Key: ')
if st.button('Convert'):
    text=c_engine.encrypt_decrypt(input_text,key)
else: 
    text='{}'

st.write('## Output Text:')
out=st.text_area('',value=text)
