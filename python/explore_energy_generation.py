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
aut_df = top10_products(labelled_df, 'AUT')
bel_df = top10_products(labelled_df, 'BEL')
bgr_df = top10_products(labelled_df, 'BGR')
hrv_df = top10_products(labelled_df, 'HRV')
cyp_df = top10_products(labelled_df, 'CYP')
cze_df = top10_products(labelled_df, 'CZE')
dnk_df = top10_products(labelled_df, 'DNK')
est_df = top10_products(labelled_df, 'EST')
fin_df = top10_products(labelled_df, 'FIN')
fra_df = top10_products(labelled_df, 'FRA')
deu_df = top10_products(labelled_df, 'DEU')
grc_df = top10_products(labelled_df, 'GRC')
hun_df = top10_products(labelled_df, 'HUN')
irl_df = top10_products(labelled_df, 'IRL')
ita_df = top10_products(labelled_df, 'ITA')
lva_df = top10_products(labelled_df, 'LVA')
ltu_df = top10_products(labelled_df, 'LTU')
lux_df = top10_products(labelled_df, 'LUX')
mlt_df = top10_products(labelled_df, 'MLT')
nld_df = top10_products(labelled_df, 'NLD')
pol_df = top10_products(labelled_df, 'POL')
prt_df = top10_products(labelled_df, 'PRT')
rou_df = top10_products(labelled_df, 'ROU')
svk_df = top10_products(labelled_df, 'SVK')
svn_df = top10_products(labelled_df, 'SVN')
esp_df = top10_products(labelled_df, 'ESP')
swe_df = top10_products(labelled_df, 'SWE')

### BRICS
rus_df = top10_products(labelled_df, 'RUS')
ind_df = top10_products(labelled_df, 'IND')
chn_df = top10_products(labelled_df, 'CHN')
bra_df = top10_products(labelled_df, 'BRA')
zaf_df = top10_products(labelled_df, 'ZAF')

### NATO 
aut_df = top10_products(labelled_df, 'AUT')
bel_df = top10_products(labelled_df, 'BEL')
bgr_df = top10_products(labelled_df, 'BGR')
hrv_df = top10_products(labelled_df, 'HRV')
cyp_df = top10_products(labelled_df, 'CYP')
cze_df = top10_products(labelled_df, 'CZE')
dnk_df = top10_products(labelled_df, 'DNK')
est_df = top10_products(labelled_df, 'EST')
fin_df = top10_products(labelled_df, 'FIN')
fra_df = top10_products(labelled_df, 'FRA')
deu_df = top10_products(labelled_df, 'DEU')
grc_df = top10_products(labelled_df, 'GRC')
hun_df = top10_products(labelled_df, 'HUN')
irl_df = top10_products(labelled_df, 'IRL')
ita_df = top10_products(labelled_df, 'ITA')
lva_df = top10_products(labelled_df, 'LVA')
ltu_df = top10_products(labelled_df, 'LTU')
lux_df = top10_products(labelled_df, 'LUX')
mlt_df = top10_products(labelled_df, 'MLT')
nld_df = top10_products(labelled_df, 'NLD')
pol_df = top10_products(labelled_df, 'POL')
prt_df = top10_products(labelled_df, 'PRT')
rou_df = top10_products(labelled_df, 'ROU')
svk_df = top10_products(labelled_df, 'SVK')
svn_df = top10_products(labelled_df, 'SVN')
esp_df = top10_products(labelled_df, 'ESP')
swe_df = top10_products(labelled_df, 'SWE')
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

plot_top10_partners(rus_df, 'RUS')
plot_top10_partners(ind_df, 'IND')
plot_top10_partners(chn_df, 'CHN')
plot_top10_partners(bra_df, 'BRA')
plot_top10_partners(zaf_df, 'ZAF')

