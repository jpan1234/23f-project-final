# creating database HuskyHealth
CREATE DATABASE IF NOT EXISTS HuskyHealth;

# use the database
USE HuskyHealth;

# creating the Patient table
CREATE TABLE IF NOT EXISTS Patient
(
    patientID INT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName  VARCHAR(255),
    birthDate DATE,
    age INT
);

# updating the age to be the timestamp difference between birth date and current date
UPDATE Patient SET age = TIMESTAMPDIFF(YEAR, birthDate, CURDATE());

# creating the Doctor table
CREATE TABLE IF NOT EXISTS Doctor (
    doctorID INT PRIMARY KEY,
    specialization VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255)
);

# creating WellnessCoach table
CREATE TABLE IF NOT EXISTS WellnessCoach (
    coachID INT PRIMARY KEY,
    education VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255)
);

# creating InsuranceRepresentative table
CREATE TABLE IF NOT EXISTS InsuranceRepresentative (
    repID INT PRIMARY KEY,
    company VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255)
);

# creating Visit table
CREATE TABLE IF NOT EXISTS Visit (
    visitID INT PRIMARY KEY,
    purpose VARCHAR(255),
    visitDate DATE,
    patientID INT,
    doctorID INT,
    coachID INT,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (coachID) REFERENCES WellnessCoach(coachID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating LabResults table
CREATE TABLE IF NOT EXISTS LabResults (
    testID INT PRIMARY KEY,
    result TEXT,
    type VARCHAR(255),
    testDate DATE
);

# creating Prescriptions table
CREATE TABLE IF NOT EXISTS Prescriptions (
    scriptID INT PRIMARY KEY,
    type VARCHAR(255),
    visitID INT,
    testID INT,
    patientID INT,
    resultDate DATE,
    company VARCHAR(255),
    doctorID INT,
    status VARCHAR(50),
    datePrescribed DATE,
    pharmacy VARCHAR(255),
    medication VARCHAR(255),
    duration INT,
    FOREIGN KEY (visitID) REFERENCES Visit(visitID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (testID) REFERENCES LabResults(testID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating HealthRecords table
CREATE TABLE IF NOT EXISTS HealthRecords (
    healthRecordID INT PRIMARY KEY,
    familyHistory TEXT,
    allergies TEXT,
    vaxHistory TEXT,
    patientID INT,
    doctorID INT,
    scriptID INT,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (scriptID) REFERENCES Prescriptions(scriptID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating Message table
CREATE TABLE IF NOT EXISTS Message (
    comID INT PRIMARY KEY,
    dateSent DATE,
    subject VARCHAR(255),
    content TEXT,
    patientID INT,
    doctorID INT,
    coachID INT,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (coachID) REFERENCES WellnessCoach(coachID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating InsurancePLan table
CREATE TABLE IF NOT EXISTS InsurancePlan (
    planID INT PRIMARY KEY,
    terminationDate DATE,
    copay DECIMAL,
    description TEXT,
    repID INT,
    FOREIGN KEY (repID) REFERENCES InsuranceRepresentative(repID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating BillingRecord table
CREATE TABLE IF NOT EXISTS BillingRecord (
    billingRecordID INT PRIMARY KEY,
    description TEXT,
    amount DECIMAL,
    patientID INT,
    planID INT,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (planID) REFERENCES InsurancePlan(planID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating WellnessRecord table
CREATE TABLE IF NOT EXISTS WellnessRecord (
    wellnessRecordID INT PRIMARY KEY,
    goal VARCHAR(255),
    description TEXT,
    coachID INT,
    FOREIGN KEY (coachID) REFERENCES WellnessCoach(coachID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating AllergyRecord table
CREATE TABLE IF NOT EXISTS AllergyRecord (
    healthRecordID INT,
    allergies TEXT,
    PRIMARY KEY (healthRecordID),
    FOREIGN KEY (healthRecordID) REFERENCES HealthRecords(healthRecordID) ON UPDATE CASCADE ON DELETE CASCADE
);

# creating vaxhistoryRecord table
CREATE TABLE IF NOT EXISTS vaxHistoryRecord (
    healthRecordID INT,
    vaxHistory TEXT,
    PRIMARY KEY (healthRecordID),
    FOREIGN KEY (healthRecordID) REFERENCES HealthRecords(healthRecordID) ON UPDATE CASCADE ON DELETE CASCADE
);

# creating Notifications table
CREATE TABLE IF NOT EXISTS Notifications (
    notificationID INT PRIMARY KEY,
    content TEXT,
    status VARCHAR(50),
    timeSent TIMESTAMP,
    patientID INT,
    visitID INT,
    testID INT,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (visitID) REFERENCES Visit(visitID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (testID) REFERENCES LabResults(testID) ON UPDATE CASCADE ON DELETE SET NULL
);

/*


 Creating examples



 */

 -- Examples for each table

-- Patient Table
INSERT INTO Patient (patientID, firstName, lastName, birthDate, age)
VALUES
    (1, 'John', 'Doe', '1990-05-15', TIMESTAMPDIFF(YEAR, '1990-05-15', CURDATE())),
    (2, 'Jane', 'Smith', '1985-08-22', TIMESTAMPDIFF(YEAR, '1985-08-22', CURDATE()));

-- Doctor Table
INSERT INTO Doctor (doctorID, specialization, firstName, lastName)
VALUES
    (1, 'Cardiologist', 'Dr. Michael', 'Johnson'),
    (2, 'Pediatrician', 'Dr. Susan', 'Williams');

-- WellnessCoach Table
INSERT INTO WellnessCoach (coachID, education, firstName, lastName)
VALUES
    (1, 'Certified Nutritionist', 'Coach David', 'Miller'),
    (2, 'Fitness Trainer', 'Coach Emily', 'Taylor');

-- InsuranceRepresentative Table
INSERT INTO InsuranceRepresentative (repID, company, firstName, lastName)
VALUES
    (1, 'HealthInsure', 'Mark', 'Anderson'),
    (2, 'SecureCare', 'Laura', 'Smith');

-- Visit Table
INSERT INTO Visit (visitID, purpose, visitDate, patientID, doctorID, coachID)
VALUES
    (1, 'Regular Checkup', '2023-02-10', 1, 1, NULL),
    (2, 'Sports Injury', '2023-03-15', 2, 2, 1);

-- LabResults Table
INSERT INTO LabResults (testID, result, type, testDate)
VALUES
    (1, 'Normal', 'Blood Test', '2023-02-15'),
    (2, 'Positive', 'COVID-19', '2023-03-20');

-- Prescriptions Table
INSERT INTO Prescriptions (scriptID, type, visitID, testID, patientID, resultDate, company, doctorID, status, datePrescribed, pharmacy, medication, duration)
VALUES
    (1, 'Medication', 1, NULL, 1, '2023-02-10', 'PharmaCare', 1, 'Active', '2023-02-10', 'HealthPharm', 'Aspirin', 7),
    (2, 'Lab Test', 2, 2, 2, '2023-03-15', 'LabHealth', 2, 'Pending', '2023-03-15', NULL, NULL, NULL);

-- HealthRecords Table
INSERT INTO HealthRecords (healthRecordID, familyHistory, allergies, vaxHistory, patientID, doctorID, scriptID)
VALUES
    (1, 'No significant family history', 'Pollen', 'Flu, Hepatitis B', 1, 1, 1),
    (2, 'Heart disease in family', 'Penicillin', 'COVID-19', 2, 2, 2);

-- Message Table
INSERT INTO Message (comID, dateSent, subject, content, patientID, doctorID, coachID)
VALUES
    (1, '2023-02-20', 'Follow-up Appointment', 'Please schedule a follow-up appointment.', 1, 1, NULL),
    (2, '2023-03-25', 'Wellness Program', 'Join our fitness program starting next month!', 2, NULL, 1);

-- InsurancePlan Table
INSERT INTO InsurancePlan (planID, terminationDate, copay, description, repID)
VALUES
    (1, '2023-12-31', 30.00, 'Comprehensive Health Plan', 1),
    (2, '2023-11-30', 20.00, 'Basic Coverage', 2);

-- BillingRecord Table
INSERT INTO BillingRecord (billingRecordID, description, amount, patientID, planID)
VALUES
    (1, 'Consultation Fee', 50.00, 1, 1),
    (2, 'Lab Test Charge', 25.00, 2, 2);

-- WellnessRecord Table
INSERT INTO WellnessRecord (wellnessRecordID, goal, description, coachID)
VALUES
    (1, 'Weight Loss', 'Achieve a healthy weight through diet and exercise.', 1),
    (2, 'Stress Management', 'Learn techniques to manage stress and improve mental well-being.', 2);

-- AllergyRecord Table
INSERT INTO AllergyRecord (healthRecordID, allergies)
VALUES
    (1, 'Pollen, Dust'),
    (2, 'Penicillin, Peanuts');

-- VaxHistoryRecord Table
INSERT INTO vaxHistoryRecord (healthRecordID, vaxHistory)
VALUES
    (1, 'Flu, Hepatitis B'),
    (2, 'COVID-19, Influenza');

-- Notifications Table
INSERT INTO Notifications (notificationID, content, status, timeSent, patientID, visitID, testID)
VALUES
    (1, 'Your lab results are ready.', 'Unread', '2023-02-15 08:00:00', 1, NULL, NULL),
    (2, 'Upcoming appointment reminder.', 'Unread', '2023-03-15 10:30:00', 2, 2, NULL);

