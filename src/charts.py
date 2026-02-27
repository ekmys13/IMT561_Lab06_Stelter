import pandas as pd
import plotly.express as px
import streamlit as st # importing streamlit to get graphs to streamlit

'''This notebook stores all the functions for plotting the graphs you want on the dashboard'''

# histogram: Distribution of Response Time (Days)
def plot_response_hist(df: pd.DataFrame) -> None:
    """Plotting a simple histogram of response times."""
    # check to ensure there's data in the dataframe first -- if the dataframe is empty, raise an error message
    if df.empty:
        st.info("No rows match your filters.")
        return

    # I guess we don't need an else statement?
    fig = px.histogram(df, x='response_time_days', nbins=30, title="Distribution of Response Time (Days)",)
    st.plotly_chart(fig, use_container_width=True) # use container width - graph will be dynamically sized in the layout
    # note that if you're using not plotly (e.g. bokeh library), you have to call st.bokeh_chart instead

# bar chart: Response Time by Borough
def plot_borough_bar(df: pd.DataFrame) -> None:
    """Plotting median response time by borough."""
    if df.empty:
        st.info("No rows match your filters.")
        return

    agg = (df.groupby("borough", as_index=False)["response_time_days"]
        .median()
        .rename(columns={"response_time_days": "median_response_days"})
        .sort_values("median_response_days", ascending=False)
    )

    fig = px.bar(
        agg,
        x="borough",
        y="median_response_days",
        title="Response Time by Borough",
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_borough_bar1 (df: pd.DataFrame) -> None:
    """Plotting number of complaints by borough."""
    if df.empty:
        st.info("No rows match your filters.")
        return

    borough_counts = df.groupby("borough").size().sort_values(ascending=False).to_frame()
    borough_counts = borough_counts.rename(columns={0: "Number of Complaints"})
    borough_counts

    fig = px.bar(borough_counts, y="Number of Complaints", title="Number of Complaints by Borough")

    fig

# bar chart: Response Time by Complaint Type
def plot_complaint_bar(df:pd.DataFrame) -> None:
    """Plotting median response time by complaint type."""
    if df.empty:
        st.info("No rows match your filters.")
        return

    agg = (df.groupby("complaint_type", as_index=False)["response_time_days"]
           .median()
           .rename(columns={"response_time_days": "median_response_days"})
           .sort_values("median_response_days", ascending=False) # ascending_false sets it so we're sorting the values from largest to smallest
           )

    fig = px.bar(agg, x="complaint_type",
                 y="median_response_days",
                 title="Response Time by Complaint Type")
    st.plotly_chart(fig, use_container_width=True)


