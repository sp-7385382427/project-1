import streamlit as st

# Caesar Cipher Functions
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            ascii_offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            ascii_offset = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - ascii_offset - shift_amount) % 26 + ascii_offset)
        else:
            decrypted_text += char
    return decrypted_text


# Streamlit UI
st.title("Caesar Cipher Encrypt/Decrypt App")

# Input text field
text_input = st.text_area("Enter the text to encrypt/decrypt", height=150)

# Input shift value
shift_value = st.number_input("Enter the shift value (1-25)", min_value=1, max_value=25, value=3)

# Option to choose between Encrypt or Decrypt
option = st.radio("Choose an option", ("Encrypt", "Decrypt"))

# Process text based on the selected option
if st.button("Process"):
    if option == "Encrypt":
        result = caesar_encrypt(text_input, shift_value)
        st.subheader("Encrypted Text:")
        st.write(result)
    else:
        result = caesar_decrypt(text_input, shift_value)
        st.subheader("Decrypted Text:")
        st.write(result)