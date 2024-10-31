import streamlit as st

def app():
    st.title("Device Integration")

    st.write("""
    Integrate your sleep data with the following devices for enhanced tracking and personalized recommendations. 
    Below are some of the popular devices we support:
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/apple_watch.png", use_column_width=True, caption="Apple Watch")
        if st.button("Connect Apple Watch"):
            st.success("Apple Watch connected successfully!")


    with col2:
        st.image("images/garmin_watch.png", use_column_width=True, caption="Garmin Watch")
        if st.button("Connect Garmin Watch"):
            st.success("Garmin Watch connected successfully!")

    with col3:
        st.image("images/muse_band.png", use_column_width=True, caption="Muse")
        if st.button("Connect Muse"):
            st.success("Muse connected successfully!")
