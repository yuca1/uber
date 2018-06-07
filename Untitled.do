import delimited "FHV_Base_Aggregate_Report.csv", encoding(ISO-8859-1)

duplicates drop baselicensenumber, force
drop wavenumber basename weeknumber pickupstartdate pickupenddate totaldispatchedtrips uniquedispatchedvehicle

*drop if years != 2015
drop years

rename baselicensenumber dispatching_base_num

save "fhv_base_aggregate_2015.dta", replace
