import streamlit as st
import json


def load_settings():
    try:
        with open('settings.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.warning("Settings file not found. Please complete the onboarding process.")
        return user_onboarding()

# Save settings to JSON file
def save_settings(settings):
    with open('settings.json', 'w') as file:
        json.dump(settings, file)

# User onboarding wizard
def user_onboarding():
    st.info("Welcome! Please complete the onboarding process.")
    
    # Legal waiver
    st.write("Please read and accept the legal waiver:")
    st.write("""
    ## Legal Disclaimer for QuickFit Max

    By downloading, installing, or using QuickFit Max (hereinafter referred to as "the App"), you agree to be bound by the following terms and conditions:

    1. **Acceptance of Terms**: By using the App, you acknowledge that you have read, understood, and agree to be bound by this disclaimer and all applicable terms and conditions. If you do not agree with these terms, please do not use the App.

    2. **Informational Purposes Only**: The App and its content are provided for informational and educational purposes only. The App is not intended to be a substitute for professional medical advice, diagnosis, or treatment.

    3. **Not a Medical Device**: QuickFit Max is a wellness app and is not intended to be, nor should it be construed as, a medical device. It does not diagnose, treat, cure, or prevent any disease, illness, or medical condition.

    4. **Consult Healthcare Professionals**: Always seek the advice of your physician or other qualified healthcare provider with any questions you may have regarding a medical condition, or before starting any new diet, exercise program, or wellness routine. Never disregard professional medical advice or delay in seeking it because of something you have read or accessed through the App.

    5. **Use at Your Own Risk**: Your use of the App is entirely at your own risk. You are solely responsible for any injuries, damages, or losses that may occur as a result of using the App or following any advice, recommendations, or information provided through it.

    6. **Limitation of Liability**: To the fullest extent permitted by applicable law, you agree to hold harmless and release from any liability QuickFit Max, its developers, contributors, affiliates, partners, officers, employees, and agents from any and all claims, demands, or damages (actual or consequential) of any kind and nature, known and unknown, suspected and unsuspected, disclosed and undisclosed, arising out of or in any way connected with your use of the App.

    7. **Accuracy and Reliability**: While we strive to provide accurate and up-to-date information, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability of the App or the information contained within it. Any reliance you place on such information is strictly at your own risk.

    8. **No Guarantee of Results**: We do not guarantee any specific results from the use of the App. Individual results may vary based on personal factors, adherence to recommendations, and other variables.

    9. **Third-Party Content**: The App may contain links to third-party websites or resources. We are not responsible for the content, accuracy, or practices of these external sites and resources.

    10. **Personal Data**: Your use of the App is also governed by our Privacy Policy. Please review this policy to understand how we collect, use, and protect your personal information.

    11. **Intellectual Property**: All content, features, and functionality of the App are owned by QuickFit Max or its licensors and are protected by international copyright, trademark, patent, trade secret, and other intellectual property or proprietary rights laws.

    12. **Changes to Disclaimer**: We reserve the right to modify this disclaimer at any time without prior notice. Your continued use of the App after any such changes constitutes your acceptance of the new terms.

    13. **Severability**: If any provision of this disclaimer is found to be unenforceable or invalid, that provision shall be limited or eliminated to the minimum extent necessary so that this disclaimer shall otherwise remain in full force and effect and enforceable.

    14. **Governing Law**: This disclaimer is governed by and construed in accordance with the laws of [Your Jurisdiction], without regard to its conflict of law provisions. You agree to submit to the personal and exclusive jurisdiction of the courts located within [Your Jurisdiction].

    By using QuickFit Max, you acknowledge that you have read, understood, and agree to be bound by this disclaimer. If you do not agree with these terms, please do not use the App.

    Remember, your health and safety are paramount. Always prioritize professional medical advice and listen to your body when engaging in any fitness or wellness program.    """)
    accept_waiver = st.checkbox("I accept the legal waiver")
    
    # User data input
    age = st.number_input("Enter your age", min_value=0, max_value=120, value=30)
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
    physical_condition = st.selectbox("Select your physical condition", ["Excellent", "Good", "Fair", "Poor"])
    max_hr = st.slider("Set your Max Heart Rate (bpm)", min_value=0, max_value=220, value=180)
    
    # Instructional video
    st.write("Watch the instructional video:")
    st.video("https://www.canva.com/design/DAGSUAn2VZU/K_l9QHj7D-KCQTn7S20sTg/watch?utm_content=DAGSUAn2VZU&utm_campaign=designshare&utm_medium=link&utm_source=editor")  # Replace with your video URL
    
    if st.button("Complete Onboarding"):
        if accept_waiver:
            settings = {
                'age': age,
                'gender': gender,
                'physical_condition': physical_condition,
                'max_hr': max_hr
            }
            save_settings(settings)
            st.success("Welcome to your QuickFit Max journey!")
            return settings
        else:
            st.error("Please accept the legal waiver to continue.")
    return None