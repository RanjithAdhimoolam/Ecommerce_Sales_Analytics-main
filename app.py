import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="assets/ecommerce_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 2rem;
}

.dashboard-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 5px;
}

.dashboard-logo {
    width: 60px;
    height: 60px;
    object-fit: contain;
}

.dashboard-title {
    font-size: 34px;
    font-weight: 800;
    line-height: 1.3;
    margin-top: 10px;
    margin-bottom: 8px;
    padding-top: 5px;
    overflow: visible;
}

.dashboard-subtitle {
    color: #94a3b8;
    margin-top: 2px;
    margin-bottom: 22px;
}

[data-testid="stMetric"] {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 14px 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}

[data-testid="stMetricLabel"] {
    color: #cbd5e1 !important;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
}

.section-title {
    font-size: 20px;
    font-weight: 700;
    margin: 8px 0 12px;
}

[data-testid="stSidebar"] {
    background-color: #0f172a;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/Ecommerce_Sales_Analytics_Dataset.csv"
    )

    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"],
        format="%d-%m-%Y"
    )

    df["Year"] = df["Year"].astype(int)

    df["Month_Number"] = df[
        "Month_Number"
    ].astype(int)

    # Standardize Delhi naming
    df["City"] = df["City"].replace({"Delhi": "New Delhi"})

    # Standardize Laptop naming
    df["Product"] = df["Product"].replace(
        {"Business Laptop": "Laptop","Gaming Laptop": "Laptop","Smartphone": "Phone","Budget Phone": "Phone"}
    )

    

    return df


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🎛️ Filters")

st.sidebar.caption(
    "Use the filters to interact with the dashboard."
)


# Reset
if st.sidebar.button("🔄 Reset Filters"):

    # st.session_state["year_filter"] = "All Years"
    st.session_state["region_filter"] = "All Regions"
    st.session_state["state_filter"] = "All States"
    st.session_state["city_filter"] = "All Cities"
    st.session_state["category_filter"] = "All Categories"
    st.session_state["subcategory_filter"] = "All Sub-Categories"
    st.session_state["product_filter"] = "All Products"
    st.session_state["payment_filter"] = "All Payment Methods"
    st.session_state["channel_filter"] = "All Channels"
    st.session_state["status_filter"] = "All Statuses"

    st.session_state["date_filter"] = (
        df["Order_Date"].min().date(),
        df["Order_Date"].max().date()
    )

    # st.session_state["price_filter"] = (
    #     float(df["Unit_Price"].min()),
    #     float(df["Unit_Price"].max())
    # )

    # st.session_state["discount_filter"] = (
    #     float(df["Discount_Percent"].min()),
    #     float(df["Discount_Percent"].max())
    # )

    st.rerun()


# ============================================================
# DATE FILTER
# ============================================================

min_date = df["Order_Date"].min().date()
max_date = df["Order_Date"].max().date()

date_range = st.sidebar.date_input(
    "📅 Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
    key="date_filter"
)

if (
    isinstance(date_range, (tuple, list))
    and len(date_range) == 2
):

    start_date = date_range[0]
    end_date = date_range[1]

else:

    start_date = min_date
    end_date = max_date


# ============================================================
# YEAR FILTER
# ============================================================

# years = sorted(
#     df["Year"].unique()
# )

# selected_year = st.sidebar.selectbox(
#     "📆 Year",
#     ["All Years"] + years,
#     key="year_filter"
# )

# ============================================================
# REGION FILTER
# ============================================================

regions = sorted(
    df["Region"].unique()
)

selected_region = st.sidebar.selectbox(
    "🌍 Region",
    ["All Regions"] + regions,
    key="region_filter"
)


# ============================================================
# STATE FILTER
# ============================================================

states = sorted(
    df["State"].unique()
)

selected_state = st.sidebar.selectbox(
    "📍 State",
    ["All States"] + states,
    key="state_filter"
)

# ============================================================
# CITY FILTER
# ============================================================

# cities = sorted(
#     df["City"].unique()
# )

# selected_city = st.sidebar.selectbox(
#     "🏙️ City",
#     ["All Cities"] + cities,
#     key="city_filter"
# )


