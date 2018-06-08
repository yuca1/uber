// fhv_tripdata_hourly_2016


// filenames_2016
#delimit;
local fnames "
fhv_tripdata_2016-02.csv
fhv_tripdata_2016-03.csv
fhv_tripdata_2016-04.csv
fhv_tripdata_2016-05.csv
fhv_tripdata_2016-06.csv
fhv_tripdata_2016-07.csv
fhv_tripdata_2016-08.csv
fhv_tripdata_2016-09.csv
fhv_tripdata_2016-10.csv
fhv_tripdata_2016-11.csv
fhv_tripdata_2016-12.csv
";
#delimit cr;


// set data name
local dta_name "fhv_tripdata_hourly_2016.dta"


// initial dta file
import delimited "fhv_tripdata_2016-01.csv", encoding(ISO-8859-1)

gen pickup_time = regexs(1) if regexm(pickup_date, "(^.*)[:][0-9]*[:]")
gen num = 1
collapse  (count) count=num, by(dispatching_base_num pickup_time locationid)

save "`dta_name'", replace
clear 


// for loop 
foreach var of local fnames {
	import delimited "`var'", encoding(ISO-8859-1)
	
	gen pickup_time = regexs(1) if regexm(pickup_date, "(^.*)[:][0-9]*[:]")
	gen num = 1
	collapse  (count) count=num, by(dispatching_base_num pickup_time locationid)
	
    append using "`dta_name'"
    save "`dta_name'", replace
    clear    
}


// cleaning up fhv base aggregate
import delimited "FHV_Base_Aggregate_Report.csv", encoding(ISO-8859-1)

duplicates drop baselicensenumber, force
drop wavenumber basename weeknumber pickupstartdate pickupenddate totaldispatchedtrips uniquedispatchedvehicle

*drop if years != 2016
drop years

rename baselicensenumber dispatching_base_num

save "fhv_base_aggregate_2016.dta", replace
clear


// merge
use "fhv_tripdata_hourly_2016.dta"
merge m:1 dispatching_base_num using fhv_base_aggregate_2016.dta

save "fhv_tripdata_hourly_2016_merged.dta", replace
