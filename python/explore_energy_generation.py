import pyarrow.parquet as pq
import polars as pl
import pandas as pd
import squarify
import matplotlib.pyplot as plt
import seaborn as sns
import dataframe_image as dfi
import subprocess
import locale

# Read in the data
product_labs = pd.read_csv('../data/processed/SITCCodeandDescription.csv')
trade_data_all_years = pq.ParquetDataset('../data/processed/country_partner_sitcproduct4digit_year_all.parquet').read_pandas().to_pandas()
# Import the population data
# It is in csv format. Skip first four rows 
# Fifth row contains the column names
# Write the code 
pop_data = pd.read_csv('../data/processed/API_SP_POP_TOTL_DS2.csv', skiprows=4)

#print(trade_data_all_years.head(10))

# COnvert numeric columns to numeric data type
trade_data_all_years['export_value'] = pd.to_numeric(trade_data_all_years['export_value'], errors='coerce')
trade_data_all_years['import_value'] = pd.to_numeric(trade_data_all_years['import_value'], errors='coerce')
trade_data_all_years['trade_balance'] = trade_data_all_years['export_value'] - trade_data_all_years['import_value']

# Merge the product labels to the trade data
labelled_df = trade_data_all_years.merge(product_labs, left_on='sitc_product_code', right_on='parent_code', how='inner')

# Summarize the trade_balance by location_code and product_description
labelled_df = labelled_df.groupby(['year','location_code', 'parent_code', 'partner_code', 'description'])['trade_balance'].sum().reset_index()

# Merge the population data to the trade data
# Only keep the population data for 2020 
# Write the code
pop_data = pop_data[['Country Code', 'Country Name', '2020']]

# Rename 2020 to pop_2020
pop_data = pop_data.rename(columns={'2020': 'pop_2020'})

# Create a new variable trade_balance_millions to make the numbers more readable
labelled_df['trade_balance_millions'] = labelled_df['trade_balance'] / 1000000

# Join pop_data 
labelled_df = labelled_df.merge(pop_data, left_on='location_code', right_on='Country Code', how='inner')

# Create a trade_bal_by_population variable. This variable is the trade balance divided by the population 
# Write the code
labelled_df['trade_bal_by_population'] = labelled_df['trade_balance'] / labelled_df['pop_2020']

# Create a function that returns the top 10 products by trade balance for a given location_code
def top10_products(df, location_code):
    # Filter to the top 10 products by trade balance for CHN 
    top10 = df[df['location_code'] == location_code].sort_values(by='trade_balance_millions', ascending=False).head(10)
    # Select unique values from the parent_code and description columns 
    top10 = top10[['year','parent_code','location_code', 'partner_code', 'description', 'trade_balance_millions', 'trade_balance', 'pop_2020', 'trade_bal_by_population']].drop_duplicates()
    # convert to polars dataframe
    top10 = pl.from_pandas(top10)
    return top10

rwa_df = top10_products(labelled_df, 'RWA')
uga_df = top10_products(labelled_df, 'UGA')
ken_df = top10_products(labelled_df, 'KEN')
bdi_df = top10_products(labelled_df, 'BDI')
tza_df = top10_products(labelled_df, 'TZA')


# Create a function that returns the top 10 trade partners by trade balance weighted by population for a given location_code


# Convert the following code into a function 
# The function takes a dataframe and a location_code as input
# The function plots a barplot of the top 10 trade partners for the location_code
# The function saves the plot as a png to the output folder
# Create the function 
def plot_top10_partners(df, location_code):
    # Plot bar plot andsave plot as png to output folder. Use seaborn for styling
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.set_style("whitegrid")
    sns.catplot(x='trade_balance_millions', y='partner_code', data=df.to_pandas(), palette='Blues_d', kind='bar')
    plt.title(location_code)
    plt.xlabel('Trade Balance In Millions of USD')
    plt.ylabel('')
    plt.savefig('../output/top10partners_' + location_code + '.png', dpi=300, bbox_inches='tight')

# Call the function
plot_top10_partners(rwa_df, 'RWA')
plot_top10_partners(uga_df, 'UGA')
plot_top10_partners(ken_df, 'KEN')
plot_top10_partners(bdi_df, 'BDI')
plot_top10_partners(tza_df, 'TZA')

# Combine the five datasets 
combined_df = pl.concat([rwa_df, uga_df, ken_df, bdi_df, tza_df])
# Plot bar plot with each subfigure representing a country code 
# Use trade_bal_by_population as the y variable
# write the code 
fig, ax = plt.subplots(figsize=(10, 6))
sns.set_style("whitegrid")
sns.catplot(x='trade_bal_by_population', y='partner_code', data=combined_df.to_pandas(), palette='Blues_d', kind='bar', col='location_code')
plt.savefig('../output/top10partners_all.png', dpi=300, bbox_inches='tight')

# Plot bar plot andsave plot as png to output folder. Use seaborn for styling
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.set_style("whitegrid")
# sns.factorplot(x='trade_balance_millions', y='partner_code', data=rwa_top10.to_pandas(), palette='Blues_d', kind='bar')
# plt.title('Top 10 Partners for Rwanda')
# plt.xlabel('Trade Balance In Millions of USD')
# plt.ylabel('')
# plt.savefig('../output/top10partners_rwa.png', dpi=300, bbox_inches='tight')
