import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLLamaresponse(input_text,no_words,blog_style):

    ## LLama model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt template
    template=""" 
                Write blog for {blog_style} job profile for topic {input_text}
                within {no_words} words. """
    
    prompt=PromptTemplate(input_variables=["style","text","no_words"],template=template)

    ## Generate the response from llama 2 model
    response=llm(prompt.format(style=blog_style,text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate blog",
                   page_icon='💀',
                   layout='centered',
                   initial_sidebar_status='collapsed')

st.head("Generate Blogs 💀")

input_text=st.text_input("Enter the Blog topic")

col1, col2= st.columns([5,5])

with col1:
    no_words=st.text_input('No of words')

with col2:
    blog_style=st.selectbox('Writing the blog for',('Researcher','Data scientist','Common people'),index=0)

submit=st.button("Generate")

## Final response

if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))