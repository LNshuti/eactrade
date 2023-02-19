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

### SADEC 
bwa_df = top10_products(labelled_df, 'BWA')
moz_df = top10_products(labelled_df, 'MOZ')
zmb_df = top10_products(labelled_df, 'ZMB')
ago_df = top10_products(labelled_df, 'AGO')
mwi_df = top10_products(labelled_df, 'MWI')
lso_df = top10_products(labelled_df, 'LSO')
swz_df = top10_products(labelled_df, 'SWZ')
nam_df = top10_products(labelled_df, 'NAM')

### ECOWAS 
gha_df = top10_products(labelled_df, 'GHA')
nga_df = top10_products(labelled_df, 'NGA')
sen_df = top10_products(labelled_df, 'SEN')
bfa_df = top10_products(labelled_df, 'BFA')
ben_df = top10_products(labelled_df, 'BEN')
gmb_df = top10_products(labelled_df, 'GMB')
tgo_df = top10_products(labelled_df, 'TGO')
civ_df = top10_products(labelled_df, 'CIV')
gnb_df = top10_products(labelled_df, 'GNB')
lbr_df = top10_products(labelled_df, 'LBR')

### ASEAN 
vnm_df = top10_products(labelled_df, 'VNM')
sgp_df = top10_products(labelled_df, 'SGP')
tha_df = top10_products(labelled_df, 'THA')
phl_df = top10_products(labelled_df, 'PHL')
mys_df = top10_products(labelled_df, 'MYS')
idn_df = top10_products(labelled_df, 'IDN')
khm_df = top10_products(labelled_df, 'KHM')

### OPEC 
#### Algeria, Angola, Congo, Equatorial Guinea, Gabon, Iran, Iraq, Kuwait, Libya, Nigeria, Qatar, Saudi Arabia, 
#### United Arab Emirates, Venezuela, and Yemen
dza_df = top10_products(labelled_df, 'DZA')
ago_df = top10_products(labelled_df, 'AGO')
cog_df = top10_products(labelled_df, 'COG')
gnq_df = top10_products(labelled_df, 'GNQ')
gab_df = top10_products(labelled_df, 'GAB')
irn_df = top10_products(labelled_df, 'IRN')
irq_df = top10_products(labelled_df, 'IRQ')
kwt_df = top10_products(labelled_df, 'KWT')
lby_df = top10_products(labelled_df, 'LBY')
nga_df = top10_products(labelled_df, 'NGA')
qat_df = top10_products(labelled_df, 'QAT')
sau_df = top10_products(labelled_df, 'SAU')
are_df = top10_products(labelled_df, 'ARE')
ven_df = top10_products(labelled_df, 'VEN')
yem_df = top10_products(labelled_df, 'YEM')

### EU 

### BRICS

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

plot_top10_partners(bwa_df, 'BWA')
plot_top10_partners(moz_df, 'MOZ')
plot_top10_partners(zmb_df, 'ZMB')
plot_top10_partners(ago_df, 'AGO')
plot_top10_partners(mwi_df, 'MWI')
plot_top10_partners(lso_df, 'LSO')
plot_top10_partners(swz_df, 'SWZ')
plot_top10_partners(nam_df, 'NAM')

plot_top10_partners(gha_df, 'GHA')
plot_top10_partners(nga_df, 'NGA')
plot_top10_partners(sen_df, 'SEN')
plot_top10_partners(bfa_df, 'BFA')
plot_top10_partners(ben_df, 'BEN')
plot_top10_partners(gmb_df, 'GMB')
plot_top10_partners(tgo_df, 'TGO')
plot_top10_partners(civ_df, 'CIV')
plot_top10_partners(gnb_df, 'GNB')
plot_top10_partners(lbr_df, 'LBR')

plot_top10_partners(vnm_df, 'VNM')
plot_top10_partners(sgp_df, 'SGP')
plot_top10_partners(tha_df, 'THA')
plot_top10_partners(phl_df, 'PHL')
plot_top10_partners(mys_df, 'MYS')
plot_top10_partners(idn_df, 'IDN')
plot_top10_partners(khm_df, 'KHM')

plot_top10_partners(dza_df, 'DZA')
plot_top10_partners(ago_df, 'AGO')
plot_top10_partners(cog_df, 'COG')
plot_top10_partners(gnq_df, 'GNQ')
plot_top10_partners(gab_df, 'GAB')
plot_top10_partners(irn_df, 'IRN')
plot_top10_partners(irq_df, 'IRQ')
plot_top10_partners(kwt_df, 'KWT')
plot_top10_partners(lby_df, 'LBY')
plot_top10_partners(nga_df, 'NGA')
plot_top10_partners(qat_df, 'QAT')
plot_top10_partners(sau_df, 'SAU')
plot_top10_partners(are_df, 'ARE')
plot_top10_partners(ven_df, 'VEN')
plot_top10_partners(yem_df, 'YEM')

# Combine the five datasets 
combined_df = pl.concat([rwa_df, uga_df, ken_df, bdi_df, tza_df])
#rwa_uga_df = combined_df.groupby(['location_code'])['trade_bal_by_population'].sum().reset_index()
print(combined_df)