# ============================================================
# CATEGORY FILTER
# ============================================================

categories = sorted(
    df["Category"].unique()
)

selected_category = st.sidebar.selectbox(
    "🛍️ Category",
    ["All Categories"] + categories,
    key="category_filter"
)


# ============================================================
# SUB CATEGORY
# ============================================================

# subcategories = sorted(
#     df["Sub_Category"].unique()
# )

# selected_subcategory = st.sidebar.selectbox(
#     "📦 Sub-Category",
#     ["All Sub-Categories"] + subcategories,
#     key="subcategory_filter"
# )


# ============================================================
# PRODUCT
# ============================================================

products = sorted(
    df["Product"].unique()
)

selected_product = st.sidebar.selectbox(
    "🏷️ Product",
    ["All Products"] + products,
    key="product_filter"
)


# ============================================================
# PAYMENT METHOD
# ============================================================

payments = sorted(
    df["Payment_Method"].unique()
)

selected_payment = st.sidebar.selectbox(
    "💳 Payment Method",
    ["All Payment Methods"] + payments,
    key="payment_filter"
)


# ============================================================
# SALES CHANNEL
# ============================================================

channels = sorted(
    df["Sales_Channel"].unique()
)

selected_channel = st.sidebar.selectbox(
    "🛒 Sales Channel",
    ["All Channels"] + channels,
    key="channel_filter"
)


# ============================================================
# ORDER STATUS
# ============================================================

statuses = sorted(
    df["Order_Status"].unique()
)

selected_status = st.sidebar.selectbox(
    "📦 Order Status",
    ["All Statuses"] + statuses,
    key="status_filter"
)


# ============================================================
# PRICE FILTER
# ============================================================

# min_price = float(
#     df["Unit_Price"].min()
# )

# max_price = float(
#     df["Unit_Price"].max()
# )

# price_range = st.sidebar.slider(
#     "💰 Unit Price Range",
#     min_value=min_price,
#     max_value=max_price,
#     value=(min_price, max_price),
#     key="price_filter"
# )


# ============================================================
# DISCOUNT FILTER
# ============================================================

# min_discount = float(
#     df["Discount_Percent"].min()
# )

# max_discount = float(
#     df["Discount_Percent"].max()
# )

# discount_range = st.sidebar.slider(
#     "🏷️ Discount %",
#     min_value=min_discount,
#     max_value=max_discount,
#     value=(
#         min_discount,
#         max_discount
#     ),
#     key="discount_filter"
# )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df[
    (df["Order_Date"].dt.date >= start_date)
    &
    (df["Order_Date"].dt.date <= end_date)
].copy()


# Year
# if selected_year != "All Years":
#     filtered_df = filtered_df[
#         filtered_df["Year"] == selected_year
#     ]


# Region
if selected_region != "All Regions":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]


# State
if selected_state != "All States":
    filtered_df = filtered_df[
        filtered_df["State"] == selected_state
    ]


# City
# if selected_city != "All Cities":
#     filtered_df = filtered_df[
#         filtered_df["City"] == selected_city
#     ]


# Category
if selected_category != "All Categories":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]


# Sub-Category
# if selected_subcategory != "All Sub-Categories":
#     filtered_df = filtered_df[
#         filtered_df["Sub_Category"] == selected_subcategory
#     ]


# Product
if selected_product != "All Products":
    filtered_df = filtered_df[
        filtered_df["Product"] == selected_product
    ]


# Payment Method
if selected_payment != "All Payment Methods":
    filtered_df = filtered_df[
        filtered_df["Payment_Method"] == selected_payment
    ]


# Sales Channel
if selected_channel != "All Channels":
    filtered_df = filtered_df[
        filtered_df["Sales_Channel"] == selected_channel
    ]


# Order Status
if selected_status != "All Statuses":
    filtered_df = filtered_df[
        filtered_df["Order_Status"] == selected_status
    ]


# Price
# filtered_df = filtered_df[
#     filtered_df["Unit_Price"].between(
#         price_range[0],
#         price_range[1]
#     )
# ]


