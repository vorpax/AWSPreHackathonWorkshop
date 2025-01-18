{"filter":false,"title":"embeddings_search_app.py","tooltip":"/workshop/labs/embeddings_search/embeddings_search_app.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["import streamlit as st #all streamlit commands will be available through the \"st\" alias","import embeddings_search_lib as glib #reference to local lib script",""],"id":1}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":3,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["st.set_page_config(page_title=\"Embeddings Search\", layout=\"wide\") #HTML title","st.title(\"Embeddings Search\") #page title",""],"id":3}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":6,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["input_text = st.text_input(\"Question about Amazon Bedrock:\")","go_button = st.button(\"Go\", type=\"primary\") #display a primary button",""],"id":5}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":9,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["if go_button: #code in this if block will be run when the button is clicked","    ","    with st.spinner(\"Working...\"): #show a spinner while the code in this with block runs","        response_content = glib.get_similarity_search_results(question=input_text)","        ","        st.table(response_content) #using table so text will wrap","        ",""],"id":7}]]},"ace":{"folds":[],"scrolltop":8,"scrollleft":0,"selection":{"start":{"row":12,"column":82},"end":{"row":12,"column":82},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":27,"mode":"ace/mode/python"}},"timestamp":1737190348296,"hash":"5c8ed9d80b1c57218d3043a1d5adca35622be871"}