import streamlit as st
import plotly.graph_objs as go
from utilz.llama_response import get_ai_recommendations_from_api
from utilz.mock_sleep_data import get_last_week_sleep_data, simulate_improved_sleep_data
from utilz.graphs.sleep_duration_chart import plot_sleep_duration_chart
from utilz.graphs.sleep_phases_chart import plot_sleep_phases_chart
from utilz.graphs.sleep_distribution_chart import plot_sleep_distribution_chart

def app():
    st.title("AI-Powered Sleep Recommendations and Impact")

    st.write("Please answer the following questions to help us understand your sleep habits better. Based on your responses, we'll provide personalized recommendations to improve your sleep.")

    with st.form(key='questionnaire'):
        bedtime_consistency = st.selectbox(
            "How consistent is your bedtime?",
            ("Consistent", "Inconsistent")
        )
        
        caffeine_intake = st.selectbox(
            "How would you describe your daily caffeine intake?",
            ("Low", "Moderate", "High")
        )
        
        screen_time = st.selectbox(
            "How much time do you spend on screens (phone, TV, computer) before bed?",
            ("Low", "Moderate", "High")
        )

        stress_level = st.selectbox(
            "How would you rate your stress level before bed?",
            ("Low", "Moderate", "High")
        )

        physical_activity = st.selectbox(
            "How would you describe your physical activity during the day?",
            ("Low", "Moderate", "High")
        )

        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        responses = {
            'bedtime_consistency': bedtime_consistency,
            'caffeine_intake': caffeine_intake,
            'screen_time': screen_time,
            'stress_level': stress_level,
            'physical_activity': physical_activity,
        }

        with st.spinner("Generating your personalized sleep recommendations..."):
            recommendations = get_ai_recommendations_from_api(responses)

        st.write("### Based on your answers, here are five key recommendations:")
        for i, recommendation in enumerate(recommendations, 1):
            st.write(f"{recommendation}")


        last_week_data = get_last_week_sleep_data()
        improved_data = simulate_improved_sleep_data()

        st.write("---")
        st.subheader("Comparison of Last Week's Sleep Quality vs. Projected Improvement")

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        extended_days = days + [f"Next {day}" for day in days]

        current_values = list(last_week_data.values())
        projected_values = list(improved_data.values())

        combined_fig = go.Figure()

        combined_fig.add_trace(go.Scatter(
            x=days,
            y=current_values,
            mode='lines+markers',
            name='Last Week',
            line=dict(color='blue'),
            marker=dict(size=10)
        ))

        combined_fig.add_trace(go.Scatter(
            x=extended_days,
            y=current_values + projected_values,
            mode='lines+markers',
            name='Projected Next Week',
            line=dict(color='green', dash='dash'),
            marker=dict(size=10)
        ))

        combined_fig.update_layout(
            title="Sleep Quality: Last Week vs. Projected Improvement",
            xaxis_title="Days",
            yaxis_title="Hours of Sleep",
            xaxis=dict(tickmode='array', tickvals=list(range(len(extended_days))), ticktext=extended_days),
            hovermode='x unified'
        )

        st.plotly_chart(combined_fig, use_container_width=True)