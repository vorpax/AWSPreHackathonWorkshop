{"filter":false,"title":"showcase_app.py","tooltip":"/workshop/labs/showcase/showcase_app.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["import streamlit as st","import showcase_lib as glib","import showcase_examples as examples",""],"id":1}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["st.set_page_config(page_title=\"Demo Showcase\", layout=\"wide\")","","st.title(\"Demo Showcase\")","","col1, col2, col3 = st.columns(3)",""],"id":3}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":12,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["with col1:","    st.subheader(\"Prompt template\")","    ","    prompts_keys = list(examples.prompts)","","    prompt_selection = st.selectbox(\"Select a prompt template:\", prompts_keys)","    ","    with st.expander(\"View prompt\"):","","        selected_prompt_template_text = examples.prompts[prompt_selection]","","        prompt_text = st.text_area(\"Prompt template text:\", value=selected_prompt_template_text, height=350)",""],"id":5}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":26,"column":0},"end":{"row":37,"column":0},"action":"insert","lines":["with col2:","    st.subheader(\"User input\")","    inputs_keys = list(examples.inputs)","    ","    input_selection = st.selectbox(\"Select an input example:\", inputs_keys)","    ","    selected_input_template_text = examples.inputs[input_selection]","","    input_text = st.text_area(\"Input text:\", value=selected_input_template_text, height=350)","    ","    process_button = st.button(\"Run\", type=\"primary\")",""],"id":7}],[{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":39,"column":0},"end":{"row":47,"column":0},"action":"insert","lines":["with col3:","    st.subheader(\"Result\")","    ","    if process_button:","        with st.spinner(\"Running...\"):","            response_content = glib.get_text_response(user_input=input_text, template=prompt_text)","","            st.write(response_content)",""],"id":9}]]},"ace":{"folds":[],"scrolltop":347,"scrollleft":0,"selection":{"start":{"row":44,"column":98},"end":{"row":44,"column":98},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1737207782730,"hash":"bda367fb8346d608e60c8ee7ea9964e77714709a"}