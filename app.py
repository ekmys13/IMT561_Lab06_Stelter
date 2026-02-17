import streamlit as st
import pandas as pd

from src.data import load_data
from src.filters import render_filters, apply_filters
from src.charts import plot_response_hist, plot_borough_bar
from src.layouts import header_metrics, body_layout_tabs


# -----------------------------
# IMT 561 Streamlit Lab Starter
# -----------------------------
#
# This repo is intentionally incomplete.
# During the lab, the instructor fills in TODO blocks live.
# Students then extend the same app for the in-class activity + assignment.
#


def main() -> None:
    st.set_page_config(
        page_title="NYC 311 Mini Dashboard (Lab)",
        layout="wide",
    )

    st.title("NYC 311 Mini Dashboard - Em Stelter, IMT 561")
    st.caption("Starter app for IMT 561 lab: layouts + filters + coordinated views.")

    # ✅ Data loading (cached)
    df = load_data("data/sample.csv")

    # -------------------------
    # TODO (DEMO): Add a quick 'data sanity' check
    # - show row count
    # - show first 5 rows (optional)
    # -------------------------
    # HINT: st.write / st.dataframe
    st.write("Row count: ", len(df))
    st.dataframe(df.head())

    # -------------------------
    # Filters (sidebar by default)
    # -------------------------
    # render_filters returns a dictionary of user selections
    selections = render_filters(df)

    # apply_filters returns a filtered dataframe based on selections
    df_f = apply_filters(df, selections)

    # -------------------------
    # TODO (DEMO): Explain Streamlit re-runs
    # - changing a widget reruns the script top-to-bottom
    # - df_f changes because selections changes
    # -------------------------
    # '''Student response: I'm not sure if this is something we need to respond to since this was supposed to be explained
     # in class, but my understanding is that calling st.rerun immediately reruns the script, and by default it reruns the
     # entire app script; however, you can set it to run in a fragment instead
     # (https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun).'''
    # -------------------------
    # Header metrics
    # -------------------------
    # TODO (IN-CLASS): Replace placeholder metrics with real calculations
    st.divider()
    header_metrics(df_f)
    st.divider()

    # -------------------------
    # Main body
    # -------------------------
    # Tabs layout by default (3 tabs)
    tab_choice = st.radio(
        "Choose a layout for the body (lab demo uses tabs; assignment can remix):",
        ["Tabs (3)", "Two Columns"],
        horizontal=True,
    )

    if tab_choice == "Tabs (3)":
        body_layout_tabs(df_f)
    else:
        # -------------------------
        # TODO (DEMO): Implement a 2-column layout
        # - left column: a chart
        # - right column: a table
        # -------------------------
        # HINT: st.columns(2)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Response Time Distribution")
            plot_response_hist(df_f)

        with col2:
            st.subheader("Filtered Rows")
            st.dataframe(df_f, use_container_width=True, height=420)


    # -------------------------
    # TODO (IN-CLASS): Add a footer with a short 'design note'
    # - 2–3 sentences: who is the audience + what questions can they answer?
    # -------------------------
    st.divider()
    st.subheader("The audience for this dashboard might be someone who works in urban planning or utilities management for New York City. They can answer questions such as, 'How many complaints come in to 311 per borough (and overall) in the timespan of the dataset? What are the most common kinds of complaints per borough? What is the median response time to address these complaints? Which borough has the most complaints about rodents? (etc)")

if __name__ == "__main__":
    main()
