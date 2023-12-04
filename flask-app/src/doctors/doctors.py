from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


doctors = Blueprint('doctors', __name__)

# Get all the products from the database
@doctors.route('/doctor', methods=['GET'])
def get_products():

    '''
    Get all doctors from the database

    columns: doctorID, specialization, firstName, lastNmae for the doctor
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT * FROM HuskyHealth.Doctor')

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

@doctors.route('/prescriptions/<doctorid>/<patientid>', methods=['GET'])
def get_prescriptions_for_doctor(doctorID):

    '''
    Get all the doctors prescriptions

    columns: medication, pharmacy, dateprescribed, patientID
    '''

    query = 'SELECT medication, pharmacy, dateprescribed, patientID FROM HuskyHealth.Prescriptions\
                WHERE doctorID = {doctorID};'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)
    

@doctors.route('/notifications/<doctorid>/<patientid>', methods=['Get'])
def get_notifications_for_doctors_patients(doctorID):

    '''
    Get all the doctors' patients' notifcations

    columns: medication, pharmacy, dateprescribed, patientID
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT Notifications.patientID, content, timeSent FROM HuskyHealth.Notifications\
        JOIN HuskyHealth.Patient ON Notifications.patientID = Patient.patientID\
        JOIN HuskyHealth.Visit ON Patient.patientID = Visit.patientID\
        WHERE status = ''Unread'' AND doctorID = {doctorID};'

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


@doctors.route('/messages/<doctorid>/<patientid>', methods=['Get'])
def get_messages_for_doctor(doctorID):

    '''
    Get all the doctors' messages

    columns: subject, content, dateSent, patientID
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT subject, content, dateSent, patientID FROM HuskyHealth.Message\
        WHERE doctorID = {doctorID} ORDER BY dateSent DESC;'

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


@doctors.route('/healthrecords/<doctorid>/<patientid>', methods=['Get'])
def get_healthRecords_for_doctors_patients(doctorID):

    '''
    Get all the doctors' patients' health records

    columns: healthRecordID, familyHistory, allergies, vaxHistory
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT healthRecordID, familyHistory, allergies, vaxHistory FROM HuskyHealth.HealthRecords\
        WHERE doctorID = {doctorID}\
        ORDER BY patientID;'

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


@doctors.route('/labresults/notifications/<doctorid>/<patientid>', methods=['Get'])
def get_labresults_for_doctors_patients(doctorID):

    '''
    Get all the doctors' patients' lab results

    columns:
    '''

    cursor = db.get_db().cursor()

    query = f''

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


@doctors.route('/visits/<doctorid>/<patientid>', methods=['Get'])
def get_visits_for_doctors(doctorID):

    '''
    Get all the doctors' patients' visits

    columns: purpose, visitDate, patientID
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT purpose, visitDate, patientID FROM HuskyHealth.Visit\
        WHERE doctorID = {doctorID};'

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



@doctors.route('/messages/<doctorid>/<repid>', methods=['Get'])
def get_messages_for_doctors(doctorID, repID):

    '''
    Returns messages between a doctor and a rep

    columns:
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT subject, content, dateSent FROM HuskyHealth.Message\
        WHERE doctorID = {doctorID} AND repID = {repID};'

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
























@doctors.route('/prescriptions/<doctorid>/<patientid>', methods=['POST'])
def add_new_doctor_prescription(doctorid, patientid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    scriptID = the_data['scriptID']
    type = the_data['type']
    visitID = the_data['visitID']
    testID = the_data['testID']
    resultDate = the_data['resultDate']
    company = the_data['company']
    status = the_data['status']
    datePrescribed = the_data['datePrescribed']
    pharmacy = the_data['pharmacy']
    medication = the_data['medication']
    duration = the_data['duration']

    # Constructing the query
    query = 'insert into Doctors (scriptID, type, visitID, testID, patientID, resultDate, company, doctorID, status\
        datePrescribed, pharmacy, medication, duration) values ("'
    query += scriptID + '", "'
    query += type + '", "'
    query += visitID + '", '
    query += testID + '", '
    query += {patientid} + '", "'
    query += resultDate + '", "'
    query += company + '", '
    query += {doctorid} + '", '
    query += status + '", "'
    query += datePrescribed + '", "'
    query += pharmacy + '", '
    query += medication + '", '
    query += duration + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@doctors.route('/messages/<doctorid>/<patientid>', methods=['POST'])
def add_new_message_doctor_to_patient(doctorid, patientid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    comID = the_data['comID']
    dateSent = the_data['dateSent']
    subject = the_data['subject']
    content = the_data['content']


    # Constructing the query
    query = 'insert into Messages (comID, dateSent, subject, content, patientID, doctorID) values ("'
    query += comID + '", "'
    query += dateSent + '", "'
    query += subject + '", '
    query += content + '", "'
    query += {patientid} + '", "'
    query += {doctorid} + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@doctors.route('/healthrecords/{<doctorid>/<patientid>', methods=['POST'])
def add_new_doctor_healthrecord(doctorid, patientid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    healthRecordID = the_data['healthRecordID']
    familyHistory = the_data['familyHistory']
    allergies = the_data['product_price']
    vaxHistory = the_data['vaxHistory']
    scriptID = the_data['scriptID']

    # Constructing the query
    query = 'insert into HealthRecords (healthRecordID, familyHistory, allergies, vaxHistory, patientID, doctorID, scriptID) values ("'
    query += healthRecordID + '", "'
    query += familyHistory + '", "'
    query += allergies + '", '
    query += vaxHistory + '", "'
    query += {patientid} + '", "'
    query += {doctorid} + '", '
    query += scriptID + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@doctors.route('/labresults/notifications/<doctorid>/<patientid>', methods=['POST'])
def add_new_labresults_doctor(doctorid, patientid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    testID = the_data['testID']
    result = the_data['result']
    type = the_data['type']
    testDate = the_data['testDate']

    # Constructing the query
    query = 'insert into LabResults (testID, result, type, testDate) values ("'
    query += testID + '", "'
    query += result + '", "'
    query += type + '", '
    query += testDate + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@doctors.route('/visits/<doctorid>/<patientid>', methods=['POST'])
def add_new_visit_doctor(doctorid, patientid):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    visitID = the_data['visitID']
    purpose = the_data['purpose']
    visitDate = the_data['visitDate']

    # Constructing the query
    query = 'insert into Visits (visitID, purpose, visitDate, patientID, doctorID) values ("'
    query += visitID + '", "'
    query += purpose + '", "'
    query += visitDate + '", '
    query += {patientid} + '", '
    query += {doctorid} + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@doctors.route('/messages/<doctorid>/<repid>', methods=['POST'])
def add_new_message_doctor_to_rep(doctorid, repid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    comID = the_data['comID']
    dateSent = the_data['dateSent']
    subject = the_data['subject']
    content = the_data['content']


    # Constructing the query
    query = 'insert into Messages (comID, dateSent, subject, content, patientID, doctorID) values ("'
    query += comID + '", "'
    query += dateSent + '", "'
    query += subject + '", '
    query += content + '", "'
    query += {repid} + '", "'
    query += {doctorid} + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'
