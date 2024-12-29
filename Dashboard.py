# Importing necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Air Travel Dashboard",
    page_icon="✈️",
    layout="wide"
)

# Dashboard Title
st.title("✈️ Air Travel Dashboard")
st.markdown("Analyze the monthly air travel dataset and explore trends and patterns.")

# Load the dataset from GitHub
dataset_url = "https://github.com/TabeerJehanzeb783/DATA-Visualization/blob/main/airtravel.csv"
df = pd.read_csv(dataset_url)

# Display the dataset
st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

# Summary Statistics
st.subheader("Summary Statistics")
st.write(df.describe(include="all"))

# Column Selection for Visualizations
st.sidebar.header("Visualization Options")
all_columns = df.columns.tolist()
selected_columns = st.sidebar.multiselect("Select Columns for Visualization", all_columns)

# Visualization Section
if selected_columns:
    st.subheader("Visualizations")

    # Line Chart
    if st.checkbox("Show Line Chart"):
        st.line_chart(df[selected_columns])

    # Bar Chart
    if st.checkbox("Show Bar Chart"):
        st.bar_chart(df[selected_columns])

    # Histograms
    if st.checkbox("Show Histograms"):
        for column in selected_columns:
            if pd.api.types.is_numeric_dtype(df[column]):
                st.write(f"Histogram for {column}")
                fig, ax = plt.subplots()
                sns.histplot(df[column], bins=20, kde=True, ax=ax)
                st.pyplot(fig)
else:
    st.warning("Please select at least one column for visualization.")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Built with ❤️ using Streamlit")
