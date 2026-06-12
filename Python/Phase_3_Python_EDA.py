"""
Phase 3: Python Exploratory Data Analysis (EDA) & Visual EDA

This script contains the Phase 3 code from Superstore_EDA.ipynb.
It loads the cleaned dataset and performs numerical, categorical,
customer, product, time-series, and correlation analysis.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLEANED_DATA_PATH = PROJECT_ROOT / "Datasets" / "cleaned_superstore.csv"
VISUALS_DIR = Path(__file__).resolve().parent / "Visuals"


def save_plot(filename: str) -> None:
    VISUALS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = VISUALS_DIR / filename
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved visual: {output_path}")


def main() -> None:
    data = pd.read_csv(CLEANED_DATA_PATH)
    sns.set_style("whitegrid")

    # Phase 3.1: Numerical EDA Findings
    num_cols = ["Sales", "Profit", "Quantity", "Discount", "Shipping Duration"]

    print("\nNumerical Descriptive Statistics")
    print("=" * 50)
    print(data[num_cols].describe())

    print("\nNumerical Skewness")
    print("=" * 50)
    print(data[num_cols].skew())

    # Phase 3.2: Histogram Analysis
    for column in num_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(data[column], bins=20, kde=True)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        save_plot(f"histogram_{column.lower().replace(' ', '_')}.png")

    # Phase 3.3: Outlier Analysis Using BoxenPlot
    for column in num_cols:
        plt.figure(figsize=(8, 2))
        sns.boxenplot(x=data[column])
        plt.title(f"Boxenplot of {column}")
        save_plot(f"boxenplot_{column.lower().replace(' ', '_')}.png")

    # Phase 3.4: Categorical EDA - Region Analysis
    region_orders = data["Region"].value_counts()
    print("\nOrders by Region")
    print("=" * 50)
    print(region_orders)

    plt.figure(figsize=(8, 5))
    sns.countplot(x="Region", data=data)
    plt.title("Number of Orders by Region")
    plt.xlabel("Region")
    plt.ylabel("Order Count")
    save_plot("region_order_count.png")

    region_sales = data.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    print("\nTotal Sales by Region")
    print("=" * 50)
    print(region_sales)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=region_sales.index, y=region_sales.values)
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    save_plot("region_total_sales.png")

    region_profit = data.groupby("Region")["Profit"].sum().sort_values(ascending=False)
    print("\nTotal Profit by Region")
    print("=" * 50)
    print(region_profit)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=region_profit.index, y=region_profit.values)
    plt.title("Total Profit by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Profit")
    save_plot("region_total_profit.png")

    # Phase 3.5: Segment Analysis
    segment_orders = data["Segment"].value_counts()
    print("\nOrders by Segment")
    print("=" * 50)
    print(segment_orders)

    plt.figure(figsize=(8, 5))
    sns.countplot(x="Segment", data=data, order=segment_orders.index)
    plt.title("Number of Orders by Segment")
    plt.xlabel("Segment")
    plt.ylabel("Order Count")
    save_plot("segment_order_count.png")

    segment_sales = data.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
    print("\nTotal Sales by Segment")
    print("=" * 50)
    print(segment_sales)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=segment_sales.index, y=segment_sales.values)
    plt.title("Total Sales by Segment")
    plt.xlabel("Segment")
    plt.ylabel("Total Sales")
    save_plot("segment_total_sales.png")

    segment_profit = data.groupby("Segment")["Profit"].sum().sort_values(ascending=False)
    print("\nTotal Profit by Segment")
    print("=" * 50)
    print(segment_profit)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=segment_profit.index, y=segment_profit.values)
    plt.title("Total Profit by Segment")
    plt.xlabel("Segment")
    plt.ylabel("Total Profit")
    save_plot("segment_total_profit.png")

    segment_margin = data.groupby("Segment").agg({"Sales": "sum", "Profit": "sum"})
    segment_margin["Profit Margin (%)"] = (
        segment_margin["Profit"] / segment_margin["Sales"]
    ) * 100
    print("\nProfit Margin by Segment")
    print("=" * 50)
    print(segment_margin)

    # Phase 3.6: Category & Sub-Category Analysis
    category_sales = data.groupby("Category")["Sales"].sum().sort_values(ascending=False)
    print("\nTotal Sales by Category")
    print("=" * 50)
    print(category_sales)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=category_sales.index, y=category_sales.values)
    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    save_plot("category_total_sales.png")

    category_profit = data.groupby("Category")["Profit"].sum().sort_values(ascending=False)
    print("\nTotal Profit by Category")
    print("=" * 50)
    print(category_profit)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=category_profit.index, y=category_profit.values)
    plt.title("Total Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Profit")
    save_plot("category_total_profit.png")

    category_margin = data.groupby("Category").agg({"Sales": "sum", "Profit": "sum"})
    category_margin["Profit Margin (%)"] = (
        category_margin["Profit"] / category_margin["Sales"]
    ) * 100
    print("\nProfit Margin by Category")
    print("=" * 50)
    print(category_margin.sort_values("Profit Margin (%)", ascending=False))

    sub_sales = data.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
    print("\nSales by Sub-Category")
    print("=" * 50)
    print(sub_sales)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=sub_sales.values, y=sub_sales.index)
    plt.title("Sales by Sub-Category")
    plt.xlabel("Total Sales")
    plt.ylabel("Sub-Category")
    save_plot("sub_category_sales.png")

    sub_profit = data.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)
    print("\nProfit by Sub-Category")
    print("=" * 50)
    print(sub_profit)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=sub_profit.values, y=sub_profit.index)
    plt.title("Profit by Sub-Category")
    plt.xlabel("Total Profit")
    plt.ylabel("Sub-Category")
    save_plot("sub_category_profit.png")

    # Phase 3.7: Discount Analysis
    discount_profit_corr = data[["Discount", "Profit"]].corr()
    print("\nDiscount and Profit Correlation")
    print("=" * 50)
    print(discount_profit_corr)

    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=data["Discount"], y=data["Profit"], alpha=0.5)
    plt.title("Discount vs Profit")
    plt.xlabel("Discount")
    plt.ylabel("Profit")
    save_plot("discount_vs_profit.png")

    discount_profit = data.groupby("Discount")["Profit"].mean().sort_values(ascending=False)
    print("\nAverage Profit by Discount Level")
    print("=" * 50)
    print(discount_profit)

    plt.figure(figsize=(10, 5))
    sns.barplot(x=discount_profit.index, y=discount_profit.values)
    plt.title("Average Profit by Discount Level")
    plt.xlabel("Discount")
    plt.ylabel("Average Profit")
    save_plot("discount_average_profit.png")

    discount_sales = data.groupby("Discount")["Sales"].mean()
    print("\nAverage Sales by Discount Level")
    print("=" * 50)
    print(discount_sales)

    plt.figure(figsize=(10, 5))
    sns.barplot(x=discount_sales.index, y=discount_sales.values)
    plt.title("Average Sales by Discount Level")
    plt.xlabel("Discount")
    plt.ylabel("Average Sales")
    save_plot("discount_average_sales.png")

    # Phase 3.8: Customer Analysis
    top_sales_customers = (
        data.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
    )
    print("\nTop 10 Customers by Sales")
    print("=" * 50)
    print(top_sales_customers)

    plt.figure(figsize=(12, 5))
    sns.barplot(x=top_sales_customers.values, y=top_sales_customers.index)
    plt.title("Top 10 Customers by Sales")
    plt.xlabel("Total Sales")
    plt.ylabel("Customer Name")
    save_plot("top_10_customers_by_sales.png")

    bottom_profit_customers = (
        data.groupby("Customer Name")["Profit"].sum().sort_values().head(10)
    )
    print("\nBottom 10 Customers by Profit")
    print("=" * 50)
    print(bottom_profit_customers)

    plt.figure(figsize=(12, 5))
    sns.barplot(x=bottom_profit_customers.values, y=bottom_profit_customers.index)
    plt.title("Bottom 10 Customers by Profit")
    plt.xlabel("Total Profit")
    plt.ylabel("Customer Name")
    save_plot("bottom_10_customers_by_profit.png")

    customer_margin = data.groupby("Customer Name").agg({"Sales": "sum", "Profit": "sum"})
    customer_margin["Profit Margin (%)"] = (
        customer_margin["Profit"] / customer_margin["Sales"]
    ) * 100
    print("\nTop 10 Customers by Profit Margin")
    print("=" * 50)
    print(customer_margin.sort_values("Profit Margin (%)", ascending=False).head(10))

    # Phase 3.9: Product Analysis
    top_sales_products = (
        data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
    )
    print("\nTop 10 Products by Sales")
    print("=" * 50)
    print(top_sales_products)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_sales_products.values, y=top_sales_products.index)
    plt.title("Top 10 Products by Sales")
    plt.xlabel("Total Sales")
    plt.ylabel("Product Name")
    save_plot("top_10_products_by_sales.png")

    top_profit_products = (
        data.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)
    )
    print("\nTop 10 Products by Profit")
    print("=" * 50)
    print(top_profit_products)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_profit_products.values, y=top_profit_products.index)
    plt.title("Top 10 Products by Profit")
    plt.xlabel("Total Profit")
    plt.ylabel("Product Name")
    save_plot("top_10_products_by_profit.png")

    bottom_profit_products = (
        data.groupby("Product Name")["Profit"].sum().sort_values().head(10)
    )
    print("\nBottom 10 Products by Profit")
    print("=" * 50)
    print(bottom_profit_products)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=bottom_profit_products.values, y=bottom_profit_products.index)
    plt.title("Bottom 10 Products by Profit")
    plt.xlabel("Total Profit")
    plt.ylabel("Product Name")
    save_plot("bottom_10_products_by_profit.png")

    product_margin = data.groupby("Product Name").agg({"Sales": "sum", "Profit": "sum"})
    product_margin["Profit Margin (%)"] = (
        product_margin["Profit"] / product_margin["Sales"]
    ) * 100
    print("\nTop 10 Products by Profit Margin")
    print("=" * 50)
    print(product_margin.sort_values("Profit Margin (%)", ascending=False).head(10))

    # Phase 3.10: Time Series Analysis
    print("\nDate Column Data Types Before Conversion")
    print("=" * 50)
    print(data[["Order Date", "Ship Date"]].dtypes)

    data["Order Date"] = pd.to_datetime(data["Order Date"], format="%Y-%m-%d")
    data["Ship Date"] = pd.to_datetime(data["Ship Date"], format="%Y-%m-%d")

    print("\nDate Column Data Types After Conversion")
    print("=" * 50)
    print(data[["Order Date", "Ship Date"]].dtypes)

    monthly_sales = data.groupby(data["Order Date"].dt.to_period("M"))["Sales"].sum()
    print("\nMonthly Sales Trend")
    print("=" * 50)
    print(monthly_sales)

    plt.figure(figsize=(14, 5))
    monthly_sales.plot(marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    save_plot("monthly_sales_trend.png")

    monthly_profit = data.groupby(data["Order Date"].dt.to_period("M"))["Profit"].sum()
    print("\nMonthly Profit Trend")
    print("=" * 50)
    print(monthly_profit)

    plt.figure(figsize=(14, 5))
    monthly_profit.plot(marker="o")
    plt.title("Monthly Profit Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Profit")
    plt.xticks(rotation=45)
    save_plot("monthly_profit_trend.png")

    yearly_sales = data.groupby("Order Year")["Sales"].sum()
    print("\nYearly Sales")
    print("=" * 50)
    print(yearly_sales)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=yearly_sales.index, y=yearly_sales.values)
    plt.title("Yearly Sales")
    plt.xlabel("Year")
    plt.ylabel("Total Sales")
    save_plot("yearly_sales.png")

    yearly_profit = data.groupby("Order Year")["Profit"].sum()
    print("\nYearly Profit")
    print("=" * 50)
    print(yearly_profit)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=yearly_profit.index, y=yearly_profit.values)
    plt.title("Yearly Profit")
    plt.xlabel("Year")
    plt.ylabel("Total Profit")
    save_plot("yearly_profit.png")

    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    month_sales = data.groupby("Order Month")["Sales"].sum().reindex(month_order)
    print("\nSales by Month")
    print("=" * 50)
    print(month_sales)

    plt.figure(figsize=(12, 5))
    sns.barplot(x=month_sales.index, y=month_sales.values)
    plt.title("Sales by Month")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    save_plot("sales_by_month.png")

    quarter_sales = data.groupby("Order Quarter")["Sales"].sum()
    print("\nSales by Quarter")
    print("=" * 50)
    print(quarter_sales)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=quarter_sales.index, y=quarter_sales.values)
    plt.title("Sales by Quarter")
    plt.xlabel("Quarter")
    plt.ylabel("Total Sales")
    save_plot("sales_by_quarter.png")

    # Phase 3.11: Correlation Analysis
    corr_matrix = data[["Sales", "Profit", "Quantity", "Discount", "Shipping Duration"]].corr()
    print("\nCorrelation Matrix")
    print("=" * 50)
    print(corr_matrix)

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    save_plot("correlation_heatmap.png")

    pair_grid = sns.pairplot(data[["Sales", "Profit", "Quantity", "Discount"]])
    pair_grid.savefig(VISUALS_DIR / "pairplot_sales_profit_quantity_discount.png", dpi=300)
    plt.close(pair_grid.fig)
    print(f"Saved visual: {VISUALS_DIR / 'pairplot_sales_profit_quantity_discount.png'}")

    profit_corr = corr_matrix["Profit"].sort_values(ascending=False)
    print("\nProfit Correlation")
    print("=" * 50)
    print(profit_corr)


if __name__ == "__main__":
    main()
