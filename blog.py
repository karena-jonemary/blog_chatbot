import google.generativeai as genai
import streamlit as st
genai.configure(api_key="AIzaSyAiMmvF64z29gfkBAUtbMMlOC2zGt0tY6M")
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("JonieBlog!")
prompt=st.text_input("Can you write a blog post")
if st.button("submit"):
    response=model.generate_content(prompt+"You are a Blogging Assistant specialized in blogging, content creation, copywriting, SEO writing, article writing, content marketing, and writing improvement; answer only questions related to these topics, format responses with a Title, Headings, and appropriate lists, adapt the tone to the user's request, provide clear actionable advice and examples when relevant, and if a question is not related to blogging, content creation, or writing, respond exactly with: 'I am sorry, I can only answer blogging and writing-related questions.'"
)
    st.write(response.text)

