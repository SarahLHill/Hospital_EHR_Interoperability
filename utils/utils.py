#!/usr/bin/env python
# coding: utf-8

# # Reusable Functions

# In[ ]:

import pandas as pd
import matplotlib.pyplot as plt

# ## Exploratory Data Analysis Function

# In[ ]:


def basic_eda(df: pd.DataFrame, show_head: bool = True, show_tail: bool = True, show_info: bool = True) -> None:
    """
    Prints a quick summary of a DataFrame, including shape, column names, data types,
    missing values, and optional previews of the data.

    Args:
        df: The pandas DataFrame to summarize.
        show_head: Whether to display df.head(). Default is True.
        show_tail: Whether to display df.tail(). Default is True.
        show_info: Whether to display df.info(). Default is True.

    Returns:
        None. Creates a printed summary.
    """

    print("DataFrame Shape:", df.shape)
    print("\n Column Names:")
    print(df.columns.tolist())

    print("\n Data Types:")
    print(df.dtypes)

    if show_info:
        print("\n DataFrame Info:")
        df.info()

    print("\n Null Values (%):")
    nulls = df.isnull().mean() * 100 #mean will give the decimal of total missing values and  * 100 will turn that into a percentage
    print(nulls[nulls > 0].round(2).sort_values(ascending=False)) #only displays columns with nulls, round the percent to 2 decimal places, and sorts high to low

    if show_head:
        print("\n Preview (Head):")
        print(df.head())

    if show_tail:
        print("\n Preview (Tail):")
        print(df.tail())


# ## Plot Style Function

# In[ ]:
def compare_ratings_by_ehr(df, rating_col='hospital_overall_rating', developer_col='developer_name', product_col='product_name'):
    """
    Compares hospital ratings across EHR developers and products.

    Parameters:
    - df (pd.DataFrame): Merged dataset containing hospital ratings and EHR info.
    - rating_col (str): Column name for hospital ratings.
    - developer_col (str): Column name for EHR developer.
    - product_col (str): Column name for EHR product.

    Returns:
    - pd.DataFrame: Summary table with average rating and hospital count per developer-product pair.
    """
    # Drop rows with missing ratings or developer/product info
    filtered_df = df.dropna(subset=[rating_col, developer_col, product_col])

    # Convert ratings to numeric if needed
    filtered_df[rating_col] = pd.to_numeric(filtered_df[rating_col], errors='coerce')
    # Group by developer and product
    summary = (
        filtered_df
        .groupby([developer_col, product_col])
        .agg(
            average_rating=(rating_col, 'mean'),
            hospital_count=(rating_col, 'count')
        )
        .reset_index()
        .sort_values(by='average_rating', ascending=False)
 )

# In[ ]:
