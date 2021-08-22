# ExcelSummationApp
1. CLone project
2. create virtualenv and install requirements.txt [pip install -r requirements.txt]
3. create settings_local.py in same directory as settings.py and paste here content of settings_local.example.
4. create and connect database in settings local (I used POSTGRESQL)
5. run project
6. url to POST api request  is {domain}/upload_file/ and url to GET request is {domain}//get_file/{pk}/
## Example of POST request:
(I used POSTMAN to test requests)
![POST](https://user-images.githubusercontent.com/47391224/130364443-c956ea56-d1e0-4059-aeb9-c9b73e7eecc3.png)
1. file fields contain uploaded excel file
2. fields field contain name of column for which we want to count summary and average
3. nrows field contain information about how many rows of table we want to count
4. header_row fields contain information about row index in excel where targeted excel table header is placed.
## Example of GET request:
![GET](https://user-images.githubusercontent.com/47391224/130364582-c27efd1c-be4a-4764-9c25-64a7318c26d2.png)
