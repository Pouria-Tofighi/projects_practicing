import streamlit as st

from password_generator import RandomPasswordGenerator, MemorablePasswordGenerator, PinGenerator


st.title(":zap: PASSWORD GENERATOR")

option = st.radio('Password Type:',
                   ('Random Password', 'Memorable Password', 'PIN Code'))

if option == 'Random Password':
    length = st.slider("The length of the password", min_value = 5, max_value = 20)
    Include_numbers = st.toggle("Include Numbers")
    Include_symbles = st.toggle("Include Symbols")

    generator = RandomPasswordGenerator(
        length, Include_numbers, Include_symbles
    )

elif option == 'Memorable Password':
    No_of_words = st.slider("The length of the password", min_value = 5, max_value = 20)
    Capitalization = st.toggle('Capitilze words')
    seperator = st.text_input('Seperator', value='-')

    generator = MemorablePasswordGenerator(
        length = No_of_words, capitalization=  Capitalization, seperator=  seperator, 
    )

else:
    length = st.slider("The length of the password", min_value = 5, max_value = 20)

    generator = PinGenerator(length)

password = generator.generate()

st.write("Your password is: ")
st.header(fr'``` {password} ```')