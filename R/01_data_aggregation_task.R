repo_ <- "eactrade"
source(paste0(repo_, "/R/manifest.R"))

DZA	AFRINIC
ANGOLA	AO	AGO	AFRINIC
BENIN	BJ	BEN	AFRINIC
BOTSWANA	BW	BWA	AFRINIC
BURKINA FASO	BF	BFA	AFRINIC
BURUNDI	BI	BDI	AFRINIC
CAMEROON	CM	CMR	AFRINIC
CAPE VERDE	CV	CPV	AFRINIC
CENTRAL AFRICAN REPUBLIC	CF	CAF	AFRINIC
CHAD	TD	TCD	AFRINIC
COMOROS	KM	COM	AFRINIC
CONGO	CG	COG	AFRINIC
CONGO, THE DEMOCRATIC REPUBLIC OF THE	CD	COD	AFRINIC
COTE D’IVOIRE	CI	CIV	AFRINIC
DJIBOUTI	DJ	DJI	AFRINIC
EGYPT	EG	EGY	AFRINIC
EQUATORIAL GUINEA	GQ	GNQ	AFRINIC
ERITREA	ER	ERI	AFRINIC
ETHIOPIA	ET	ETH	AFRINIC
GABON	GA	GAB	AFRINIC
GAMBIA	GM	GMB	AFRINIC
GHANA	GH	GHA	AFRINIC
GUINEA	GN	GIN	AFRINIC
GUINEA-BISSAU	GW	GNB	AFRINIC
KENYA	KE	KEN	AFRINIC
LESOTHO	LS	LSO	AFRINIC
LIBERIA	LR	LBR	AFRINIC
LIBYAN ARAB JAMAHIRIYA	LY	LBY	AFRINIC
MADAGASCAR	MG	MDG	AFRINIC
MALI	ML	MLI	AFRINIC
MALAWI	MW	MWI	AFRINIC
MAURITANIA	MR	MRT	AFRINIC
MAURITIUS	MU	MUS	AFRINIC
MAYOTTE	YT	MYT	AFRINIC
MOROCCO	MA	MAR	AFRINIC
MOZAMBIQUE	MZ	MOZ	AFRINIC
NAMIBIA	NA	NAM	AFRINIC
NIGER	NE	NER	AFRINIC
NIGERIA	NG	NGA	AFRINIC
REUNION ISLAND	RE	REU	AFRINIC
RWANDA	RW	RWA	AFRINIC
SAO TOME AND PRINCIPE	ST	STP	AFRINIC
SENEGAL	SN	SEN	AFRINIC
SEYCHELLES	SC	SYC	AFRINIC
SIERRA LEONE	SL	SLE	AFRINIC
SOMALIA	SO	SOM	AFRINIC
SOUTH AFRICA	ZA		AFRINIC



c()
		


country_ids <- 
  read_csv("eactrade/data/countries_codes_and_coordinates.csv") %>%
  janitor::clean_names() %>%
  select(alpha_3_code, numeric_code) %>%
  #filter(alpha_3_code %in% c("RWA","UGA","TZA","BDI", "COD", "KEN","ZMB", "ZWE", "UGA", "TUN", "TGO", "SDN", "SWZ", "SSD", "ZAF"))  %>%
  mutate(numeric_code = as.character(numeric_code))

#Combine trade data from 2015 to 2019
trade_data_all_years <-
 list.files(paste0("dataverse_files"), recursive = TRUE) %>%
 as_tibble() %>%
 filter(grepl(pattern = "partner_sitcproduct4digit", x = value)) %>%
 pull(value)

allcountries_trade_df <-
 trade_data_all_years %>%
 map(~data.table::fread(file = paste0("dataverse_files/",.x)) %>%
       janitor::clean_names() %>% as_tibble() %>%
       mutate_all(as.character)
     ) %>%
 bind_rows() %>% as_tibble() 


eaccountries_trade_df <- 
  allcountries_trade_df %>%
  inner_join(country_ids, by = c("location_id" = "numeric_code")) %>%
  rename(to = alpha_3_code) %>%
  inner_join(country_ids, by = c("partner_id" = "numeric_code")) %>%
  rename(from = alpha_3_code)  %>%
  select(-location_id, -partner_id, -sitc_eci, -sitc_coi ) %>%
  select(from, to, everything())

saveRDS(object = eaccountries_trade_df, "eactrade/data/processed/eac_trade_df_2015_2019.rds")