import pyarrow.parquet as pq
import polars as pl
import pandas as pd
import squarify
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the data
product_labs = pd.read_csv('../data/processed/SITCCodeandDescription.csv')
trade_data_all_years = pq.ParquetDataset('../data/processed/country_partner_sitcproduct4digit_year_all.parquet').read_pandas().to_pandas()
# Import the population data
pop_data = pd.read_csv('../data/processed/API_SP_POP_TOTL_DS2.csv', skiprows=4)

# Convert numeric columns to numeric data type
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

all_countries_df = labelled_df[['year','parent_code','location_code', 'partner_code', 'description', 'trade_balance_millions', 'trade_balance', 'pop_2020', 'trade_bal_by_population']].drop_duplicates()

# Filter all_countries_df by location_code using the following locations 
all_countries = ["REU", "RWA", "STP",	"SEN", 	"SYC", 	"SLE",
                 "SOM","ZAF", "SSD", "SDN", "SWZ", "TZA", "NGA", "NER",
                 "TGO", "TUN",	"UGA", "ESH",	"ZMB", "ZWE",
                 "LSO",	"LBR",	"LBY", "MDG", "MLI",	"MWI",	"MRT",	"MUS",	
                 "MYT",	"MAR",	"MOZ","NAM", "DZA", "AGO", "BEN", "BWA", "BFA",
            	"BDI", "CMR", "CPV","CAF",	"TCD", "COM", "COG", "COD", "CIV", 
                "DJI",	"EGY","GNQ", "ERI",	"ETH", "GAB", "GMB", "GHA", "GIN", "GNB", "KEN"]
# Write the code
all_countries_df = all_countries_df[all_countries_df['location_code'].isin(all_countries)]

all_africa_df = all_countries_df.sort_values(by='trade_bal_by_population', ascending=False)
# convert to polars dataframe
top10 = pl.from_pandas(all_africa_df)

all_countries_df_agg = (
    top10
    .groupby(['location_code'])
    .agg(
        pl.col('trade_bal_by_population').mean().alias('avg_trade_bal_per_capita')
    )
    # Sort polars dataframe in descending ordert by avg_trade_bal_per_capita    
    )
print(all_countries_df_agg.tail(20))


# Convert polars table to png and save to output 
# Write the code
fig, ax = plt.subplots(figsize=(6, 4))
sns.set_style("whitegrid")
sns.factorplot(x='avg_trade_bal_per_capita', y='location_code', data=all_countries_df_agg.to_pandas(), kind='bar')
plt.title('Trade balance per capita $')
plt.xlabel('USD')
plt.ylabel('')
plt.savefig('../output/trade_bal_by_population_allafrica.png', dpi=200, bbox_inches='tight')


# Convert polars table to png and save to output 
# Write the code
# fig, ax = plt.subplots(figsize=(5, 3))
# sns.set_style("whitegrid")
# sns.factorplot(x='avg_trade_bal_per_capita', y='location_code', data=all_countries_df_agg.to_pandas(), kind='bar')
# plt.title('Trade balance per capita in USD')
# plt.xlabel('USD')
# plt.ylabel('Country')
# plt.show()
#plt.savefig('../output/avg_trade_bal_per_capita_sadec.png', dpi=300, bbox_inches='tight')
