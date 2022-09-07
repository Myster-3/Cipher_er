import streamlit as st
from PIL import Image

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.ibb.co/1v8bKBQ/logo.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 0px 0px;
                background-size: 350px 250px;
            }
            [data-testid="stSidebarNav"]::before {
                content: " ";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


st.set_page_config(
    page_title='Cipher_er'
)
add_logo()
st.title('Cipher_er')
'''
### Hey Everyone so this is Cipher_er, 
#### This will allow anyone to use my system to encrypt your messages and get new private and public key for every new messages.
#### Wtih this you can use it on any site or anywhere and decrypt it here only,
This system uses multiple different encryption algorithm, hence we have a hybrid encryption/decryption algorithm. Y
ou can not decrypt these messages anywhere else except here.This 
is There Fore most secured place for Encrypting and Decrypting messages.

### Developed by: Myster_3
'''
image = Image.open('assets\image.png')
newsize = (300, 300)
image = image.resize(newsize)
st.image(image)
