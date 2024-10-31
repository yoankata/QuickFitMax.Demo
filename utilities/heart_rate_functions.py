
import streamlit as st
import time
import random

# Mock heart rate data
def generate_heart_rate_data(stages, max_hr):
    heart_rate_data = []
    resting_hr = int(max_hr * 0.5)
    warm_up_target = int(max_hr * 0.6)
    max_intensity_target = int(max_hr * 0.94)
    recovery_target = int(max_hr * 0.7)
    cool_down_target = int(max_hr * 0.5)
    
    # Warm Up
    current_hr = resting_hr
    for _ in range(stages["Warm Up"]):
        current_hr += random.randint(1, 3)  # Gradually increase heart rate
        heart_rate_data.append(("Warm Up", min(current_hr, warm_up_target)))
        time.sleep(1)  # Simulate real-time data generation
    
    # Max Intensity
    current_hr = warm_up_target
    for _ in range(stages["Max Intensity"]):
        current_hr += random.randint(2, 5)  # Quickly increase heart rate
        heart_rate_data.append(("Max Intensity", min(current_hr, max_intensity_target)))
        time.sleep(1)  # Simulate real-time data generation
    
    # Recovery
    current_hr = max_intensity_target
    for _ in range(stages["Recovery"]):
        current_hr -= random.randint(1, 3)  # Gradually decrease heart rate
        heart_rate_data.append(("Recovery", max(current_hr, recovery_target)))
        time.sleep(1)  # Simulate real-time data generation
    
    # Cool Down
    current_hr = recovery_target
    for _ in range(stages["Cool Down"]):
        current_hr -= random.randint(1, 2)  # Gradually decrease heart rate
        heart_rate_data.append(("Cool Down", max(current_hr, cool_down_target)))
        time.sleep(1)  # Simulate real-time data generation
    
    return heart_rate_data

# Define the stages and their durations (in seconds)
stages = {
    "Warm Up": 60,
    "Max Intensity": 120,
    "Recovery": 60,
    "Cool Down": 60
}


# Heartbeat animation function with real-time SVG heart rate and self-contained loop
def heartbeat_animation(svg_path, heart_rate):
    # Open and read the SVG file contents
    with open(svg_path, "r") as svg_file:
        svg_content = svg_file.read()

    # Define CSS styling for the heart container
    container_css = """
    <style>
    .heartbeat-container {
        position: relative;
        width: 300px;
        height: 300px;
        margin: auto;
        text-align: center;
    }
    .heart-rate-text {
        position: absolute;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 45px;
        color: white;
        z-index: 2;
    }
    .bpm-label {
        font-size: 24px;
    }
    </style>
    """
    st.markdown(container_css, unsafe_allow_html=True)

    # Create a container for the SVG to allow periodic updates
    svg_container = st.empty()

    # Check if heart rate is zero; if so, display a static message
    if heart_rate == 0:
        svg_container.markdown(
            f"""
            <div class="heartbeat-container">
                <div class="heart-rate-text">
                    <b>No heart beat detected</b> <span class="bpm-label">Connect wearable</span>
                </div>
                <div style="transform: scale(1); transition: none;">
                    {svg_content}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return  # Exit the function if heart rate is zero

    # Calculate the interval for the heartbeat effect based on heart rate
    beat_interval = 60 / heart_rate  # time per beat in seconds
    max_sleep = 10  # max sleep time in seconds

    # Start the animation loop for non-zero heart rates
    while True:
        for scale_value in [1.2, 1.0]:  # Alternates between heartbeat (scale up) and relaxation
            svg_container.markdown(
                f"""
                <div class="heartbeat-container">
                    <div class="heart-rate-text">
                        <b>{heart_rate}</b> <span class="bpm-label">BPM</span>
                    </div>
                    <div style="transform: scale({scale_value}); transition: transform {beat_interval / 2}s ease;">
                        {svg_content}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            time.sleep(min(beat_interval / 2, max_sleep))  # Half beat interval for each scale

# # Heartbeat animation function with real-time SVG heart rate and self-contained loop
# def heartbeat_animation(svg_path, heart_rate):
#     # Open and read the SVG file contents
#     with open(svg_path, "r") as svg_file:
#         svg_content = svg_file.read()

#     # Create a container for the SVG to allow periodic updates
#     svg_container = st.empty()

#     # Calculate the interval for the heartbeat effect based on heart rate
#     beat_interval = 60 / heart_rate if heart_rate > 0 else 10  # time per beat in seconds
 
#     # Set max sleep time to avoid infinite loop
#     max_sleep = 10  # max sleep time in seconds

#     # Start the animation loop
#     while True:
#         # Scale up to simulate heartbeat
#         svg_container.markdown(
#             f"""
#             <div style="position: relative; width: 300px; height: 300px; text-align: center;">
#                 <div style="position: absolute; top: 45%; left: 50%; transform: translate(-50%, -50%); z-index: 2;">
#                     <span style="font-size: 45px; color: white;"><b>{heart_rate}</b></span>
#                     <span style="font-size: 24px;">BPM</span>
#                 </div>
#                 <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; height: 100%; z-index: 1;">
#                     <div style="width: 100%; height: 100%; transform: scale(1); transition: transform {beat_interval / 2}s ease;">
#                         {svg_content}
#             """,
#             unsafe_allow_html=True,
#         )

#         # Half beat interval or max sleep time
#         time.sleep(min(beat_interval / 2, max_sleep))  
  
#         # Scale down to simulate heartbeat relaxation
#         svg_container.markdown(
#             f"""
#             <div style="position: relative; width: 300px; height: 300px; text-align: center;">
#                 <div style="position: absolute; top: 45%; left: 50%; transform: translate(-50%, -50%); z-index: 2;">
#                     <span style="font-size: 45px; color: white;"><b>{heart_rate}</b></span>
#                     <span style="font-size: 24px;">BPM</span>
#                 </div>
#                 <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; height: 100%; z-index: 1;">
#                     <div style="width: 100%; height: 100%; transform: scale(0.5); transition: transform {beat_interval / 2}s ease;">
#                         {svg_content}
#             """,
#             unsafe_allow_html=True,
#         )
#         time.sleep(beat_interval / 2)  # Half beat interval