# Discount
# filtered_df = filtered_df[
#     filtered_df["Discount_Percent"].between(
#         discount_range[0],
#         discount_range[1]
#     )
# ]


# ============================================================
# EMPTY DATA CHECK
# ============================================================

if filtered_df.empty:

    st.error(
        "No data available for the selected filters."
    )

    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_sales = filtered_df[
    "Sales"
].sum()

total_profit = filtered_df[
    "Profit"
].sum()

total_orders = filtered_df[
    "Order_ID"
].nunique()

total_quantity = filtered_df[
    "Quantity"
].sum()

total_customers = filtered_df[
    "Customer_ID"
].nunique()


# Average order value

avg_order_value = (

    total_sales / total_orders

    if total_orders

    else 0

)


# Profit margin

profit_margin = (

    total_profit
    /
    total_sales
    *
    100

    if total_sales

    else 0

)


# Average rating

avg_rating = filtered_df[
    "Customer_Rating"
].mean()


# ============================================================
# HEADER
# ============================================================

logo_col, title_col = st.columns([0.7, 10])

with logo_col:
    st.markdown(
        '<div style="padding-top: 10px;">',
        unsafe_allow_html=True
    )

    st.image(
        "assets/ecommerce_logo.png",
        width=60
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

with title_col:
    st.markdown(
        '<div class="dashboard-title">'
        'E-COMMERCE SALES DASHBOARD'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="dashboard-subtitle">'
    "Real-time revenue, order fulfillment, and profitability analytics"
    '</div>',
    unsafe_allow_html=True
)

# ============================================================
# KPI ROW 1
# ============================================================

k1, k2, k3, k4 = st.columns(4)


k1.metric(
    "💰 Total Revenue",
    f"₹{total_sales / 1_000_000:.2f}M"
)

k2.metric(
    "📦 Total Orders",
    f"{total_orders:,}"
)

k3.metric(
    "🧾 Average Order Value",
    f"₹{avg_order_value:,.0f}"
)

k4.metric(
    "🔢 Total Quantity",
    f"{total_quantity:,}"
)


# ============================================================
# KPI ROW 2
# ============================================================

k5, k6, k7, k8 = st.columns(4)


k5.metric(
    "💵 Total Profit",
    f"₹{total_profit / 1_000_000:.2f}M"
)

k6.metric(
    "📈 Profit Margin",
    f"{profit_margin:.2f}%"
)

k7.metric(
    "👥 Customers",
    f"{total_customers:,}"
)

k8.metric(
    "⭐ Avg Rating",
    f"{avg_rating:.2f}"
)


st.divider()


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "📊 Overview",
        "📦 Product Analysis",
        "👥 Customer Analysis",
        "🌍 Geographic Analysis",
        "📈 Trends & Forecast"
    ]
)


# ============================================================
# OVERVIEW
# ============================================================

