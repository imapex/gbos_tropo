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
echo "Please provide the app name you would like to use: e.g app/prod/web"
read app_name
echo
echo "What is the Lab Application Domain?  "
read mantl_domain
echo
cp app_template.json app.json

sed -i "" -e "s!APP_NAME!$app_name!g" app.json
echo " "
echo "***************************************************"
echo "Installing gbos_kiosk as $app_name"
curl -k -X POST -u $mantl_user:$mantl_password https://$control_address:8080/v2/apps \
-H "Content-type: application/json" \
-d @app.json \
| python -m json.tool

# get hostname portion from marathon app name
reversed=$(echo $app_name | awk -F"/" '{s=$NF;for(i=NF-1;i>=1;i--)s=s FS $i;print s}')
host=$(echo $reversed | sed -e 's/\//-/g')

echo "***************************************************"
echo

echo Installed

echo "Wait 2-3 minutes for the service to deploy. "
echo
echo "Your application should be accessible at: "
echo
echo "http://$host.$mantl_domain/"
echo
echo "You can also watch the progress from the GUI at: "
echo
echo "https://$control_address/marathon"
echo