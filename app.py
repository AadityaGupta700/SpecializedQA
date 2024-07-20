import streamlit as st
from query import get_text_from_files, get_text_chunks, get_vector_embeddings,user_input
def main():
    st.set_page_config("Chat using documents")
    st.header("Q/A with documents")

    st.title('Upload Files ')
    
    # Upload multiple files
    uploaded_files = st.file_uploader('Choose PDF files', accept_multiple_files=True)

    if uploaded_files:

        # Send data
        with st.spinner("Processing..."):
            raw_text = get_text_from_files(uploaded_files)
            text_chunks = get_text_chunks(raw_text)
            get_vector_embeddings(text_chunks)
            st.success("Processed files")
        
        user_query = st.text_input('Enter your query:')
        if user_query:
          user_input(user_query)
    else:
        st.write('Upload your PDF files to proceed')

if __name__ == '__main__':
    main()
