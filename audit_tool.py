#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-

import arcpy
import pandas as pd


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "CSV Auditor Toolbox"
        self.alias = "CSVAt"

        # List of tool classes associated with this toolbox
        self.tools = [Duplicate]


class Duplicate(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Duplicate Removal"
        self.description = "Creates two new csv files. One with only the duplicates from the input table and one with the duplicates removed."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        
        #first paramater which is the table to be audited
        param0= arcpy.Parameter(
            displayName = 'Table to be audited',
            name = 'input_file',
            datatype = 'DEFile',
            parameterType = 'Required',
            direction = 'Input')
        #create a filter to force the file to be a csv
            param0.filter.list = ['csv']
            
        #second parameter where the duplicate file will be stored
        param1= arcpy.Parameter(
            displayName = 'Duplicate File',
            name = 'duplicate_file',
            datatype = 'DEFile',
            parameterType = 'Required',
            direction = 'Output')
        #create a filter that the output file must also be a csv
            param1.filter.list = ['csv']
        
        #third parameter where the file containing no duplicates will be stored
        param2= arcpy.Parameter(
            displayName = 'Output File',
            name = 'output_file',
            datatype = 'DEFile',
            parameterType = 'Required',
            direction = 'Output')
        #create a filter that the output file must also be a csv
            param1.filter.list = ['csv']
            
        #fourth parameter field name of interest
        param3 = arcpy.Parameter(
            displayName = 'Field to Find Duplicates',
            name = 'field',
            datatype = 'Field',
            parameterType = 'Required',
            direction = 'Input')
        
        params = [param0, param1, param2, param3, param4]        
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        
        #get parameters
        
        input_file = parameters[0].valueAsText
        duplicate_file = parameters[1].valueAsText
        output_file = parameters[2].valueAsText
        field = parameters[3].valueAsText
        
        
        #this reads the csv as a dataframe
        old_df = pd.read_csv(input_file)
        
        dup_idx = old_df.duplicated(field)
        
        dups = old_df[dup_idx]

        #this writes those duplicates to a csv file determined above
        dups.to_csv(duplicate_file)

        #this creates the new file while dropping every duplicate except for the first time that
        #the duplicate occurs
        
        newdf = old_df[~dup_idx]
        
        #this writes the new dif to a csv with no duplicates
        no_dup = newdf.to_csv(output_file, index=False) 
        
        messages.addMessage('Audit Complete')
        
        return