aggregated_df = (
    combined_df
    .groupby(['location_code'])
    .agg(
        pl.col('trade_bal_by_population').mean().alias('avg_trade_bal_per_capita')
    )
)

print(aggregated_df)

sadec_df = pl.concat([bwa_df, moz_df, zmb_df, ago_df, mwi_df, tza_df, lso_df, swz_df, nam_df])
aggregated_sadecc_df = (
    sadec_df
    .groupby(['location_code'])
    .agg(
        pl.col('trade_bal_by_population').mean().alias('avg_trade_bal_per_capita')
    ) )

print(aggregated_sadecc_df)

# Convert polars table to png and save to output 
# Write the code
fig, ax = plt.subplots(figsize=(5, 3))
sns.set_style("whitegrid")
sns.factorplot(x='avg_trade_bal_per_capita', y='location_code', data=aggregated_sadecc_df.to_pandas(), kind='bar')
plt.title('Trade balance per capita in USD')
plt.xlabel('USD')
plt.ylabel('Country')
plt.savefig('../output/avg_trade_bal_per_capita_sadec.png', dpi=300, bbox_inches='tight')


ecowas_df = pl.concat([gha_df, nga_df, sen_df, bfa_df, ben_df, gmb_df, tgo_df, civ_df, gnb_df, lbr_df])
aggregated_ecowas_df = (
    ecowas_df
    .groupby(['location_code'])
    .agg(   
        pl.col('trade_bal_by_population').mean().alias('avg_trade_bal_per_capita')
    ) )

print(aggregated_ecowas_df)

asean_df = pl.concat([vnm_df, sgp_df, tha_df, phl_df, mys_df, idn_df, khm_df])
aggregated_asean_df = (
    asean_df
    .groupby(['location_code'])
    .agg(
        pl.col('trade_bal_by_population').mean().alias('avg_trade_bal_per_capita')
    ) )

print(aggregated_asean_df)
# Convert polars table to png and save to output
# Write the code
fig, ax = plt.subplots(figsize=(5, 3))
sns.set_style("whitegrid")
sns.factorplot(x='avg_trade_bal_per_capita', y='location_code', data=aggregated_asean_df.to_pandas(), kind='bar')
plt.title('Trade balance per capita in USD')
plt.xlabel('USD')
plt.ylabel('Country')
plt.savefig('../output/avg_trade_bal_per_capita_asean.png', dpi=300, bbox_inches='tight')



opec_df = pl.concat([dza_df, ago_df, cog_df, gnq_df, gab_df, irn_df, irq_df, kwt_df, lby_df, nga_df, qat_df, sau_df, are_df, ven_df, yem_df])
aggregated_opec_df = (
    opec_df
    .groupby(['location_code'])
    .agg(
        pl.col('trade_bal_by_population').mean().alias('avg_trade_bal_per_capita')
    ) )

print(aggregated_opec_df)

# Convert polars table to png and save to output 
# Write the code
fig, ax = plt.subplots(figsize=(5, 3))
sns.set_style("whitegrid")
sns.factorplot(x='avg_trade_bal_per_capita', y='location_code', data=aggregated_opec_df.to_pandas(), kind='bar')
plt.title('Trade balance per capita in USD')
plt.xlabel('USD')
plt.ylabel('Country')
plt.savefig('../output/avg_trade_bal_per_capita_opec.png', dpi=300, bbox_inches='tight')

# Plot bar plot with each subfigure representing a country code


# combined_ken_tza = pl.concat([ken_df, tza_df])
# combined_ken_tza_df = combined_ken_tza.groupby(['location_code'])['trade_bal_by_population'].sum().reset_index()

#, ken_df, bdi_df, tza_df

# Plot bar plot with each subfigure representing a country code 
# Use trade_bal_by_population as the y variable
# write the code 
# Incease the size of the figure
# Increase the overall plot size especially the height
# Plot bar plot andsave plot as png to output folder. Use seaborn for styling

# fig, ax = plt.subplots(figsize=(4, 6))
# sns.set_style("whitegrid")
# sns.catplot(x='trade_bal_by_population', y='partner_code', data=rwa_uga_df.to_pandas(), kind='bar', col='location_code')
# plt.xlabel('Trade Balance in USD/Population')
# plt.savefig('../output/top10partners_rwa_uga.png', bbox_inches='tight')


# fig, ax = plt.subplots(figsize=(4, 6))
# sns.set_style("whitegrid")
# sns.catplot(x='trade_bal_by_population', y='partner_code', data=combined_ken_tza_df.to_pandas(), kind='bar', col='location_code')
# plt.xlabel('Trade Balance in USD/Population')
# plt.savefig('../output/top10partners_ken_tza.png', bbox_inches='tight')

# Plot bar plot andsave plot as png to output folder. Use seaborn for styling
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.set_style("whitegrid")
# sns.factorplot(x='trade_balance_millions', y='partner_code', data=rwa_top10.to_pandas(), palette='Blues_d', kind='bar')
# plt.title('Top 10 Partners for Rwanda')
# plt.xlabel('Trade Balance In Millions of USD')
# plt.ylabel('')
# plt.savefig('../output/top10partners_rwa.png', dpi=300, bbox_inches='tight')
