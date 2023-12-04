from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


patients = Blueprint('patients', __name__)

# Get all the prescriptions from the database 
@patients.route('/prescriptions/<patientid>', methods=['GET'])
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

# Get all the notifications from the database 
@patients.route('/notifications/<patientid>', methods=['GET'])
def get_notifications(patientid):
    '''
    Get all notifications from the database for the patient

    columns: content for the patient
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT content FROM HuskyHealth.Notifications\
                    WHERE patientID = {patientid}\
                    AND status = "Unread";')

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


# Get all the messages from the database from a doctor 
@patients.route('/messages/<patientid>', methods=['GET'])
def get_message(patientid):
    '''
    Get all messages for a particular patient

    columns: subject, content, dateSent for the patient
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT subject, content, dateSent FROM HuskyHealth.Message\
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


# Get all the healthrecords from the database for a patient 
@patients.route('/healthrecords/<patientid>', methods=['GET'])
def get_health_records(patientid):
    '''
    Get all health records from the database for the patient

    columns: first name, last name, familyHistory, allergies, vaxHistory
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT familyHistory, allergies, vaxHistory\
                    FROM HealthRecords\
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


# Get all the lab results from the database for a patient 
@patients.route('/labresults/<patientid>', methods=['GET'])
def get_lab_records(patientid):
    '''
    Get all lab result records from the database for the patient

    columns: result, type, testDate
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT result, type, testDate FROM LabResults\
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

# Get all the visits records from the database for a patient 
@patients.route('/visits/<patientid>', methods=['GET'])
def get_visit_records(patientid):
    '''
    Get all visits records from the database for the patient

    columns: purpose, visitDate
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT purpose, visitDate\
                     FROM HuskyHealth.Visit\
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

# Get all the billing records from the database for a patient 
@patients.route('/billingrecords/<patientid>', methods=['GET'])
def get_billing_records(patientid):
    '''
    Get all billing records from the database for the patient

    columns: description, amount
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT description, amount\
                     FROM HuskyHealth.BillingRecord\
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



# Get all the wellness goal records from the database for a patient 
@patients.route('/wellnessrecords/<patientid>', methods=['GET'])
def get_wellness_records(patientid):
    '''
    Get all wellness records from the database for the patient

    columns: description, goal
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT goal, description\
                     FROM HuskyHealth.WellnessRecord\
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















# POST METHODS

# post a message from a patient to a doctor
@patients.route('/messages/<doctorid>', methods=['POST'])
def post_doctor_message(doctorid):
    '''
    Post a message to the database from a patient to a doctor

    columns: subject, content, patientid, doctorid
    '''
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    subject = the_data['subject']
    content = the_data['content']
    patientid = the_data['patientID']


    # Constructing the query
    query = 'INSERT INTO HuskyHealth.Message (subject, content, patientid, doctorid) VALUES ("'
    query += subject + '", "'
    query += content + '", "'
    query += patientid + '", '
    query += doctorid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Message sent!'

# post a message from a patient to a coach
@patients.route('/messages/<coachid>', methods=['POST'])
def post_coach_message(coachid):
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
    patientid = the_data['patientID']


    # Constructing the query
    query = 'INSERT INTO Message (subject, content, patientid, coachid) VALUES ("'
    query += subject + '", "'
    query += content + '", "'
    query += patientid + '", '
    query += coachid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Message sent!'



# post a message from a patient to a rep
@patients.route('/messages/<repid>', methods=['POST'])
def post_rep_message(repid):
    '''
    Post a message to the database from a patient to a rep

    columns: subject, content, patientid, repid
    '''
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    subject = the_data['subject']
    content = the_data['content']
    patientid = the_data['patientID']

    # Constructing the query
    query = 'INSERT INTO HuskyHealth.Message (subject, content, patientid, repid) VALUES ("'
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


# post a visit with a doctor
@patients.route('/visits/<doctorid>', methods=['POST'])
def schedule_doctor_visit(patientid, doctorid):
    '''
    Schedule a visit with a doctor

    columns: purpose, visitDate, patientID, doctorID
    '''
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    purpose = the_data['purpose']
    visitDate = the_data['visitDate']
    patientid = the_data['patientID']

    # Constructing the query
    query = 'INSERT INTO Visit (purpose, visitDate, patientID, doctorID) VALUES ("'
    query += purpose + '", "'
    query += visitDate + '", "'
    query += patientid + '", '
    query += doctorid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Visit scheduled!'

# post a visit with a coach
@patients.route('/visits/<coachid>', methods=['POST'])
def schedule_coach_visit(coachid):
    '''
    Schedule a visit with a coach

    columns: purpose, visitDate, patientID, coachID
    '''
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    purpose = the_data['purpose']
    visitDate = the_data['visitDate']
    patientid = the_data['patientID']


    # Constructing the query
    query = 'INSERT INTO Visit (purpose, visitDate, patientID, coachID) VALUES ("'
    query += purpose + '", "'
    query += visitDate + '", "'
    query += patientid + '", '
    query += coachid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Visit scheduled!'























# PUT COMMANDS

# update a message to a doctor
@patients.route('/messages/<comid>', methods=['PUT'])
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

    query = f'UPDATE HuskyHealth.Message\
                    SET subject = {subject}, content = {content}\
                    WHERE comID = {comid};'

    # update with new content and keep remaining old subject
    cursor.execute(query)
    # log the query
    current_app.logger.info(query)

    # commit the changes
    db.get_db().commit()


    return "Updated message."

# update a wellness record
@patients.route('/wellnessrecords/<wellnessrecordid>', methods=['PUT'])
def update_patient_wellnessrecord(wellnessrecordID):
    '''
    Update a wellness goal as complete or not

    columns
    '''

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    completed = the_data['complete'] # either 1 or 0, mostly going to set to 1 to set as "complete"

    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = f'UPDATE HuskyHealth.WellnessRecord\
                     SET complete = {completed}\
                     WHERE wellnessrecordID = {wellnessrecordID};'
    
    # use cursor to query the database for a list of products
    cursor.execute(query)
    
    # log query
    current_app.logger.info(query)

    # commit changes
    db.get_db().commit()

    return 'Updated wellness record!'

# cancel a doctor visit
@patients.route('/visits/<visitid>', methods=['PUT'])
def cancel_doctor_visit(visitid):
    '''
    Cancel a visit 

    columns: 
    '''

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    canceled = the_data['canceled'] # either 1 or 0, mostly going to set to 1 to set as "complete"

    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = f'UPDATE HuskyHealth.Visit\
                     SET canceled = {canceled}\
                     WHERE visitID = {visitid};'
    
    # use cursor to query the database for a list of products
    cursor.execute(query)
    
    # log query
    current_app.logger.info(query)

    # commit changes
    db.get_db().commit()

    return 'Canceled visit.'

# Deletes a notification
@patients.route('/notifications/<notificationid>', methods=['DELETE'])
def delete_notification(notificationID):
    
    query = f'DELETE\
        FROM Notifications\
        WHERE notificationID = {notificationID};'
        
    # get cursor and execute it
    cursor = db.get_db().cursor()

    cursor.execute(query)
    
    # commit changes
    db.get_db().commit()

    return "Successfully deleted notification!"