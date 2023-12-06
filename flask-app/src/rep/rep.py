from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


rep = Blueprint('rep', __name__)

# get all insurance plans affiliated with rep
@rep.route('/insuranceplans/<repid>', methods=['GET'])
def get_patient_insurance_plan(repid):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT Patient.firstName, Patient.lastName,\
                    InsurancePlan.description, Patient.patientID\
                    FROM Patient\
                    JOIN BillingRecord\
                    ON Patient.patientID = BillingRecord.patientID\
                    JOIN InsurancePlan\
                    ON BillingRecord.planID = InsurancePlan.planID\
                    WHERE InsurancePlan.repID = {repid};')

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


# Provide a list of all unique insurance plans 
@rep.route('/insuranceplan', methods=['GET'])
def get_all_insurance_plans():
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
@rep.route('/healthrecords/<patientid>', methods=['GET'])
def get_patient_health_records(patientid):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of healthrecords if the given rep has consent
    query = f'SELECT * FROM HealthRecords\
                JOIN InsuranceRepresentative\
                ON HealthRecords.repID = InsuranceRepresentative.repID\
                WHERE HealthRecords.patientID = {patientid}\
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
@rep.route('/billingrecords/<repid>', methods=['GET'])
def get_patient_billing_records(repid):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    query = f'''SELECT BillingRecord.description, amount, paid FROM BillingRecord\
                JOIN InsurancePlan ON BillingRecord.planID = InsurancePlan.planID\
                WHERE repID = {repid}
                '''
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

@rep.route('/messages/<repid>', methods=['GET'])
def get_message_patient(repid):
    '''
    Get all messages for a particular patient

    columns: subject, content, dateSent for the patient
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT subject, content, dateSent, patientID, doctorID FROM Message\
                     WHERE repID = {repid}\
                     ORDER BY dateSent DESC;')

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
@rep.route('/insuranceplan/>', methods=['POST'])
def add_patient_insurance_plan():

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    terminationDate = the_data['description']
    copay = the_data['amount']
    description = the_data['repID']
    repID = the_data['repID']
    inactive = "0"

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
@rep.route('/insuranceplans/<patientid>', methods=['POST'])
def add_patient_billing_record (patientid):

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
    query += patientid + '", '
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


# post a message to a patient
@rep.route('/messages/<repid>', methods=['POST'])
def post_patient_message(repid):
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
    patientid = the_data['patientID']
    datesent = the_data['dateSent']


    # Constructing the query
    query = 'INSERT INTO Message (subject, content, patientID, dateSent, repID) VALUES ("'
    query += subject + '", "'
    query += content + '", "'
    query += patientid + '", "'
    query += datesent + '", '
    query += repid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Message sent!'

# post a message to a doctor
@rep.route('/messages/<repid>', methods=['POST'])
def post_doctor_message(repid):
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
    doctorid = the_data['doctorID']
    datesent = the_data['dateSent']


    # Constructing the query
    query = 'INSERT INTO Message (subject, content, doctorID, dateSent, repID) VALUES ("'
    query += subject + '", "'
    query += content + '", "'
    query += doctorid + '", "'
    query += datesent + '", '
    query += repid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Message sent!'







# PUT METHODS




# updates a patient's current insurance plan
@rep.route('/rep/insuranceplans/<planid>', methods=['PUT'])
def update_patient_insurance_plan(planid):
    
    # collecting data from request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting variable data 
    terminationDate = the_data['terminationDate']
    copay = the_data['copay']
    description = the_data['description']
    inactive = the_data['inactive'] # have the choice to set something as inactive
    patientid = the_data['patientID']
        
    # create update query
    the_query = f'''UPDATE InsurancePlan\
                    SET terminationDate = {terminationDate}, copay = {copay}, description = {description},\
                        inactive = {inactive}, patientID = {patientid}\
                    WHERE planID = {planid}'''
    current_app.logger.info(the_query)
    
    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "Success!"

# set billing record as paid
@rep.route('/billingrecord/<patientid>', methods=['PUT'])
def pay_bill(patientid):

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
                     AND patientID = {patientid};'
    
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