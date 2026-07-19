#!/bin/bash

<< disclaimer
This is just for infotainment purpose
disclaimer


# THis is func definition
function is_loyal() {
read -p "$1 ne mud ke kise dekha: " bandi
read -p "$1 ka pyar % " pyaar
if [[ $bandi == "daya bhabhi"  ]];
then
	echo "$1 is loyal"
elif [[ $pyaar -ge 100 ]];
then
	echo "$1 is loyal"
else
	echo "$1 is not loyal"
fi
}

# This is func call
is_loyal "tom"
