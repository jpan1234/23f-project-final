from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


doctors = Blueprint('doctors', __name__)


@doctors.route('/patients/<doctorid>', methods=['GET'])
def get_patients(doctorid):

    '''
    Get all the doctors prescriptions

    columns: medication, pharmacy, dateprescribed, patientID
    '''

    query = f'SELECT DISTINCT V.patientID, Patient.firstName, Patient.lastName FROM Patient\
                JOIN Visit V on Patient.patientID = V.patientID\
                WHERE V.doctorID = {doctorid};'
    

    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

@doctors.route('/prescriptions/<doctorid>', methods=['GET'])
def get_prescriptions_for_doctor(doctorid):

    '''
    Get all the doctors prescriptions

    columns: medication, pharmacy, dateprescribed, patientID
    '''

    query = f'SELECT medication, pharmacy, datePrescribed, patientID FROM Prescriptions\
                WHERE doctorID = {doctorid}]
                ORDER BY datePrescribed DESC;'
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
def get_notifications_for_doctors_patients(doctorid):

    '''
    Get all the doctors' patients' notifcations

    columns: medication, pharmacy, dateprescribed, patientID
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT Notifications.patientID, content, timeSent FROM Notifications\
        JOIN Patient ON Notifications.patientID = Patient.patientID\
        JOIN Visit ON Patient.patientID = Visit.patientID\
        WHERE status = "Unread" AND doctorID = {doctorid};'

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
def get_messages_for_doctor(doctorid):

    '''
    Get all the doctors' messages

    columns: subject, content, dateSent, patientID
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT subject, content, patientID FROM Message\
        WHERE doctorID = {doctorid}\
        ORDER BY dateSent DESC;'

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
def get_healthRecords_for_doctors_patients(doctorid):

    '''
    Get all the doctors' patients' health records

    columns: healthRecordID, familyHistory, allergies, vaxHistory
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT healthRecordID, patientID, familyHistory, allergies, vaxHistory FROM HealthRecords\
        WHERE doctorID = {doctorid}\
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



@doctors.route('/labresults/<doctorid>', methods=['Get'])
def get_labresults_for_doctors_patients(doctorid):

    '''
    Get all the doctors' patients' lab results

    columns:
    '''

    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(f'SELECT result, type, testDate, LabResults.patientID FROM LabResults\
                     JOIN Patient\
                     ON LabResults.patientID = Patient.patientID\
                     JOIN Visit\
                     ON Visit.patientID = Patient.patientID\
                     WHERE Visit.doctorID = {doctorid}\
                     ;')

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
def get_visits_for_doctors(doctorid):

    '''
    Get all the doctors' patients' visits

    columns: purpose, visitDate, patientID
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT purpose, visitDate, patientID FROM Visit\
            WHERE doctorID = {doctorid}\
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



