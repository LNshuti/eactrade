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

# Read in the data
trade_data_all_years = pq.ParquetDataset('../data/processed/country_partner_sitcproduct4digit_year_all.parquet').read_pandas().to_pandas()
print(trade_data_all_years.head(10))
trade_data_all_years['export_value'] = pd.to_numeric(trade_data_all_years['export_value'], errors='coerce')
trade_data_all_years['import_value'] = pd.to_numeric(trade_data_all_years['import_value'], errors='coerce')
trade_data_all_years['trade_balance'] = trade_data_all_years['export_value'] - trade_data_all_years['import_value']

labelled_df = trade_data_all_years.merge(product_labs, left_on='sitc_product_code', right_on='parent_code', how='inner')

#print(labelled_df.head(10))
# Filter location_code to the USA, CHN, and RUS (China, Russia, and the United States)
#labelled_df = labelled_df[labelled_df['location_code'].isin(['RWA', 'BDI', 'UGA'])]

# Summarize the trade_balance by location_code and product_description
labelled_df = labelled_df.groupby(['year','location_code', 'parent_code', 'partner_code', 'description'])['trade_balance'].sum().reset_index()

# Create a new variable trade_balance_millions to make the numbers more readable
labelled_df['trade_balance_millions'] = labelled_df['trade_balance'] / 1000000

# Filter to the top 10 products by trade balance for CHN 
rwa_df = labelled_df[labelled_df['location_code'] == 'RWA'].sort_values(by='trade_balance_millions', ascending=False)
uga_df = labelled_df[labelled_df['location_code'] == 'UGA'].sort_values(by='trade_balance_millions', ascending=False)

# Select unique values from the parent_code and description columns 
rwa_df = rwa_df[['year','parent_code','location_code', 'partner_code', 'description', 'trade_balance_millions']].drop_duplicates()
uga_df = uga_df[['year','parent_code','location_code', 'partner_code', 'description', 'trade_balance_millions']].drop_duplicates()
# convert to polars dataframe
rwa_df = pl.from_pandas(rwa_df)
uga_df = pl.from_pandas(uga_df)
#print(rwa_df)

# Select the top 10 partner_code by trade balance for RWA
rwa_top10 = rwa_df.groupby('partner_code').agg(pl.sum('trade_balance_millions')).sort('trade_balance_millions', reverse=True).head(10)
uga_top10 = uga_df.groupby('partner_code').agg(pl.sum('trade_balance_millions')).sort('trade_balance_millions', reverse=True).head(10)
print(rwa_top10)

# Convert the following code into a function 
# The function takes a dataframe and a location_code as input
# The function plots a barplot of the top 10 trade partners for the location_code
# The function saves the plot as a png to the output folder
# Create the function 
def plot_top10_partners(df, location_code):
    # Select the top 10 partner_code by trade balance for RWA
    top10 = df.groupby('partner_code').agg(pl.sum('trade_balance_millions')).sort('trade_balance_millions', reverse=True).head(10)
    # Plot bar plot andsave plot as png to output folder. Use seaborn for styling
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.set_style("whitegrid")
    sns.factorplot(x='trade_balance_millions', y='partner_code', data=top10.to_pandas(), palette='Blues_d', kind='bar')
    plt.title('Top 10 Partners for ' + location_code)
    plt.xlabel('Trade Balance In Millions of USD')
    plt.ylabel('')
    plt.savefig('../output/top10partners_' + location_code + '.png', dpi=300, bbox_inches='tight')

# Call the function
plot_top10_partners(rwa_df, 'RWA')
plot_top10_partners(uga_df, 'UGA')
# Plot bar plot andsave plot as png to output folder. Use seaborn for styling
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.set_style("whitegrid")
# sns.factorplot(x='trade_balance_millions', y='partner_code', data=rwa_top10.to_pandas(), palette='Blues_d', kind='bar')
# plt.title('Top 10 Partners for Rwanda')
# plt.xlabel('Trade Balance In Millions of USD')
# plt.ylabel('')
# plt.savefig('../output/top10partners_rwa.png', dpi=300, bbox_inches='tight')
