import pandas as pd
import streamlit as st

from src.charts import plot_response_hist, plot_borough_bar, plot_complaint_bar

def header_metrics(df: pd.DataFrame) -> None:
    """Rendering header metrics. Placeholder values are intentional."""
    c1, c2, c3 = st.columns(3)

    # TODO (IN-CLASS): Replace these placeholders with real metrics from df
    # Suggestions:
    # - Total complaints (len(df))
    # - Median response time
    # - % from Web vs Phone vs App (pick one)
    with c1:
        st.metric("Total complaints", len(df))
    with c2:
        st.metric("Median response time (days)", df['response_time_days'].median())
    with c3:
        st.metric("Most common complaint", df['complaint_type'].mode().to_string())


def body_layout_tabs(df: pd.DataFrame) -> None:
    """Tabs layout with 3 default tabs."""
    t1, t2, t3 = st.tabs(["Distribution", "By Borough", "By Complaint Type"])

    with t1:
        st.subheader("Response Time Distribution")
        plot_response_hist(df)

        # TODO (IN-CLASS): Add a short interpretation sentence under the chart

        st.write("The distribution of response time in days is heavily right-skewed; however, the average response time for each complaint is 6.17 days, and the median response time is 5 days.")

    with t2:
        st.subheader("Median Response Time by Borough")
        plot_borough_bar(df)

    with t3:
        # TODO (IN-CLASS): Add a second view here (e.g., count by borough)
        # moved to under t3 -- makes more sense to organize with complaint type counts
        st.subheader("Median Response Time by Complaint Type")
        plot_complaint_bar(df)

        st.subheader("Median Response Time by Complaint Type: Data")
        st.dataframe(df, use_container_width=True, height=480)



        # TODO (OPTIONAL): Add st.download_button to export filtered rows

        st.download_button(
            label="Download CSV",
            data=df.to_csv().encode("utf-8"),
            file_name="NYC_complaints.csv",
            mime="text/csv",
            icon=":material/download:",
        )