@doctors.route('/messages/<doctorid>', methods=['Get'])
def get_rep_messages_for_doctors(doctorid):

    '''
    Returns messages between a doctor and a their patients' corresponding representatitves

    columns:
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT subject, content, dateSent, repID FROM Message\
        WHERE doctorID = {doctorid}\
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



@doctors.route('/prescriptions/<doctorid>', methods=['POST'])
def add_new_doctor_prescription(doctorid):
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
    patientid = the_data['patientid'] # obtain the doctorid

    # Constructing the query
    query = 'INSERT INTO Prescription (scriptID, type, visitID, testID, patientID, resultDate, company, doctorID, status\
        datePrescribed, pharmacy, medication, duration) VALUES ("'
    query += scriptID + '", "'
    query += type_prescription + '", "'
    query += visitID + '", "'
    query += testID + '", "'
    query += patientid + '", "'
    query += resultDate + '", "'
    query += company + '", "'
    query += doctorid + '", "'
    query += status + '", "'
    query += datePrescribed + '", "'
    query += pharmacy + '", "' 
    query += medication + '", "'
    query += str(duration) + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'



@doctors.route('/messagepatient/<doctorid>', methods=['POST'])
def add_new_message_doctor_to_patient(doctorid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    subject = the_data['subject']
    content = the_data['content']
    patientid = the_data['patientID']
    datesent = the_data['dateSent']


    # Constructing the query
    query = 'INSERT INTO Message (subject, content, patientID, dateSent, doctorID) values ("'
    query += subject + '", "'
    query += content + '", "'
    query += patientid + '", "'
    query += datesent + '",'
    query += doctorid + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

@doctors.route('/messagerep/<doctorid>', methods=['POST'])
def add_new_message_doctor_to_rep(doctorid):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    subject = the_data['subject']
    content = the_data['content']
    repid = the_data['repID']
    datesent = the_data['dateSent']


    # Constructing the query
    query = 'INSERT INTO Message (subject, content, repID, dateSent, doctorID) values ("'
    query += subject + '", "'
    query += content + '", "'
    query += repid + '", "'
    query += datesent + '",'
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
    allergies = the_data['allergies']
    vaxHistory = the_data['vaxHistory']
    scriptID = the_data['scriptID']
    patientID = the_data['patientID']

    # Constructing the query
    query = 'INSERT INTO HealthRecords (healthRecordID, familyHistory, allergies, vaxHistory, patientID, doctorID, scriptID) VALUES ("'
    query += healthRecordID + '", "'
    query += familyHistory + '", "'
    query += allergies + '", "'
    query += vaxHistory + '", "'
    query += patientID + '", "'
    query += doctorid + '", "'
    query += scriptID + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@doctors.route('/labresults/', methods=['POST'])
def add_new_labresults_doctor():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    testID = the_data['testID']
    result = the_data['result']
    result_type = the_data['type']
    testDate = the_data['testDate']
    patientid = the_data['patientID']


    # Constructing the query
    query = 'INSERT INTO LabResults (testID, result, type, testDate, patientID) VALUES ("'
    query += testID + '", "'
    query += result + '", "'
    query += result_type + '", "'
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


# PUT COMMANDS

# update a message
@doctors.route('/messages/<comid>', methods=['PUT'])
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

    query = f'UPDATE Message\
                    SET subject = {subject}, content = {content}\
                    WHERE comID = {comid};'
    cursor = db.get_db().cursor()

    # update with new content and keep remaining old subject
    cursor.execute(query)
    # log the query
    current_app.logger.info(query)

    # commit the changes
    db.get_db().commit()


    return "Updated message."


# cancel a doctor visit
@doctors.route('/visits/<visitid>', methods=['PUT'])
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

    query = f'UPDATE Visit\
                     SET canceled = {canceled}\
                     WHERE visitID = {visitid};'
    
    # use cursor to query the database for a list of products
    cursor.execute(query)
    
    # log query
    current_app.logger.info(query)

    # commit changes
    db.get_db().commit()

    return 'Canceled visit.'


# update a prescription
@doctors.route('/prescriptions/', methods=['PUT'])
def update_prescription():
    '''
    Update a prescription

    columns: 
    '''

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    deactived = the_data['deactived'] # either 1 or 0, mostly going to set to 1 to set as "complete"
    scriptid = the_data['scriptID']

    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = f'UPDATE Presctiptions\
                     SET inactive = {deactived}\
                     WHERE scriptID = {scriptid};'
    
    # use cursor to query the database for a list of products
    cursor.execute(query)
    
    # log query
    current_app.logger.info(query)

    # commit changes
    db.get_db().commit()

    return 'Canceled visit.'


# DELETE ROUTE

# Deletes a notification
@doctors.route('/notifications/<notificationid>', methods=['DELETE'])
def delete_notification(notificationid):
    
    query = f'DELETE\
        FROM Notifications\
        WHERE notificationID = {notificationid};'
        
    # get cursor and execute it
    cursor = db.get_db().cursor()

    cursor.execute(query)
    
    # commit changes
    db.get_db().commit()

    return "Successfully deleted notification!"