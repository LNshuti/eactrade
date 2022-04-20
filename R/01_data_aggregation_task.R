repo_ <- "eactrade"
source(paste0(repo_, "/R/manifest.R"))


#select products of interest(sitc_product_code == "transportation")
product2digit <-
 read_csv(paste0(repo_, "/data/dataverse_files/country_sitcproduct2digit_year.csv"))

#Import country identifiers
countryweb <-
 "https://pkgstore.datahub.io/JohnSnowLabs/country-and-continent-codes-list/country-and-continent-codes-list-csv_csv/data/b7876b7f496677669644f3d1069d3121/country-and-continent-codes-list-csv_csv.csv"

#Get EAC country codes
country_codes <-
 read.csv(countryweb) %>%
 janitor::clean_names() %>%
 select(continent_code,
        country_code = three_letter_country_code) %>%
 filter(country_code %in% c("RWA","UGA","TZA","BDI", "COD", "KEN")) %>%
 rename(continent_name =continent_code)

#Combine trade data from 2015 to 2019
trade_data_all_years <-
 list.files(paste0(repo_, "/data/dataverse_files"), recursive = TRUE) %>%
 as_tibble() %>%
 filter(grepl(pattern = "partner_sitcproduct4digit", x = value)) %>%
 pull(value)

eac_trade_df <-
 trade_data_all_years %>%
 map(~data.table::fread(file = paste0(repo_, "/data/dataverse_files/",.x)) %>%
       janitor::clean_names() %>% as_tibble() %>%
       mutate_all(as.character) %>%
       filter(location_code %in% c("RWA","UGA","TZA","BDI", "COD", "KEN"))
     ) %>%
 bind_rows() %>% as_tibble() 

saveRDS(object = eac_trade_df, "eactrade/data/processed/eac_trade_df_2015_2019.rds")