plot_top10_partners(aut_df, 'AUT')
plot_top10_partners(bel_df, 'BEL')
plot_top10_partners(bgr_df, 'BGR')
#plot_top10_partners(che_df, 'CHE')
plot_top10_partners(cyp_df, 'CYP')
plot_top10_partners(cze_df, 'CZE')
plot_top10_partners(deu_df, 'DEU')
plot_top10_partners(dnk_df, 'DNK')
plot_top10_partners(esp_df, 'ESP')
plot_top10_partners(est_df, 'EST')
plot_top10_partners(fin_df, 'FIN')
plot_top10_partners(fra_df, 'FRA')
#plot_top10_partners(gbr_df, 'GBR')
plot_top10_partners(grc_df, 'GRC')
plot_top10_partners(hun_df, 'HUN')
plot_top10_partners(irl_df, 'IRL')
#plot_top10_partners(isl_df, 'ISL')
plot_top10_partners(ita_df, 'ITA')
#plot_top10_partners(jpn_df, 'JPN')
#plot_top10_partners(ltu_df, 'LTU')
plot_top10_partners(lux_df, 'LUX')
plot_top10_partners(lva_df, 'LVA')
plot_top10_partners(nld_df, 'NLD')
#plot_top10_partners(nor_df, 'NOR')
plot_top10_partners(pol_df, 'POL')
plot_top10_partners(prt_df, 'PRT')
plot_top10_partners(rou_df, 'ROU')
plot_top10_partners(svk_df, 'SVK')
plot_top10_partners(svn_df, 'SVN')
plot_top10_partners(swe_df, 'SWE')
#plot_top10_partners(tur_df, 'TUR')
#plot_top10_partners(usa_df, 'USA')




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


brics_df = pl.concat([rus_df, ind_df, chn_df, bra_df, zaf_df])
aggregated_brics_df = (
    asean_df
    .groupby(['location_code'])
    .agg(
        pl.col('trade_bal_by_population').mean().alias('avg_trade_bal_per_capita')
    ) )

print(aggregated_brics_df)
# Convert polars table to png and save to output
# Write the code
fig, ax = plt.subplots(figsize=(5, 3))
sns.set_style("whitegrid")
sns.factorplot(x='avg_trade_bal_per_capita', y='location_code', data=aggregated_brics_df.to_pandas(), kind='bar')
plt.title('Trade balance per capita in USD')
plt.xlabel('USD')
plt.ylabel('Country')
plt.savefig('../output/avg_trade_bal_per_capita_brics.png', dpi=300, bbox_inches='tight')


eu_df = pl.concat([aut_df, bel_df, bgr_df, cyp_df, cze_df, deu_df, dnk_df, est_df, fin_df, fra_df, grc_df, hun_df, irl_df, ita_df, lva_df, ltu_df, lux_df, mlt_df, nld_df, pol_df, prt_df, rou_df, svk_df, svn_df, esp_df, swe_df])
aggregated_eu_df = (
    asean_df
    .groupby(['location_code'])
    .agg(
        pl.col('trade_bal_by_population').mean().alias('avg_trade_bal_per_capita')
    ) )

print(aggregated_eu_df)
# Convert polars table to png and save to output
# Write the code
fig, ax = plt.subplots(figsize=(5, 3))
sns.set_style("whitegrid")
sns.factorplot(x='avg_trade_bal_per_capita', y='location_code', data=aggregated_eu_df.to_pandas(), kind='bar')
plt.title('Trade balance per capita in USD')
plt.xlabel('USD')
plt.ylabel('Country')
plt.savefig('../output/avg_trade_bal_per_capita_eu.png', dpi=300, bbox_inches='tight')

############################################

nato_df = pl.concat([aut_df, bel_df, bgr_df, cyp_df, cze_df, deu_df, dnk_df, est_df, fin_df, fra_df, grc_df, hun_df, irl_df, ita_df, lva_df, ltu_df, lux_df, mlt_df, nld_df, pol_df, prt_df, rou_df, svk_df, svn_df, esp_df, swe_df, dza_df, ago_df, cog_df, gnq_df, gab_df, irn_df, irq_df, kwt_df, lby_df, nga_df, qat_df, sau_df, are_df, ven_df, yem_df, rus_df, ind_df, chn_df, bra_df, zaf_df, vnm_df, sgp_df, tha_df, phl_df, mys_df, idn_df, khm_df])
aggregated_nato_df = (
    asean_df
    .groupby(['location_code'])
    .agg(
        pl.col('trade_bal_by_population').mean().alias('avg_trade_bal_per_capita')
    ) )

print(aggregated_nato_df)
# Convert polars table to png and save to output
# Write the code
fig, ax = plt.subplots(figsize=(5, 3))
sns.set_style("whitegrid")
sns.factorplot(x='avg_trade_bal_per_capita', y='location_code', data=aggregated_nato_df.to_pandas(), kind='bar')
plt.title('Trade balance per capita in USD')
plt.xlabel('USD')
plt.ylabel('Country')
plt.savefig('../output/avg_trade_bal_per_capita_nato.png', dpi=300, bbox_inches='tight')

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
