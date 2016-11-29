#!/usr/bin/env bash
#! /usr/bin/env bash

echo "Please provide the following details on your lab environment."
echo
echo "What is the address of your Mantl Control Server?  "
echo "eg: control.mantl.internet.com"
read control_address
echo
echo "What is the username for your Mantl account?  "
read mantl_user
echo
echo "What is the password for your Mantl account?  "
read -s mantl_password
echo
echo "Please provide the Marathon app name you would like to use: e.g app/prod/web"
read app_name
echo
echo "What is the Lab Application Domain?  "
read mantl_domain
echo
echo "What is the username for your Tropo account?  "
read TROPO_USER
echo
echo "What is the password for your Tropo account?  "
read -s TROPO_PASS
echo "What is the preferred area code for your service? e.g 1913 "
read TROPO_PREFIX

cp app_template.json app.json

sed -i "" -e "s!APP_NAME!$app_name!g" app.json
echo " "
echo "***************************************************"
echo "Installing gbos_tropo as $app_name"
curl -k -X POST -u $mantl_user:$mantl_password https://$control_address:8080/v2/apps \
-H "Content-type: application/json" \
-d @app.json \
| python -m json.tool

# get hostname portion from marathon app name
host=$(echo $app_name | sed -e 's/\//-/g')
TROPO_APP_URL=`echo "http://$host.$mantl_domain/api/v1"`
python setup/tropo.py -n $host -a $TROPO_APP_URL -u $TROPO_USER -p $TROPO_PASS --tropoprefix $TROPO_PREFIX
echo
echo
echo "Marathon Application Details"
echo "Wait 2-3 minutes for the service to deploy. "
echo
echo "Your application should be accessible at: "
echo
echo $TROPO_APP_URL
echo
echo "You can also watch the progress from the GUI at: "
echo
echo "https://$control_address/marathon"
echo
echo "***************************************************"

