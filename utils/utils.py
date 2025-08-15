#!/usr/bin/env python
# coding: utf-8

# # Reusable Functions

# In[ ]:

import pandas as pd

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

