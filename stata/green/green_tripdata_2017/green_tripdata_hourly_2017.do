// green_tripdata_hourly_2017


// filenames_2017
#delimit;
local fnames "
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-02.csv 
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-03.csv 
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-04.csv 
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-05.csv 
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-06.csv 
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-07.csv 
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-08.csv 
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-09.csv 
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-10.csv 
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-11.csv 
https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-12.csv 
";
#delimit cr;


// set data name
local dta_name "green_tripdata_hourly_2017.dta"


// initial dta file
import delimited "https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-01.csv"

gen pickup_time = regexs(1) if regexm(lpep_pickup_datetime, "(^.*)[:][0-9]*[:]")
gen num = 1
collapse  (count) count=num, by(vendorid pickup_time pulocationid)

save "`dta_name'", replace
clear 


// for loop 
foreach var of local fnames {
	import delimited "`var'"
	
	gen pickup_time = regexs(1) if regexm(lpep_pickup_datetime, "(^.*)[:][0-9]*[:]")
	gen num = 1
	collapse  (count) count=num, by(vendorid pickup_time pulocationid)
	
    append using "`dta_name'"
    save "`dta_name'", replace
    clear    
}


/*
// cleaning up fhv base aggregate
import delimited "FHV_Base_Aggregate_Report.csv", encoding(ISO-8859-1)

duplicates drop baselicensenumber, force
drop wavenumber basename weeknumber pickupstartdate pickupenddate totaldispatchedtrips uniquedispatchedvehicle

*drop if years != 2017
drop years

rename baselicensenumber dispatching_base_num

save "fhv_base_aggregate_2017.dta", replace
clear


// merge
use "fhv_tripdata_hourly_2017.dta"
merge m:1 dispatching_base_num using fhv_base_aggregate_2017.dta

save "fhv_tripdata_hourly_2017_merged.dta", replace
*/