with tab1:

    st.markdown(
        '<div class="section-title">'
        'Sales Graphs'
        '</div>',
        unsafe_allow_html=True
    )


    # Monthly data

    monthly = (
        filtered_df
        .groupby(
            pd.Grouper(
                key="Order_Date",
                freq="MS"
            )
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order_ID", "nunique")
        )
        .reset_index()
    )


    # --------------------------------------------------------
    # Sales trend
    # --------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        fig = px.line(
            monthly,
            x="Order_Date",
            y="Sales",
            markers=True,
            title="📈 Monthly Sales Trend"
        )

        fig.update_traces(
            fill="tozeroy",
            fillcolor="rgba(56, 189, 248, 0.08)",
            line=dict(color="#38bdf8", width=2.5),
        )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Sales (₹)",
            height=420,
            hovermode="x unified",
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )


    # --------------------------------------------------------
    # Profit trend
    # --------------------------------------------------------

    with col2:

        fig = px.line(
            monthly,
            x="Order_Date",
            y="Profit",
            markers=True,
            title="💵 Monthly Profit Trend"
        )

        fig.update_traces(
            fill="tozeroy",
            fillcolor="rgba(74, 222, 128, 0.08)",
            line=dict(color="#4ade80", width=2.5),
        )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Profit (₹)",
            height=420,
            hovermode="x unified",
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )
    st.caption("ℹ️ *Note: August 2026 data represents a partial month.*")

    # --------------------------------------------------------
    # City
    # --------------------------------------------------------

    col3, col4 = st.columns(2)

    city_sales = (
        filtered_df.groupby("City", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    max_city_sales = city_sales["Sales"].max()

    with col3:
        fig = px.bar(
            city_sales.sort_values("Sales"),
            x="Sales",
            y="City",
            orientation="h",
            title="🏙️ Top 10 Cities by Sales"
        )

        fig.update_traces(
            texttemplate="₹%{x:.2s}",
            textposition="outside",
            cliponaxis=False
        )

        fig.update_layout(
            xaxis_title="Sales (₹)",
            yaxis_title="City",
            height=430,
            xaxis=dict(range=[0, max_city_sales * 1.18]),
            margin=dict(r=40)                        
        )

        st.plotly_chart(fig, width="stretch")

    # --------------------------------------------------------
    # Category
    # --------------------------------------------------------

    category_sales = filtered_df.groupby("Category", as_index=False).agg(
        Sales=("Sales", "sum"), 
        Profit=("Profit", "sum")
    )

    with col4:
        fig = px.bar(
            category_sales,
            x="Category",
            y=["Sales", "Profit"],
            barmode="group",
            title="🛍️ Sales vs Profit by Category",
            labels={"value": "Amount (₹)", "variable": "Metric"}
        )
        fig.update_layout(
            yaxis_title="Amount (₹)",
            legend_title_text="",
            height=430
        )
        st.plotly_chart(
            fig, 
            width="stretch"
        )


    # --------------------------------------------------------
    # Payment
    # --------------------------------------------------------

    col5, col6 = st.columns(2)

    with col5:
        payment = filtered_df.groupby("Payment_Method", as_index=False).agg(
            Sales=("Sales", "sum")
        )
        fig = px.pie(
            payment,
            names="Payment_Method",
            values="Sales",
            hole=0.48,
            title="💳 Revenue by Payment Method",
        )

        fig.update_traces(
            textposition="auto",
            textinfo="percent",
            insidetextorientation="horizontal",
        )
        fig.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h", yanchor="top", y=-0.05, xanchor="center", x=0.5
            ),
            height=380,
        )

        st.plotly_chart(fig, width="stretch")


    # --------------------------------------------------------
    # Status
    # --------------------------------------------------------

    with col6:
        status = filtered_df.groupby("Order_Status", as_index=False).agg(
            Orders=("Order_ID", "nunique")
        )
        fig = px.pie(
            status,
            names="Order_Status",
            values="Orders",
            hole=0.48,
            title="📦 Order Status Distribution",
        )
        fig.update_traces(
            textposition="auto",
            textinfo="percent",
            insidetextorientation="horizontal",
        )
        fig.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h", yanchor="top", y=-0.05, xanchor="center", x=0.5
            ),
            height=380,
        )

        st.plotly_chart(fig, width="stretch")


    # --------------------------------------------------------
    # Channel
    # --------------------------------------------------------


    channel = (
        filtered_df.groupby("Sales_Channel", as_index=False)
        .agg(Sales=("Sales", "sum"), Orders=("Order_ID", "nunique"))
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        channel,
        x="Sales_Channel",
        y="Sales",
        color="Sales_Channel",
        title="🛒 Sales by Channel",
    )

    fig.update_traces(
        texttemplate="₹%{y:.2s}",
        textposition="outside",
        showlegend=False, 
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Sales (₹)",
        height=400,
        yaxis=dict(range=[0, channel["Sales"].max() * 1.15]), 
    )

    st.plotly_chart(fig, width="stretch")

# ============================================================
# PRODUCT ANALYSIS
# ============================================================

