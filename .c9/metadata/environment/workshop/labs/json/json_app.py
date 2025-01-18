{"filter":false,"title":"json_app.py","tooltip":"/workshop/labs/json/json_app.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["import streamlit as st #all streamlit commands will be available through the \"st\" alias","import json_lib as glib #reference to local lib script",""],"id":1}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":3,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["st.set_page_config(page_title=\"Text to JSON\", layout=\"wide\")  #set the page width wider to accommodate columns","st.title(\"Text to JSON\")  #page title","","col1, col2 = st.columns(2)  #create 2 columns",""],"id":3}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":8,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["with col1: #everything in this with block will be placed in column 1","    st.subheader(\"Content\") #subhead for this column","    ","    input_text = st.text_area(\"Input text\", height=500, label_visibility=\"collapsed\")","","    process_button = st.button(\"Run\", type=\"primary\") #display a primary button",""],"id":5}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":15,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["with col2: #everything in this with block will be placed in column 2","    st.subheader(\"Result\") #subhead for this column","    ","    if process_button: #code in this if block will be run when the button is clicked","        with st.spinner(\"Running...\"): #show a spinner while the code in this with block runs","            response_content = glib.get_json_response(input_content=input_text) #call the model through the supporting library","            ","            st.json(response_content) #render JSON if there was no error",""],"id":7}]]},"ace":{"folds":[],"scrolltop":181.5,"scrollleft":0,"selection":{"start":{"row":23,"column":0},"end":{"row":23,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":103,"mode":"ace/mode/python"}},"timestamp":1737193771064,"hash":"f4a8589c8b56de898394dfe87aec78abd53a1ade"}