import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# Load the diamonds dataset
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")

diamonds = load_data()

st.image('Image/mysteries.png', width=800)

# Title of the web app
st.write(" # **Diamonds Dataset Analysis🔎💎**")

st.write("## **Created by:** `Aarish Asif Khan`")
st.write("## **Date:** `3rd April 2024`")

# Sidebar for dataset exploration options
st.sidebar.subheader("Data Exploration Options")
option = st.sidebar.selectbox("Select any option from below:", ["Overview of Dataset", "Visualizations", "Describing the Dataset"])

# Overview of the dataset
if option == "Overview of Dataset":
    st.write(diamonds.head())
    st.write("The dimensions of the dataset typically consist of around 53,940 rows and 10 columns. However, the specific dimensions may vary depending on the version or source of the dataset being used.")
    st.write(" ### **The dataset is composed of 10 variables which are listed below:**")
    
    st.write("1. `Carat:` Weight of the diamond in carats")
    st.write("2. `Cut:` quality of the cut (Fair, Good, Very Good, Premium, Ideal)")
    st.write("3. `Color:` color of the diamond (D, E, F, G, H, I, J)")
    st.write("4. `Clarity:` a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))")
    st.write("5. `Depth:` a measurement of the diamond's thickness (from 43 to 79 mm)")
    st.write("6. `Table:` a measurement of the width of the diamond's table (from 43 to 95 mm)")
    st.write("7. `Price:` the price in US dollars of the diamond")
    st.write("8. `X:` length in mm")
    st.write("9. `Y:` width in mm")
    st.write(". `Z:` depth in mm")
    
    st.write(" ### **About the Dataset:**")
    st.write("The diamonds dataset is a popular dataset often used for data analysis and machine learning tasks. It contains information about various characteristics of diamonds, such as carat weight, cut, color, clarity, and price. This dataset is commonly used in tutorials, educational materials, and data analysis projects to demonstrate techniques such as data visualization, descriptive statistics, and predictive modeling.")
    
    st.write(" ### **Founder of the Dataset:**")
    st.write("It is often included as part of datasets provided by various programming libraries and packages, such as ggplot2 in R or Seaborn in Python. There isn't a single founder or creator of this dataset in the traditional sense, as it is typically compiled from various sources for educational and analytical purposes. Therefore, it's more accurate to say that the dataset is curated and made available by the developers of the programming libraries or packages that include it.")

# Visualizations of the dataset
elif option == "Visualizations":
    st.write("## **Creating Box plots and Scatter plots!**")
    st.write("A scatter-plot shows the relationship between two continuous variables and each point represents a data observation. On the other hand, a box-plot summarizes distributions of a continuous variable and displays the median, quartiles, and outliers.")

    st.write("### - **The Price Distribution by Cut**")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='cut', y='price', data=diamonds)
    plt.title("Price Distribution by Cut")
    st.pyplot()

    st.write("### - **Carat vs Price**")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='carat', y='price', data=diamonds, alpha=0.5)
    plt.title("Carat vs Price")
    st.pyplot()
    
    st.write(" ## **What this Scatter plot represents:**")
    st.write("This plot compares the weight (carat) of diamonds to their price. Each dot represents a diamond and the horizontal axis shows the weight of the diamond, and the vertical axis shows its price. By looking at this plot, we can see if there's a relationship between a diamond's weight and its price. Generally, as the weight increases, the price tends to increase too.")
    
st.set_option('deprecation.showPyplotGlobalUse', False)

# Descriptive statistics of the dataset
if option == "Describing the Dataset":
    st.write("## **Descriptive Statistics of the Dataset:**")
    
    st.write("In order to describe a dataset, you need to keep the following point in mind:")
    
    st.write("`Sumary statistics:` Calculate and examine summary statistics for numerical variables, such as mean, median, standard deviation, minimum, maximum, and quartiles. This provides insights into the central tendency and spread of the data.")
    st.write("`Explore categorical columns:` For categorical variables, determine the frequency or count of each category to understand the distribution of the data across different groups.")
    st.write("`Visualize the dataset:` Create visualizations such as histograms, box plots, scatter plots, or bar charts to further explore the distribution and relationships within the dataset.")
    
    st.write("## **Code snippet to Describe the data:**")
    
    st.write("By following these steps, you can easily understand on how you can describe your dataset. There is a short code snippet that will help to describe your data! The code is `your_dataset.describe()` Replace the your_dataset with the name of your dataset.")
    st.write(diamonds.describe())
    st.write("As you can see above, we used the code snippet and got the summary statistics of the diamonds dataset. You can implement the same too!")