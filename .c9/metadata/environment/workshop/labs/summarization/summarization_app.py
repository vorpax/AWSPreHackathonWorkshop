{"filter":false,"title":"summarization_app.py","tooltip":"/workshop/labs/summarization/summarization_app.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["import streamlit as st","import summarization_lib as glib",""],"id":1}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":3,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["st.set_page_config(page_title=\"Document Summarization\")","st.title(\"Document Summarization\")",""],"id":3}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":6,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["input_text = st.text_area(\"How would you like the document summarized?\")","","summarize_button = st.button(\"Summarize\", type=\"primary\")","","if summarize_button:","    st.subheader(\"Summary\")","","    with st.spinner(\"Running...\"):","        response_content = glib.get_summary(input_text)","        st.write(response_content)",""],"id":5}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":0},"end":{"row":16,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1737189563344,"hash":"f173d47afd4e257cd74dbf88c4e3bdc386c71b27"}