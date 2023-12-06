from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


coach = Blueprint('coach', __name__)

# GETS

# Get all the unseen notifications for the coach
@coach.route('/notifications/<coachid>', methods=['GET'])
def get_notifications_from_patient(coachid):
    '''
    Get all notifications that are unseen from coach's patient

    columns: 
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = f'SELECT notificationID, Notifications.patientID, content, timeSent FROM Notifications\
        JOIN Patient ON Notifications.patientID = Patient.patientID\
        JOIN Visit ON Patient.patientID = Visit.patientID\
        WHERE status = "Unread" AND deleted = 0 AND coachID = {coachid};'

    # use cursor to query the database for a list of products
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

# Get all coachs messages
@coach.route('/messages/<coachid>', methods=['GET'])
def get_messages_from_coach(coachid):
    '''
    Get all messages between coach and affiliated patient

    columns: 
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = f'SELECT subject, content, dateSent,patientID FROM Message\
                     WHERE coachID = {coachid}\
                     ORDER BY dateSent DESC;'

    # use cursor to query the database for a list of products
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

# Get all coachs visits
@coach.route('/visits/<coachid>', methods=['GET'])
def get_coach_visits(coachid):
    '''
    Get all coachs visits

    columns: 
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = f'SELECT purpose, visitDate\
                     FROM HuskyHealth.Visit\
                     WHERE coachID = {coachid};'

    # use cursor to query the database for a list of products
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


# Get list of all wellness records of a coach
@coach.route('/wellnessrecord/<coachid>', methods=['GET'])
def get_coach_records(coachid):
    '''
    Gets list of all goals of a coach 

    columns: 
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    query = f'SELECT goal, description\
                     FROM WellnessRecord\
                     JOIN Visit ON WellnessRecord.patientID = Visit.patientID\
                     WHERE Visit.coachID = {coachid};'

    # use cursor to query the database for a list of products
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

# get all coachs patients health records
@coach.route('/healthrecords/<coachid>', methods=['Get'])
def get_healthRecords_for_coach(coachid):

    '''
    Get all the coachs' patients' health records

    columns: healthRecordID, familyHistory, allergies, vaxHistory
    '''

    cursor = db.get_db().cursor()

    query = f'SELECT healthRecordID, familyHistory, allergies, vaxHistory FROM HealthRecords\
        JOIN WellnessCoach\
        ON WellnessCoach.coachID = HealthRecords.coachID\
        WHERE HealthRecords.coachID = {coachid} AND WellnessCoach.consent = 1'

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



# POSTS

# posts a message to coachs patient

@coach.route('/messages/<coachid>', methods=['POST'])
def post_coach_message(coachid):
    '''
    Post a message to the database from a patient to a coach

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
    query = 'INSERT INTO HuskyHealth.Message (subject, content, patientid, coachid) VALUES ("'
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

# add a visit to the database by coach

@coach.route('/visit/<coachid>', methods=['POST'])
def post_coach_visit(coachid):

    '''
    Post a visit to the database from coach to patient

    columns: subject, content, patientid, doctorid
    '''

    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    purpose = the_data['purpose']
    visitDate = the_data['visitDate']
    patientid = the_data['patientID']

    # Constructing the query
    query = 'INSERT INTO HuskyHealth.Visit (purpose, visitDate, patientID, coachID) VALUES ("'
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

# PUT

# update a message to a patient
@coach.route('/messages/<comid>', methods=['PUT'])
def update_message_coach(comid):
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

# cancel a coach visit
@coach.route('/visits/<visitid>', methods=['PUT'])
def cancel_coach_visit(visitid):
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

# DELETE

# Deletes a notification
@coach.route('/deletenotifications/<notificationid>', methods=['DELETE'])
def delete_notification_coach(notificationid):
    
    query = f'DELETE\
        FROM Notifications\
        WHERE notificationID = {notificationid};'
        
    # get cursor and execute it
    cursor = db.get_db().cursor()

    cursor.execute(query)
    
    # commit changes
    db.get_db().commit()

    return "Successfully deleted message!"

