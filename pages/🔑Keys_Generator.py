import streamlit as st
import Generic.generate_keys as g_k
st.title('Generate Keys: ')
def generate_keys(public_keys,private_keys):
    st.write('#### Public_key: \t'+public_keys)
    st.write('#### Private_Key:\t'+private_keys)

'''
### Generate a public key and private key for encryption and decryption process
You will Generate public key and private key for Encryption and decryption period where 
    Public key: This key is used to encrypt the message and you can share it with everyone
    Private Key: This key is used to decrypt all the messages encrypted with public key must keep secret

'''

if st.button('Generate Keys'):
    pub,pri=g_k.get_keys()
    generate_keys(pub,pri)