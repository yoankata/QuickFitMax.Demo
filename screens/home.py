import time
import numpy as np
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utilities.ai_coaching_functions import get_ai_coaching
from utilities.heart_rate_functions import get_heart_rate, heartbeat_animation
from utilities.onboarding_functions import load_settings

# Main app
def app():
   # Load settings
    settings = load_settings()
    
    # Initialize session state
    if 'stage' not in st.session_state:
        st.session_state.stage = "Not Started"
        st.session_state.time_elapsed = 0
        st.session_state.heart_rates = []
        st.session_state.heart_rate = 60
        st.session_state.max_hr = settings.get('max_hr', 180)        
        st.session_state.last_coaching_time = 0
    
    # Start/Stop button
    if st.session_state.stage == "Not Started":
        if st.button("Start Workout"):
            st.session_state.stage = "Warm Up"
            st.session_state.time_elapsed = 0
            st.session_state.heart_rates = []
            st.session_state.last_coaching_time = 0
            st.session_state.heart_rate = 0
    else:
        if st.button("Stop Workout"):
            st.session_state.stage = "Not Started"

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Workout Progress")
        progress_bar = st.progress(0)
        stage_text = st.empty()
        time_text = st.empty()
        
        heart_rate_text = st.empty()
        heart_animation = st.empty()
        coaching_text = st.empty()

    with col2:
        st.subheader("Workout Metrics")
        metrics_chart = st.empty()

    # Workout loop
    if st.session_state.stage != "Not Started":
        stages = ["Warm Up", "Max Intensity", "Recovery", "Max Intensity", "Cool Down"]
        durations = [90, 20, 90, 20, 80]  # in seconds
        total_duration = sum(durations)
        target_pulse_per_stage = [0.6, 0.94, 0.6, 0.94, 0.4]  # in seconds

        while st.session_state.time_elapsed < total_duration:
            current_stage_index = 0
            for duration in durations:
                if st.session_state.time_elapsed < sum(durations[:current_stage_index + 1]):
                    break
                current_stage_index += 1

                st.session_state.stage = stages[current_stage_index]
                stage_text.text(f"Current Stage: {st.session_state.stage}")
                time_text.text(f"Time Elapsed: {st.session_state.time_elapsed} seconds")
                progress_bar.progress(st.session_state.time_elapsed / total_duration)

                # Get and display heart rate
                heart_rate = get_heart_rate(st.session_state.stage, st.session_state.max_hr)
                st.session_state.heart_rates.append(heart_rate)
                heart_rate_text.text(f"Current Heart Rate: {heart_rate} bpm")

                # Update the heartbeat animation
                heart_animation=heartbeat_animation("docs/images/pink-heart.svg", st.session_state.heart_rate)

                # Display AI coaching
                coaching_interval = 5 if st.session_state.stage == "Max Intensity" else 15
                if st.session_state.time_elapsed - st.session_state.last_coaching_time >= coaching_interval:
                    coaching_message = get_ai_coaching(st.session_state.stage, heart_rate, st.session_state.max_hr)
                coaching_text.text(f"AI Coach: {coaching_message}")
                st.session_state.last_coaching_time = st.session_state.time_elapsed

            # Update metrics chart
            df = pd.DataFrame({
                'Time': range(len(st.session_state.heart_rates)),
                'Heart Rate': st.session_state.heart_rates
            })
            fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                                subplot_titles=("Heart Rate During Workout", "Recovery Time"))
            fig.add_trace(go.Scatter(x=df['Time'], y=df['Heart Rate'], mode='lines', name='Heart Rate'),
                          row=1, col=1)
            fig.add_trace(go.Scatter(x=[60, 260], y=[st.session_state.max_hr * 0.94, st.session_state.max_hr * 0.94],
                                     mode='lines', name='94% Max HR', line=dict(dash='dash')),
                          row=1, col=1)
            fig.update_layout(height=500, showlegend=False)
            metrics_chart.plotly_chart(fig, use_container_width=True)

            st.session_state.time_elapsed += 1
            time.sleep(1)

        st.success("Workout Complete!")