# CSV Database Auditor

A tool that runs throughs a csv file, finds duplicates, writes all duplicates (except the first occurance) to a new csv file and rewrites all none duplicates to a seperate csv file. The duplicates are filtered by a field of your choosing. 

## Installation
You can pull the repository and run the CSV Auditor Toolbox in ArcGIS Pro 10.1 `CSV_Auditor.Duplicate.pyt.xml`

## Usage
The CSV Auditor can be opened by creating a folder connection to the pulled repository on your personal computer.

[Creating a Folder connection and viewing Dupliate Removal Tool](https://github.com/catschooley/CSV-Database-Auditor/blob/master/Screenshots/Pictures_2.png)

Double-click the tool script 'Duplicate Removal' or right-click and choose 'open' to use the tool. 

[Tool Interface](https://github.com/catschooley/CSV-Database-Auditor/blob/master/Screenshots/Pictures_1.png)

The tool will only except csv files, most excel files can be easily converted to or saved as a csv file. For the input choose an existing csv file that you want to remove duplicates from, then create two new csv filenames with folder paths. For the field name choose a single field name from the original csv file. Make sure to type it matching spelling and capitilization. 

### Room for Improvement
* Expand beyond csv files
* Allow for multiple fields of interest
* Create dropdown selection for field(s) of interest


