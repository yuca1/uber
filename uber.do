* fhv_tripdata_hourly

* filenames
#delimit;

local fnames "
fhv_tripdata_2015-12.csv
fhv_tripdata_2016-01.csv
fhv_tripdata_2016-12.csv
";

#delimit cr;

* set data name
local dta_name "fhv_tripdata_hourly.dta"

import delimited "fhv_tripdata_2015-01.csv", encoding(ISO-8859-1)

gen pickup_time = regexs(1) if regexm(pickup_date, "(^.*)[:][0-9]*[:]")
gen num = 1
collapse  (count) count=num, by(dispatching_base_num pickup_time locationid)

save "`dta_name'", replace
clear 


foreach var of local fnames {
	import delimited "`var'", encoding(ISO-8859-1)
	
	gen pickup_time = regexs(1) if regexm(pickup_date, "(^.*)[:][0-9]*[:]")
	gen num = 1
	collapse  (count) count=num, by(dispatching_base_num pickup_time locationid)
	
    append using "`dta_name'"
    save "`dta_name'", replace
    clear    
}

