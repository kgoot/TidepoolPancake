# Tidepool Pancake

This application integrates OpenMHealth's open source [Shimmer](https://github.com/openmhealth/shimmer) application, conneting it to Tidepool's note platfrom. 
After settings up and running the [Shimmer](https://github.com/openmhealth/shimmer) application, a json file with either normalized or raw data from a third party API can be generated. For instructions for obtaining the desired json file from any supoprted third party API, follow Shimmer's README file. 

Once a json file is generated, Tidepool Pancake adds the data from the third party API into the Tidepool platfrom by setting up login credentials and adding a note for each event registered in the json file.

After running the application, new notes are generated under the specified user in [https://devel-clamshell.tidepool.io/](https://devel-clamshell.tidepool.io/).

# Requirements 
 
 Tidepool Pankake runs with python3 and requires the requests library which can be found [here](http://www.python-requests.org/en/latest/). 