with tab2:

    st.markdown(
        '<div class="section-title">'
        'Product Performance'
        '</div>',
        unsafe_allow_html=True
    )


    product_summary = (
        filtered_df
        .groupby(
            [
                "Category",
                "Sub_Category",
                "Product"
            ],
            as_index=False
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum"),
            Orders=("Order_ID", "nunique"),
            Rating=(
                "Customer_Rating",
                "mean"
            )
        )
    )


    # Top products

    col1, col2 = st.columns(2)

    top_products = (
        product_summary
        .sort_values("Sales", ascending=False)
        .head(10)
        .sort_values("Sales")
    )

    # Calculate max sales specifically for top products
    max_product_sales = top_products["Sales"].max()

    with col1:
        fig = px.bar(
            top_products,
            x="Sales",
            y="Product",
            orientation="h",
            title="🏆 Top 10 Products by Revenue"
        )

        fig.update_traces(
            texttemplate="₹%{x:.2s}",
            textposition="outside",
            cliponaxis=False
        )

        fig.update_layout(
            xaxis_title="Sales (₹)",
            yaxis_title="Product",                                  # Fixed from "City"
            height=430,
            xaxis=dict(range=[0, max_product_sales * 1.20]),         # Uses max_product_sales + 20% buffer
            margin=dict(r=50)                                        # Adds extra right margin
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )


    # Top profit

    top_profit = (
        product_summary
        .sort_values(
            "Profit",
            ascending=False
        )
        .head(10)
        .sort_values("Profit")
    )

    max_product_sales = top_products["Profit"].max()


    with col2:

        fig = px.bar(
            top_profit,
            x="Profit",
            y="Product",
            orientation="h",
            title="💰 Top 10 Products by Profit"
        )

        fig.update_traces(
            texttemplate="₹%{x:.2s}",
            textposition="outside",
            cliponaxis=False
        )

        fig.update_layout(
            xaxis_title="Sales (₹)",
            yaxis_title="Product",                                  # Fixed from "City"
            height=430,
            xaxis=dict(range=[0, max_product_sales * 1.20]),         # Uses max_product_sales + 20% buffer
            margin=dict(r=50)                                        # Adds extra right margin
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )


    # Quantity

    quantity_products = (
        product_summary
        .sort_values(
            "Quantity",
            ascending=False
        )
        .head(10)
        .sort_values("Quantity")
    )


    fig = px.bar(
        quantity_products,
        x="Quantity",
        y="Product",
        orientation="h",
        title="🔢 Top Products by Quantity Sold"
    )

    fig.update_traces(
        texttemplate="%{x:,}",
        textposition="outside",
        cliponaxis=False,
    )
    fig.update_layout(
        xaxis_title="Quantity",
        yaxis_title="Product",
        height=400,
        xaxis=dict(range=[0, quantity_products["Quantity"].max() * 1.15]),
        margin=dict(r=40),
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


    # Scatter

    fig = px.scatter(
        product_summary,
        x="Sales",
        y="Profit",
        size="Quantity",
        color="Category",
        hover_name="Product",
        title="📌 Product Sales vs Profit"
    )

    fig.update_layout(
        xaxis_type="log",
        yaxis_type="log",
        xaxis_title="Sales (₹, Log Scale)",
        yaxis_title="Profit (₹, Log Scale)",
        height=450,
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # Product Table
    
    st.subheader("Product Details")

    table = product_summary.copy()

    st.dataframe(
        table,
        width="stretch",
        hide_index=True,
        column_config={
            "Sales": st.column_config.NumberColumn(
                "Sales",
                format="₹%,.0f",
            ),
            "Profit": st.column_config.NumberColumn(
                "Profit",
                format="₹%,.0f",
            ),
            "Quantity": st.column_config.NumberColumn(
                "Quantity",
                format="%d",
            ),
            "Orders": st.column_config.NumberColumn(
                "Orders",
                format="%d",
            ),
            "Rating": st.column_config.NumberColumn(
                "Rating",
                format="%.2f ⭐",
            ),
        },
    )
# ============================================================
# CUSTOMER ANALYSIS
# ============================================================

with tab3:

    st.markdown(
        '<div class="section-title">'
        'Customer Performance'
        '</div>',
        unsafe_allow_html=True
    )


    customer_summary = (
        filtered_df
        .groupby(
            [
                "Customer_ID",
                "Customer_Name",
                "Gender",
                "Customer_Segment"
            ],
            as_index=False
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order_ID", "nunique"),
            Quantity=("Quantity", "sum"),
            Rating=(
                "Customer_Rating",
                "mean"
            )
        )
        .sort_values(
            "Sales",
            ascending=False
        )
    )


    col1, col2 = st.columns(2)


    # Top customers

    with col1:

        top_customers = (
            customer_summary
            .head(10)
            .sort_values("Sales")
        )
        max_cust_sales = top_customers["Sales"].max()

        fig = px.bar(
            top_customers,
            x="Sales",
            y="Customer_Name",
            orientation="h",
            title="👑 Top 10 Customers"
        )

        fig.update_traces(
            texttemplate="₹%{x:.2s}",
            textposition="outside",
            cliponaxis=False,
        )
        fig.update_layout(
            xaxis_title="Sales (₹)",
            yaxis_title="Customer",
            height=430,
            xaxis=dict(range=[0, max_cust_sales * 1.20]),
            margin=dict(r=45),
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )


    # Segments

    with col2:

        segment = (
            filtered_df
            .groupby(
                "Customer_Segment",
                as_index=False
            )
            .agg(
                Sales=("Sales", "sum"),
                Customers=(
                    "Customer_ID",
                    "nunique"
                )
            )
            .sort_values("Sales", ascending=False)
        )

        fig = px.bar(
            segment,
            x="Customer_Segment",
            y="Sales",
            title="🎯 Sales by Customer Segment",
            text_auto=".2s"
        )

        fig.update_traces(
            texttemplate="₹%{y:.2s}",
            textposition="outside",
            cliponaxis=False,
        )
        fig.update_layout(
            xaxis_title="",
            yaxis_title="Sales (₹)",
            height=430,
            yaxis=dict(range=[0, segment["Sales"].max() * 1.15]),
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )


    col3, col4 = st.columns(2)


    # Gender

    with col3:

        gender = (
            filtered_df
            .groupby(
                "Gender",
                as_index=False
            )
            .agg(
                Sales=("Sales", "sum")
            )
        )

        fig = px.pie(
            gender,
            names="Gender",
            values="Sales",
            hole=0.45,
            title="👤 Revenue by Gender"
        )

        fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
            insidetextorientation="horizontal",
        )
        fig.update_layout(
            showlegend=False,
            height=400,
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )


    # Age groups

    with col4:

        age_bins = [
            17,
            25,
            35,
            45,
            55,
            65,
            100
        ]

        age_labels = [
            "18-25",
            "26-35",
            "36-45",
            "46-55",
            "56-65",
            "66+"
        ]

        temp = filtered_df.copy()

        temp["Age_Group"] = pd.cut(
            temp["Age"],
            bins=age_bins,
            labels=age_labels,
            include_lowest=True
        )

        age_sales = (
            temp
            .groupby(
                "Age_Group",
                observed=False,
                as_index=False
            )
            .agg(
                Sales=("Sales", "sum")
            )
        )

        fig = px.bar(
            age_sales,
            x="Age_Group",
            y="Sales",
            title="🎂 Sales by Customer Age Group",
            text_auto=".2s"
        )

        fig.update_traces(
            texttemplate="₹%{y:.2s}",
            textposition="outside",
            cliponaxis=False,
        )
        fig.update_layout(
            xaxis_title="Age Group",
            yaxis_title="Sales (₹)",
            height=400,
            yaxis=dict(range=[0, age_sales["Sales"].max() * 1.15]),
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # Customer Details Table

    st.subheader(
        "Customer Details"
    )

    st.dataframe(
        customer_summary.head(100),
        width="stretch",
        hide_index=True,
        column_config={
            "Customer_ID": "Customer ID",
            "Customer_Name": "Name",
            "Gender": "Gender",
            "Customer_Segment": "Segment",
            "Sales": st.column_config.NumberColumn(
                "Sales",
                format="₹%,.0f",
            ),
            "Profit": st.column_config.NumberColumn(
                "Profit",
                format="₹%,.0f",
            ),
            "Orders": st.column_config.NumberColumn(
                "Orders",
                format="%d",
            ),
            "Quantity": st.column_config.NumberColumn(
                "Quantity",
                format="%d",
            ),
            "Rating": st.column_config.NumberColumn(
                "Rating",
                format="%.2f ⭐",
            ),
        },
    )


# ============================================================
# GEOGRAPHIC ANALYSIS
# ============================================================

with tab4:

    st.markdown(
        '<div class="section-title">'
        'Geographic Performance'
        '</div>',
        unsafe_allow_html=True
    )


    region_summary = (
        filtered_df
        .groupby(
            "Region",
            as_index=False
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=(
                "Order_ID",
                "nunique"
            ),
            Customers=(
                "Customer_ID",
                "nunique"
            )
        )
        .sort_values(
            "Sales",
            ascending=False
        )
    )


    col1, col2 = st.columns(2)


    # Region sales

    with col1:

        fig = px.bar(
            region_summary,
            x="Region",
            y="Sales",
            title="🌍 Sales by Region",
            text_auto=".2s"
        )

        fig.update_traces(
            texttemplate="₹%{y:.2s}",
            textposition="outside",
            cliponaxis=False,
        )
        fig.update_layout(
            xaxis_title="",
            yaxis_title="Sales (₹)",
            height=430,
            yaxis=dict(range=[0, region_summary["Sales"].max() * 1.18]),
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )


    # Region profit

    with col2:

        fig = px.bar(
            region_summary,
            x="Region",
            y="Profit",
            title="💰 Profit by Region",
            text_auto=".2s"
        )

        fig.update_traces(
            texttemplate="₹%{y:.2s}",
            textposition="outside",
            cliponaxis=False,
        )
        fig.update_layout(
            xaxis_title="",
            yaxis_title="Profit (₹)",
            height=430,
            yaxis=dict(range=[0, region_summary["Profit"].max() * 1.18]),
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )


    # State

    state_summary = (
        filtered_df
        .groupby(
            [
                "State",
                "Region"
            ],
            as_index=False
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=(
                "Order_ID",
                "nunique"
            )
        )
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    top_15_states = state_summary.head(15).sort_values("Sales", ascending=True)
    max_state_sales = top_15_states["Sales"].max()


    fig = px.bar(
        state_summary
        .head(15)
        .sort_values("Sales"),
        x="Sales",
        y="State",
        color="Region",
        orientation="h",
        title="🇮🇳 Top 15 States by Sales",
        text_auto=".2s"
    )

    fig.update_traces(
        texttemplate="₹%{x:.2s}",
        textposition="outside",
        cliponaxis=False,
    )
    fig.update_layout(
        xaxis_title="Sales (₹)",
        yaxis_title="State",
        height=480,
        xaxis=dict(range=[0, max_state_sales * 1.18]),
        margin=dict(r=50),
        yaxis={"categoryorder": "total ascending"},  # Maintains strict sorted bar order
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


    # City scatter

    city_summary = (
        filtered_df
        .groupby(
            [
                "City",
                "State"
            ],
            as_index=False
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=(
                "Order_ID",
                "nunique"
            )
        )
    )


    fig = px.scatter(
        city_summary,
        x="Sales",
        y="Profit",
        size="Orders",
        color="State",
        hover_name="City",
        title="🏙️ City Sales vs Profit"
    )

    fig.update_layout(
        xaxis_title="Sales (₹)",
        yaxis_title="Profit (₹)",
        height=450,
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # State Summary Table

    st.subheader(
        "State Summary"
    )

    st.dataframe(
        state_summary,
        width="stretch",
        hide_index=True,
        column_config={
            "State": "State",
            "Region": "Region",
            "Sales": st.column_config.NumberColumn(
                "Sales",
                format="₹%,.0f",
            ),
            "Profit": st.column_config.NumberColumn(
                "Profit",
                format="₹%,.0f",
            ),
            "Orders": st.column_config.NumberColumn(
                "Orders",
                format="%d",
            ),
        },
    )


# ============================================================
# TRENDS AND FORECAST
# ============================================================

with tab5:

    st.markdown(
        '<div class="section-title">'
        'Trends & Forecast'
        '</div>',
        unsafe_allow_html=True
    )


    monthly = (
        filtered_df
        .groupby(
            pd.Grouper(
                key="Order_Date",
                freq="MS"
            )
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order_ID", "nunique")
        )
        .reset_index()
    )


    # Monthly orders

    fig = px.bar(
        monthly,
        x="Order_Date",
        y="Orders",
        title="📦 Monthly Orders"
    )

    fig.update_traces(
        texttemplate="%{y:,}",
        textposition="outside",
        cliponaxis=False,
    )
    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Orders",
        height=400,
        yaxis=dict(range=[0, monthly["Orders"].max() * 1.15]),
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


    # Moving average

    monthly["3_Month_Avg"] = (
        monthly["Sales"]
        .rolling(
            3,
            min_periods=1
        )
        .mean()
    )


    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=monthly["Order_Date"],
            y=monthly["Sales"],
            mode="lines+markers",
            name="Actual Sales",
            line=dict(color="#38bdf8", width=2)
        )
    )


    fig.add_trace(
        go.Scatter(
            x=monthly["Order_Date"],
            y=monthly["3_Month_Avg"],
            mode="lines",
            name="3-Month Moving Average",
            line=dict(color="#f59e0b", width=2.5, dash="dash")
        )
    )


    fig.update_layout(
        title="📊 Sales with 3-Month Moving Average",
        xaxis_title="Month",
        yaxis_title="Sales (₹)",
        height=420,
        hovermode="x unified"
    )


    st.plotly_chart(
        fig,
        width="stretch"
    )


    # ========================================================
    # FORECAST
    # ========================================================


    st.subheader("🔮 6-Month Sales Forecast")

    if len(monthly) >= 6:
        # Fit model on complete months to avoid partial-month skew
        fit_df = monthly.iloc[:-1] if len(monthly) > 6 else monthly

        fit_index = np.arange(len(fit_df))
        coefficients = np.polyfit(fit_index, fit_df["Sales"], 1)  # Linear trend avoids artificial crashes
        model = np.poly1d(coefficients)

        # Connect forecast directly to last historical data point
        last_date = monthly["Order_Date"].iloc[-1]
        last_sales = monthly["Sales"].iloc[-1]

        future_index = np.arange(len(fit_df), len(fit_df) + 6)
        future_dates = pd.date_range(
            last_date + pd.offsets.MonthBegin(1),
            periods=6,
            freq="MS",
        )

        forecast_values = np.maximum(model(future_index), 0)

        # Plotly chart connecting continuous line
        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=monthly["Order_Date"],
                y=monthly["Sales"],
                mode="lines+markers",
                name="Actual Sales",
                line=dict(color="#38bdf8", width=2),
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[last_date] + list(future_dates),
                y=[last_sales] + list(forecast_values),
                mode="lines+markers",
                name="Forecast",
                line=dict(color="#a855f7", width=2.5, dash="dot"),
            )
        )

        fig.update_layout(
            title="Actual vs Forecast Sales",
            xaxis_title="Month",
            yaxis_title="Sales (₹)",
            height=430,
            hovermode="x unified",
        )

        st.plotly_chart(fig, width="stretch")

        # --------------------------------------------------------
        # Forecast Summary Table (Clean Date & ₹ Format)
        # --------------------------------------------------------
        forecast_df = pd.DataFrame({
            "Month": future_dates.strftime("%B %Y"),
            "Forecasted Sales": np.round(forecast_values, 0),
        })

        st.dataframe(
            forecast_df,
            width="stretch",
            hide_index=True,
            column_config={
                "Month": "Forecast Month",
                "Forecasted Sales": st.column_config.NumberColumn(
                    "Forecasted Sales",
                    format="₹%,.0f",
                ),
            },
        )

    else:
        st.warning("At least 6 months of data are required.")


# ============================================================
# DOWNLOAD
# ============================================================

st.divider()


st.download_button(
    "⬇️ Download Filtered Dataset",

    filtered_df.to_csv(
        index=False
    ).encode("utf-8"),

    "filtered_ecommerce_sales.csv",

    "text/csv"
)


st.caption(
    f"Showing {len(filtered_df):,} records | "
    f"Date: {start_date} to {end_date}"
)

# Run Code
# py -m streamlit run app.py