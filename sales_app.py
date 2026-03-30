import streamlit as st
import pandas as pd

# Title and description
st.title("📊 Sales Summary Dashboard")
st.subheader("Interactive sales report with category filter")

# Hardcoded dataset
data = {
    "Product": ["Laptop", "Shirt", "Phone", "Shoes", "Tablet", "Jacket"],
    "Category": ["Electronics", "Clothing", "Electronics", "Footwear", "Electronics", "Clothing"],
    "Sales": [50000, 15000, 30000, 12000, 25000, 18000]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Filter Options")
category_options = df["Category"].unique()
selected_category = st.sidebar.selectbox("Select Category", category_options)

# Filter data
filtered_df = df[df["Category"] == selected_category]

# Display filtered data
st.write(f"### Showing data for: {selected_category}")
st.dataframe(filtered_df)

# Line chart
st.write("### Sales Trend")
st.line_chart(filtered_df["Sales"])
