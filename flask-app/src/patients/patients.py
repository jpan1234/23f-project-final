from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


patients = Blueprint('patients', __name__)

# Get all the prescriptions from the database 
@patients.route('/prescriptions/<patientid>}', methods=['GET'])
def get_prescriptions(patientid):
    '''
    Get all prescriptions from the database

    columns: medication, pharmacy, dateprescribed for the patient
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT medication, pharmacy, dateprescribed FROM HuskyHealth.Prescriptions\
                    WHERE patientID = {patientid};')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get all the prescriptions from the database 
@patients.route('/notifications/<patientid>}', methods=['GET'])
def get_prescriptions(patientid):
    '''
    Get all notifications from the database for the patient

    columns: content for the patient
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT content FROM HuskyHealth.Notifications\
                    WHERE patientID = {patientid};')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


