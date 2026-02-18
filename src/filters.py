import pandas as pd
import streamlit as st

# render filters --> pass in the dataframe; returns a dictionary (that's the -> dict part)
def render_filters(df: pd.DataFrame) -> dict:
    """Rendering filter widgets and returning the chosen values."""
    st.sidebar.header("Filters") # putting filters in the sidebar

    # create sorted lists of a few of the different categorical datasets
    boroughs = ["All"] + sorted(df["borough"].dropna().unique().tolist()) # drop NA values; get unique records; convert to list
    channels = ["All"] + sorted(df["channel"].dropna().unique().tolist())
    complaint_types = sorted(df["complaint_type"].dropna().unique().tolist())

    # my god this is so much better than PROTOTYPING IN FUCKING FIGMA

    # simple select box situation --> so users can only select one thing at a time
    borough = st.sidebar.selectbox("Borough", boroughs, index=0) # pass in boroughs list from above
    channel = st.sidebar.selectbox("Channel", channels, index=0) # pass in channels list from above

    # TODO (DEMO): Convert this selectbox to a multiselect (and update filtering logic)

    # complaint types: want user to be able to select multiple complaint types
    # complaint = st.sidebar.selectbox("Complaint Type", ["All"] + complaint_types, index=0)

    # multiselect version: user can tick multiple complaint types
    complaint = st.sidebar.multiselect("Complaint Type",
                                                   complaint_types,
                                                   default=complaint_types)

    # Response time slider
    min_rt, max_rt = float(df["response_time_days"].min()), float(df["response_time_days"].max())
    rt_range = st.sidebar.slider(
        "Response time (days)",
        min_value=0.0,
        max_value=float(max_rt),
        value=(0.0, float(min(30.0, max_rt))),
        step=0.5,
    )

    # TODO (IN-CLASS): Add a checkbox toggle to cap outliers (e.g., at 99th percentile)
    cap_outliers = st.sidebar.checkbox("Cap extreme response times", value=False)

    return {
        "borough": borough,
        "channel": channel,
        "complaint": complaint,
        "rt_range": rt_range,
        "cap_outliers": cap_outliers,
    }


def apply_filters(df: pd.DataFrame, selections: dict) -> pd.DataFrame:
    """Applying filter selections to the dataframe."""
    out = df.copy()

    if selections["borough"] != "All":
        out = out[out["borough"] == selections["borough"]]

    if selections["channel"] != "All":
        out = out[out["channel"] == selections["channel"]]

    if selections["complaint"] == "All" or selections["complaint"] == []:
        out = out

    else:
        out = out[out["complaint_type"].isin(selections['complaint'])]

    lo, hi = selections["rt_range"]
    out = out[(out["response_time_days"] >= lo) & (out["response_time_days"] <= hi)]

    # TODO (IN-CLASS): Implement outlier capping when cap_outliers is checked
    # HINT: use out["response_time_days"].quantile(0.99)
    if selections["cap_outliers"]:
        out = out[out['response_time_days'] <= out["response_time_days"].quantile(0.99)]

    return out.reset_index(drop=True)