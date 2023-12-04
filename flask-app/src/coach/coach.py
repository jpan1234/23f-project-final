from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


coach = Blueprint('coach', __name__)

# Get all the unseen notifications sent by the coach's patient from the database
@coach.route('/notifications/<coachid>/<patientid>', methods=['GET'])
def get_notifications_from_patient(patient_id):
    '''
    Get all notifications that are unseen from coach's patient

    columns: 
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT Notifications.patientID, content, timeSent FROM HuskyHealth.Notifications\
        JOIN HuskyHealth.Patient ON Notifications.patientID = Patient.patientID\
        JOIN HuskyHealth.Visit ON Patient.patientID = Visit.patientID\
        WHERE status = ''Unread'' AND patientID = {patientID};')

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

# Get all messages between coach and affiliated patient
@coach.route('/messages/<coachid>/<patientid>', methods=['GET'])
def get_messages_from_coach(coach_id, patient_id):
    '''
    Get all messages between coach and affiliated patient

    columns: 
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT subject, content, dateSent FROM HuskyHealth.Message\
                     WHERE patientID = {patientid}\
                     AND coachID = {coachid}\
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

# Get all visits associated with the coach's patient
@coach.route('/visits/<coachid>/<patientid>', methods=['GET'])
def get_coach_visits(coach_id, patient_id):
    '''
    Get all visits between coach and affiliated patient

    columns: 
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT purpose, visitDate\
                     FROM HuskyHealth.Visit\
                     WHERE patientID = {patientid}\
                     and coachID = {coachid}')

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



# Get list of the health records a coach is allowed to view of affiliated patient
@coach.route('/healthrecords/<coachid>/<patientid>', methods=['GET'])
def get_coach_healthrecords(patient_id, coach_id):
    '''
    Gets list of health records a coach can view of affiliated patient

    columns: 
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT familyHistory, allergies, vaxHistory\
                     FROM HuskyHealth.HealthRecords\
                     WHERE patientID = {patientid}\
                     and repConsent = 1')

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

# Get list of all wellness records a coach has of patient
@coach.route('/wellnessrecord/<coachid>/<patientid>', methods=['GET'])
def get_coach_records(patient_id, coach_id):
    '''
    Gets list of all goals a coach has sent to affiliated patient

    columns: 
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT goal, description\
                     FROM HuskyHealth.WellnessRecord\
                     WHERE patientID = {patientid}\
                     and coachID = {coachid}')

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