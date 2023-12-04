from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


products = Blueprint('doctors', __name__)

@doctors.route('/prescriptions/<doctorid>/<patientid>', methods=['GET'])
def get_prescriptions_for_doctor(doctorID):

    '''
    Get all the doctors prescriptions

    columns: medication, pharmacy, dateprescribed, patientID
    '''

    query = f'SELECT medication, pharmacy, dateprescribed, patientID FROM Prescriptions\
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
    

@doctors.route('/notifications/<doctorid>', methods=['Get'])
def get_notifications_for_doctors_patients(doctorID):

    '''
    Get all the doctors' patients' notifcations

    columns: medication, pharmacy, dateprescribed, patientID
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT Notifications.patientID, content, timeSent FROM Notifications\
        JOIN Patient ON Notifications.patientID = Patient.patientID\
        JOIN Visit ON Patient.patientID = Visit.patientID\
        WHERE status = "Unread" AND doctorID = {doctorID};'

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


@doctors.route('/messages/<doctorid>', methods=['Get'])
def get_messages_for_doctor(doctorID):

    '''
    Get all the doctors' messages

    columns: subject, content, dateSent, patientID
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT subject, content, dateSent, patientID FROM Message\
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


@doctors.route('/healthrecords/<doctorid>', methods=['Get'])
def get_healthRecords_for_doctors_patients(doctorID):

    '''
    Get all the doctors' patients' health records

    columns: healthRecordID, familyHistory, allergies, vaxHistory
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT healthRecordID, familyHistory, allergies, vaxHistory FROM HealthRecords\
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





# THIS NEEDS TO BE CHANGED BELOW NEED TO ADD QUERY




@doctors.route('/labresults/<doctorid>', methods=['Get'])
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





@doctors.route('/visits/<doctorid>', methods=['Get'])
def get_visits_for_doctors(doctorID):

    '''
    Get all the doctors' patients' visits

    columns: purpose, visitDate, patientID
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT purpose, visitDate, patientID FROM Visit\
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



@doctors.route('/messages/<doctorid>', methods=['Get'])
def get_rep_messages_for_doctors(doctorID):

    '''
    Returns messages between a doctor and a their patients' corresponding representatitves

    columns:
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT subject, content, dateSent FROM Message\
        WHERE doctorID = {doctorID}\
        AND repID IS NOT NULL;'

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

















# POSTING 



@doctors.route('/prescriptions/<patientid>', methods=['POST'])
def add_new_doctor_prescription(patientid):
    ''' 
    adding a new prescription for a patient
    '''
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    scriptID = the_data['scriptID']
    type_prescription = the_data['type']
    visitID = the_data['visitID']
    testID = the_data['testID']
    resultDate = the_data['resultDate']
    company = the_data['company']
    status = the_data['status']
    datePrescribed = the_data['datePrescribed']
    pharmacy = the_data['pharmacy']
    medication = the_data['medication']
    duration = the_data['duration']
    doctorid = the_data['doctorID'] # obtain the doctorid

    # Constructing the query
    query = 'INSERT INTO Prescription (scriptID, type, visitID, testID, patientID, resultDate, company, doctorID, status\
        datePrescribed, pharmacy, medication, duration) VALUES ("'
    query += scriptID + '", "'
    query += type_prescription + '", "'
    query += visitID + '", '
    query += testID + '", '
    query += patientid + '", "'
    query += resultDate + '", "'
    query += company + '", '
    query += doctorid + '", '
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

    








@doctors.route('/messages/<patientid>', methods=['POST'])
def add_new_message_doctor_to_patient(patientid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    subject = the_data['subject']
    content = the_data['content']
    doctorid = the_data['doctorID']


    # Constructing the query
    query = 'INSERT INTO Message (comID, dateSent, subject, content, patientID, doctorID) values ("'
    query += comID + '", "'
    query += dateSent + '", "'
    query += subject + '", '
    query += content + '", "'
    query += patientid + '", "'
    query += doctorid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@doctors.route('/healthrecords/<doctorid>', methods=['POST'])
def add_new_doctor_healthrecord(doctorid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    healthRecordID = the_data['healthRecordID']
    familyHistory = the_data['familyHistory']
    allergies = the_data['product_price']
    vaxHistory = the_data['vaxHistory']
    scriptID = the_data['scriptID']
    patientID = the_data['patientID']

    # Constructing the query
    query = 'INSERT INTO HealthRecords (healthRecordID, familyHistory, allergies, vaxHistory, patientID, doctorID, scriptID) VALUES ("'
    query += healthRecordID + '", "'
    query += familyHistory + '", "'
    query += allergies + '", '
    query += vaxHistory + '", "'
    query += patientid + '", "'
    query += doctorid + '", '
    query += scriptID + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@doctors.route('/labresults/<patientid>', methods=['POST'])
def add_new_labresults_doctor(patientid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    testID = the_data['testID']
    result = the_data['result']
    result_type = the_data['type']
    testDate = the_data['testDate']


    # Constructing the query
    query = 'INSERT INTO LabResults (testID, result, type, testDate, patientID) VALUES ("'
    query += testID + '", "'
    query += result + '", "'
    query += result_type + '", '
    query += testDate + '", '
    query += patientid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@doctors.route('/visits/<doctorid>', methods=['POST'])
def add_new_visit_doctor(doctorid):

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    visitID = the_data['visitID']
    purpose = the_data['purpose']
    visitDate = the_data['visitDate']
    patientid = the_data['patientID'] # patient id will be requested

    # Constructing the query
    query = 'INSERT INTO Visits (visitID, purpose, visitDate, patientID, doctorID) VALUES ("'
    query += visitID + '", "'
    query += purpose + '", "'
    query += visitDate + '", '
    query += patientid + '", '
    query += doctorid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@doctors.route('/messages/<repid>', methods=['POST'])
def add_new_message_doctor_to_rep(repid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    comID = the_data['comID']
    dateSent = the_data['dateSent']
    subject = the_data['subject']
    content = the_data['content']
    doctor = the_data['doctorID'] # doctor will need to be provided, shouldn't this be other way?


    # Constructing the query
    query = 'INSERT INTO Message (comID, dateSent, subject, content, patientID, doctorID) VALUES ("'
    query += comID + '", "'
    query += dateSent + '", "'
    query += subject + '", '
    query += content + '", "'
    query += repid + '", "'
    query += doctorid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'
