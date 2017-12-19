#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:45:32 2017

@author: gaelberon
"""

#############################
## DATABASE TABLES AND FIELDS
## 
import db_definition as db_def

# Create new entry into table table_name without primary key
def createNewEntriesInTableNoPK( conn, table_name, fields_names_list, values_names_list ) :
    createNewEntriesInTable( conn, table_name, fields_names_list, values_names_list )

# Create new entry into table table_name
def createNewEntriesInTable( conn, table_name, fields_names_list, values_names_list ) :
    # Build the list of fields to be populated in the table
    fields = ""
    for field_name in fields_names_list :
        if fields == "" :
            fields = field_name
        else :
            fields = fields + ", " + field_name
    # Build the list of values to be populated in the table
    values = ""
    for value_name in values_names_list :
        if values == "" :
            values = "'" + value_name + "'"
        else :
            values = values + ", " + "'" + value_name + "'"
    # Build the sql statement for inserting values in the table
    stmt = "INSERT INTO {0} ({1}) \
                     VALUES ({2});".format(table_name,
                                             fields,
                                             values)
    # Initiate the cursor on the connection
    cur = conn.cursor()
    # Execute the sql statement
    cur.execute( stmt )
    # Execute the commit
    cur.execute( "COMMIT;")

# Select values of 'fields_names_list' from 'table_name'
def selectFromTable( conn, fields_names_list, table_name ) :
    cur = conn.cursor()

    # Build the list of fields to be populated in the table
    fields = ""
    for field_name in fields_names_list :
        if fields == "" :
            fields = field_name
        else :
            fields = fields + ", " + field_name
    
    # Build the sql statement for inserting values in the table
    stmt = "SELECT {0} FROM {1}".format(fields, table_name)
    
    cur.execute( stmt )

    for field1, field2 in cur.fetchall() :
        print(field1, field2)

# Select values of 'fields_names_list' from 'table_name'
def selectFromTableWithClauses( conn, fields_names_list, table_name,
                                where_fields_names_list,
                                where_fields_values_list) :
    cur = conn.cursor()

    # Build the list of fields to be populated in the table
    fields = ""
    for field_name in fields_names_list :
        if fields == "" :
            fields = field_name
        else :
            fields = fields + ", " + field_name
            
    where_fields = ""
    for where_field_idx, where_field_name in enumerate(where_fields_names_list):
#    for  in len(where_fields_names_list) :
        print("Index dans la table: " + table_name + ", is: " + str(where_field_idx))
#        where_field_name = where_fields_names_list[where_field_idx]
        where_field_value = where_fields_values_list[where_field_idx]
        if where_fields == "" :
            where_fields = where_field_name + " = '" + where_field_value + "'"
        else :
            where_fields = where_fields + " and " + \
                           where_field_name + " = '" + where_field_value + "'"
    
    where_fields = " where " + where_fields
    # Build the sql statement for inserting values in the table
    stmt = "SELECT {0} FROM {1}".format(fields, table_name)
    stmt = stmt + where_fields
    
    print(stmt)
    
    cur.execute( stmt )

#    for field1, field2 in cur.fetchall() :
#        print(field1, field2)
    return(cur.fetchall())

#print("Using MySQLdb…")
#import MySQLdb
#myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
#doQuery( myConnection )
#myConnection.close()

#print("Using pymysql…")
#import pymysql
#myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
#createNewEntriesInTableNoPK( myConnection, table_geo_area_type_name, [field_geo_a_t_name], ['DA NANG'] )

#selectFromTable( myConnection, [field_geo_a_t_id, field_geo_a_t_name], table_geo_area_type_name )

#myConnection.close()

#print("Using mysql.connector…")
#import mysql.connector
#myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
#doQuery( myConnection )
#myConnection.close()
