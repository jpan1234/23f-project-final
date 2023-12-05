from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


rep = Blueprint('rep', __name__)

# Get information on patient-specific insurance plan
@rep.route('/insuranceplans/<patientID>', methods=['GET'])
def get_patient_insurance_plan(patientID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT Patient.firstName, Patient.lastName,\
                    InsurancePlan.description,\
                    FROM Patient\
                    JOIN BillingRecord\
                    ON Patient.patientID = BillingRecord.patientID\
                    JOIN InsurnacePlan\
                    ON BillingRecord.planID = InsurancePlan.planID\
                    WHERE Patient.patientID = {patientID};')

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


# Provide a list of all insurance plans 
@rep.route('/insuranceplans', methods=['GET'])
def get_all_insurance_plans(repID, patientID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    query = f'''SELECT DISTINCT description FROM InsurancePlan\
                WHERE inactive = 0'''
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
@rep.route('/healthrecords/<patientID>', methods=['GET'])
def get_patient_health_records(patientID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of healthrecords if the given rep has consent
    query = f'SELECT * FROM HealthRecords\
                JOIN InsuranceRepresentative
                ON HealthRecords.repID = InsuranceRepresentative.repID
                WHERE HealthRecords.patientID = {patientID}\
                AND InsuranceRepresentative.consent = 1'
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
@rep.route('/billingrecords/<patientID>', methods=['GET'])
def get_patient_billing_records(patientID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    query = f'''SELECT description, amount, paid FROM BillingRecord\
                WHERE patientID = {patientID}'''
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

@rep.route('/messages/<patientid>', methods=['GET'])
def get_message_patient(patientid):
    '''
    Get all messages for a particular patient

    columns: subject, content, dateSent for the patient
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT subject, content, dateSent FROM Message\
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

@rep.route('/messages/<doctorid>', methods=['GET'])
def get_message_doctor(doctorid):
    '''
    Get all messages for a particular doctor

    columns: subject, content, dateSent for the patient
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT subject, content, dateSent FROM Message\
                     WHERE doctorID = {doctorid};')

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




# POST ROUTES

# add new plan



# add an insurance plan for a specfic patient
@rep.route('/insuranceplans/>', methods=['POST'])
def add_patient_insurance_plan():

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    terminationDate = the_data['description']
    copay = the_data['amount']
    description = the_data['repID']
    repID = the_data['repID']
    inactive = 0

    ## Constructing the query
    query = 'INSERT INTO InsurancePlan (terminationDate, copay, description, repID, inactive) VALUES ("'
    query += terminationDate + '", "'
    query += copay + '", "'
    query += description + '", '
    query += repID + '", '
    query += inactive + '", '
    query += ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


# add an insurance plan for a specfic patient
@rep.route('/insuranceplans/<patientID>', methods=['POST'])
def add_patient_billing_record (patientID):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    description = the_data['description']
    amount = the_data['amount']
    repID = the_data['repID']
    planID = the_data['planID']
    paid = 0

    ## Constructing the query
    query = 'INSERT INTO BillingRecord (description, amount, patientID, repID, planID, paid) VALUES ("'
    query += description + '", "'
    query += amount + '", "'
    query += patientID + '", '
    query += repID + '", '
    query += planID + '", '
    query += paid + '", '
    query += ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


# post a message to a doctor
@rep.route('/messages/<patientid>', methods=['POST'])
def post_patient_message(patientid):
    '''
    Post a message to the database from a rep to a patient

    columns: 
    '''
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    subject = the_data['subject']
    content = the_data['content']
    repid = the_data['repID']


    # Constructing the query
    query = 'INSERT INTO Message (subject, content, patientID, repID) VALUES ("'
    query += subject + '", "'
    query += content + '", "'
    query += patientid + '", '
    query += repid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Message sent!'

# post a message to a doctor
@rep.route('/messages/<doctorid>', methods=['POST'])
def post_doctor_message(doctorid):
    '''
    Post a message to the database from a patient to a coach

    columns: subject, content, patientid, coachid
    '''
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    subject = the_data['subject']
    content = the_data['content']
    repid = the_data['repID']


    # Constructing the query
    query = 'INSERT INTO Message (subject, content, doctorID, repID) VALUES ("'
    query += subject + '", "'
    query += content + '", "'
    query += doctorid + '", '
    query += repid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Message sent!'







# PUT METHODS




# updates a patient's current insurance plan
@rep.route('/rep/insuranceplans/<planID>', methods=['PUT'])
def update_patient_insurance_plan(planID):
    
    # collecting data from request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting variable data 
    terminationDate = the_data['terminationDate']
    copay = the_data['copay']
    description = the_data['description']
    inactive = the_data['inactive'] # have the choice to set something as inactive
    repid = the_data['repID']
        
    # create update query
    the_query = f'''UPDATE InsurancePlan\
                    SET terminationDate = {terminationDate}, copay = {copay}, description = {description},\
                        inactive = {inactive}, repID = {repid}\
                    WHERE planID = {planID}'''
    current_app.logger.info(the_query)
    
    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "Success!"

# set billing record as paid
@rep.route('/billingrecord/<patientid>', methods=['PUT'])
def pay_bill(patientID):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    paid = the_data['paid'] # either 1 or 0, mostly going to set to 1 to set as "complete"
    billingrecordID = the_data['billingRecordID']

    # Constructing the query
    query = f'UPDATE BillingRecord\
                     SET paid = {paid}\
                     WHERE billingRecordID = {billingrecordID}\
                     AND patientID = {patientID};'
    
    current_app.logger.info(query)

    # executing and committing the update statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


# update a message to a doctor
@rep.route('/messages/<comid>', methods=['PUT'])
def update_message(comid):
    '''
    Update a message 

    columns: 
    '''

    # collecting data from the request object 
    the_data = request.json

    # extracting the variable
    subject = the_data['subject']
    content = the_data['content']

    cursor = db.get_db().cursor()

    query = f'UPDATE Message\
                    SET subject = {subject}, content = {content}\
                    WHERE comID = {comid};'

    # update with new content and keep remaining old subject
    cursor.execute(query)
    # log the query
    current_app.logger.info(query)

    # commit the changes
    db.get_db().commit()


    return "Updated message."