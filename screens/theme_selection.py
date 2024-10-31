import streamlit as st
import streamlit_scrollable_textbox as stx
# from utilz.llama_response import getLLamaSleepscapeResponse
# from utilz.text_to_speech import text_to_speech

def app():
    st.title("Select a Coaching Theme")
    # Define the coaching themes

    coaching_themes = [
        "Running in the Savannah and running away from lions",
        "Running on the Brooklyn Bridge",
        "Running on a deserted beach"
    ]

    # Initialize session state for the selected theme
    if 'selected_theme' not in st.session_state:
        st.session_state.selected_theme = None
    if 'max_hr' not in st.session_state:
        st.session_state.max_hr = None
        
    # Create the dropdown for selecting a coaching theme
    selected_theme = st.selectbox("Select a coaching theme", coaching_themes)

    # Create a button to save the selected theme to session variables
    if st.button("Save Theme"):
        st.session_state.selected_theme = selected_theme
        st.success(f"Theme saved: {selected_theme}")

    # col1, col2 = st.columns([3, 5])

    # with col1:
    #     no_words = st.text_input('No of Words')
    # with col2:
    #     sleepscape_type = st.selectbox('Sleepscape type', ('Bedtime story', 'Meditation'), index=0)

    # if st.button("Generate"):
    #     with st.spinner(f'Generating {sleepscape_type}...'):
    #         story = getLLamaSleepscapeResponse(input_text, no_words, sleepscape_type)
    #         stx.scrollableTextbox(f' {story}', height=200)
        
    #     with st.spinner('Generating Audio...'):
    #         filename = f"{sleepscape_type.replace(' ', '_').lower()}.mp3"
    #         text_to_speech(story, filename)
    #         st.audio(filename, format="audio/mpeg", loop=True, autoplay=True)
  