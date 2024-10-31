import streamlit as st
# from utilz.graphs.sleep_duration_chart import plot_sleep_duration_chart
# from utilz.graphs.sleep_efficiency_gauge import plot_sleep_efficiency_gauge
# from utilz.graphs.sleep_consistency_chart import plot_sleep_consistency_chart
# from utilz.graphs.sleep_latency_chart import plot_sleep_latency_chart

# def app():
#     st.title("Sleep Statistics and Projections")

#     # Sleep Duration Chart
#     st.subheader("Current vs Projected Sleep Quality Over Two Weeks")
#     fig_duration = plot_sleep_duration_chart()
#     st.plotly_chart(fig_duration, use_container_width=True)

#     st.write("---")

#     # Sleep Efficiency Gauge
#     st.subheader("Sleep Efficiency")
#     fig_efficiency = plot_sleep_efficiency_gauge()
#     st.plotly_chart(fig_efficiency, use_container_width=True)

#     st.write("---")

#     # Sleep Consistency Chart
#     st.subheader("Sleep Duration Consistency")
#     fig_consistency = plot_sleep_consistency_chart()
#     st.plotly_chart(fig_consistency, use_container_width=True)

#     st.write("---")

#     # Sleep Latency Chart
#     st.subheader("Sleep Latency")
#     fig_latency = plot_sleep_latency_chart()
#     st.plotly_chart(fig_latency, use_container_width=True)