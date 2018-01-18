#This .awk script was used to parse the massive city JSON database to retrieve a python dictionary of each city name 
#and its corresponding city ID number so that it could be used with the API.

#!/usr/bin/awk -f
BEGIN {
	print "{"
}

/"id":/ {
    # Get the ID without the trailing comma
    id = substr($2, 1, length($2) - 1)
}

/"name":/ {
    # Get the name without the quotes or trailing comma
    match($0, /"name": "[^"]+",/)
    name = substr($0, RSTART + 9, RLENGTH - 9 - 2)

    # Escape any single-quotes
    gsub(/'/, "\\'", name)

    print "    '" name "' : " id ","
}

END {
	print "}"
}
