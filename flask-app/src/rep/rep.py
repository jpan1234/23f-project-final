from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


rep = Blueprint('rep', __name__)

# Get information on patient-specific insurance plan
@rep.route('/rep/insuranceplans/<repID>/<patientID>', methods=['GET'])
def get_patient_insurance_plan(repID, patientID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT Patient.firstName, Patient.lastName,\
                    InsurancePlan.description,\
                    FROM Patient JOIN ')

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

# add an insurance plan for a specfic patient
@rep.route('/rep/insuranceplans/<repID>/<patientID>', methods=['POST'])
def add_patient_insurance_plan (repID, patientID):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    terminationDate = the_data['terminationDate']
    copay = the_data['copay']
    description = the_data['description']

    # Constructing the query
    query = f'''something'''
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# updates this patient's current insurance plan
@rep.route('/rep/insuranceplans/<repID>/<patientID>', methods=['PUT'])
def update_patient_insurance_plan(repID, patientID):
    
    # collecting data from request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting variable data 
    terminationDate = the_data['terminationDate']
    copay = the_data['copay']
    description = the_data['description']
    
    # create update query
    the_query = f'''something'''
    current_app.logger.info(the_query)
    
    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "Success!"

# inactive this patient's insurance plan
@rep.route('/rep/insuranceplans/<repID>/<patientID>', methods=['DELETE'])
def inactivate_patient_insurance_plan(repID, patientID):

    # Constructing the query
    query = f'''something'''
    current_app.logger.info(query)

    # executing and committing the update statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Provide a list of all insurance plans 
@rep.route('/rep/insuranceplans', methods=['GET'])
def get_all_insurance_plans(repID, patientID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    query = f'''something'''
    cursor.execute(query)

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

# Provide all health records for this patient 
@rep.route('/rep/healthrecords/<repID>/<patientID>', methods=['GET'])
def get_patient_health_records(repID, patientID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    query = f'''something'''
    cursor.execute(query)

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

# Provide all billing records for this patient 
@rep.route('/rep/billingrecords/<repID>/<patientID>', methods=['GET'])
def get_patient_billing_records(repID, patientID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    query = f'''something'''
    cursor.execute(query)

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