#Layouts

import streamlit as st

#Dividing Columns- Dashboard

st.title("Layouts")
st.subheader("Chai Taste Poll")

col1,col2=st.columns(2)

with col1:
    st.header("Masala Chai")
    vote1=st.button("Vote Masala Chai")
    st.image("https://images.pexels.com/photos/18030044/pexels-photo-18030044.jpeg", width=200)
    #Images have have args:
        # width — set the display width in pixels
        # caption — add a caption below the image
        # use_container_width — set to True to make it fill the container width (replaces the old use_column_width)
        # channels — for numpy arrays (RGB or BGR)
        # output_format — JPEG or PNG

with col2:
    st.header("Kesari Chai")
    vote2=st.button("Vote Kesari Chai")
    st.image("https://images.pexels.com/photos/36326292/pexels-photo-36326292.jpeg",width=200)

if vote1:
    st.success(f"Thansk for voting Masala Chai")
elif vote2:
    st.success(f"Thansk for voting Kesari Chai")


name=st.sidebar.text_input("Enter your name")
tea=st.sidebar.selectbox("Enter your tea",["Masal Chai","Kesari Chai"])
st.write(f"Welcome {name}, your {tea} is getting ready")


#Expander
with st.expander("Show Chai making Instructions"):
    st.write(""" 
    Step-1: Boil water with tea leaves
    Step-2: Add sugar to the boiling water tea
    Step-3: Add lemon if needed
    Step-4: Pour it in the Cup
    Step-5: Chai is ready
    """)

#markdown
st.markdown('## Welcome to chai app')
st.markdown('> cmd for blockquote')


# Headings


# st.markdown('# H1')
# st.markdown('## H2')
# st.markdown('### H3')
# st.markdown('#### H4')
# Text Formatting


# st.markdown('**bold**')
# st.markdown('*italic*')
# st.markdown('***bold and italic***')
# st.markdown('~~strikethrough~~')
# Blockquote


# st.markdown('> This is a blockquote')
# Code


# st.markdown('`inline code`')          # inline
# st.markdown('```python\ncode\n```')   # code block
# Lists


# st.markdown('- item 1\n- item 2\n- item 3')   # unordered
# st.markdown('1. item 1\n2. item 2')            # ordered
# Links


# st.markdown('[Click here](https://google.com)')
# Images


# st.markdown('![alt text](image_url)')
# Horizontal Rule


# st.markdown('---')
# Tables


# st.markdown('''
# | Name | Age |
# |------|-----|
# | Aashwin | 25 |
# ''')
# Emoji


# st.markdown('I love chai :tea:')
# Colored/Styled Text (Streamlit specific)


# st.markdown(':red[This is red text]')
# st.markdown(':blue[This is blue text]')
# st.markdown(':green[This is green text]')
# st.markdown(':orange[This is orange text]')
