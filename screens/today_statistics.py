import streamlit as st
# from utilz.graphs.sleep_duration_chart import plot_sleep_duration_chart
# from utilz.graphs.sleep_phases_chart import plot_sleep_phases_chart
# from utilz.graphs.sleep_distribution_chart import plot_sleep_distribution_chart

# def app():
#     st.title("Today's Sleep Statistics")

#     st.subheader("Total Sleep Duration")
#     fig_duration = plot_sleep_duration_chart()
#     st.plotly_chart(fig_duration, use_container_width=True)

#     st.write("---")

#     st.subheader("Sleep Phases Distribution")
#     fig_phases = plot_sleep_phases_chart()
#     st.plotly_chart(fig_phases, use_container_width=True)

#     st.write("---")

#     st.subheader("Sleep Distribution Throughout the Night")
#     fig_distribution = plot_sleep_distribution_chart()
#     st.plotly_chart(fig_distribution, use_container_width=True)