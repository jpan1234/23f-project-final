
-- creating database HuskyHealth
CREATE DATABASE IF NOT EXISTS HuskyHealth;

-- use the database
USE HuskyHealth;

CREATE USER IF NOT EXISTS 'webapp'@'%';

-- grant privileges
GRANT ALL PRIVILEGES ON HuskyHealth.* to 'webapp'@'%';

FLUSH PRIVILEGES;

-- creating the Patient table
CREATE TABLE IF NOT EXISTS Patient
(
    patientID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    birthDate DATE NOT NULL,
    age INT
);

-- updating the age to be the timestamp difference between birth date and current date
UPDATE Patient SET age = TIMESTAMPDIFF(YEAR, birthDate, CURDATE());

-- creating the Doctor table
CREATE TABLE IF NOT EXISTS Doctor (
    doctorID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    specialization VARCHAR(255) NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    consent TINYINT(1) DEFAULT 1 NOT NULL
);

-- creating WellnessCoach table
CREATE TABLE IF NOT EXISTS WellnessCoach (
    coachID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    education VARCHAR(255) NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    consent TINYINT(1) DEFAULT 0 NOT NULL
);

-- creating InsuranceRepresentative table
CREATE TABLE IF NOT EXISTS InsuranceRepresentative (
    repID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    company VARCHAR(255) NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    consent TINYINT(1) DEFAULT 0 NOT NULL
);

-- creating Visit table
CREATE TABLE IF NOT EXISTS Visit (
    visitID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    purpose VARCHAR(255) NOT NULL,
    visitDate DATE NOT NULL,
    patientID INT NOT NULL,
    doctorID INT,
    coachID INT,
    canceled TINYINT(1) DEFAULT 0 NOT NULL,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (coachID) REFERENCES WellnessCoach(coachID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- creating LabResults table
CREATE TABLE IF NOT EXISTS LabResults (
    testID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    result TEXT NOT NULL,
    type VARCHAR(255) NOT NULL,
    testDate DATE NOT NULL,
    patientID INT NOT NULL,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- creating Prescriptions table
CREATE TABLE IF NOT EXISTS Prescriptions (
    scriptID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    type VARCHAR(255) NOT NULL,
    visitID INT,
    testID INT,
    patientID INT NOT NULL,
    resultDate DATE NOT NULL,
    company VARCHAR(255) NOT NULL,
    doctorID INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    datePrescribed DATE NOT NULL,
    pharmacy VARCHAR(255) NOT NULL,
    medication VARCHAR(255) NOT NULL,
    duration INT NOT NULL,
    inactive TINYINT(1) DEFAULT 0 NOT NULL,
    FOREIGN KEY (visitID) REFERENCES Visit(visitID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (testID) REFERENCES LabResults(testID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- creating HealthRecords table
CREATE TABLE IF NOT EXISTS HealthRecords (
    healthRecordID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    familyHistory TEXT NOT NULL,
    allergies TEXT NOT NULL,
    vaxHistory TEXT NOT NULL,
    patientID INT NOT NULL,
    doctorID INT,
    repID INT,
    coachID INT,
    scriptID INT,
    complete TINYINT(1) DEFAULT 0 NOT NULL,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (repID) REFERENCES InsuranceRepresentative(repID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (coachID) REFERENCES WellnessCoach(coachID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (scriptID) REFERENCES Prescriptions(scriptID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- creating Message table
CREATE TABLE IF NOT EXISTS Message (
    comID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    dateSent DATE,
    subject VARCHAR(255),
    content TEXT,
    patientID INT,
    doctorID INT,
    coachID INT,
    repID INT,
    deleted TINYINT(1) DEFAULT 0 NOT NULL,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (coachID) REFERENCES WellnessCoach(coachID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (repID) REFERENCES InsuranceRepresentative(repID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- creating InsurancePLan table
CREATE TABLE IF NOT EXISTS InsurancePlan (
    planID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    terminationDate DATE,
    copay DECIMAL,
    description TEXT,
    repID INT,
    inactive TINYINT(1) DEFAULT 0 NOT NULL,
    FOREIGN KEY (repID) REFERENCES InsuranceRepresentative(repID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- creating BillingRecord table
CREATE TABLE IF NOT EXISTS BillingRecord (
    billingRecordID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    description TEXT,
    amount DECIMAL,
    patientID INT NOT NULL,
    planID INT,
    paid TINYINT(1) DEFAULT 0 NOT NULL,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (planID) REFERENCES InsurancePlan(planID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- creating WellnessRecord table
CREATE TABLE IF NOT EXISTS WellnessRecord (
    wellnessRecordID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    goal VARCHAR(255),
    description TEXT,
    patientID INT NOT NULL,
    complete TINYINT(1) DEFAULT 0 NOT NULL,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- creating AllergyRecord table
CREATE TABLE IF NOT EXISTS AllergyRecord (
    healthRecordID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    allergies TEXT,
    FOREIGN KEY (healthRecordID) REFERENCES HealthRecords(healthRecordID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- creating vaxhistoryRecord table
CREATE TABLE IF NOT EXISTS vaxHistoryRecord (
    healthRecordID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    vaxHistory TEXT,
    FOREIGN KEY (healthRecordID) REFERENCES HealthRecords(healthRecordID) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- creating Notifications table
CREATE TABLE IF NOT EXISTS Notifications (
    notificationID INT PRIMARY KEY NOT NULL,
    content TEXT,
    status VARCHAR(50),
    timeSent TIMESTAMP,
    patientID INT NOT NULL,
    visitID INT,
    testID INT,
    deleted TINYINT(1) DEFAULT 0 NOT NULL,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (visitID) REFERENCES Visit(visitID) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (testID) REFERENCES LabResults(testID) ON UPDATE CASCADE ON DELETE RESTRICT
);


-- Drop all tables in reverse order to avoid foreign key constraint issues
DROP TABLE IF EXISTS Notifications;
DROP TABLE IF EXISTS vaxHistoryRecord;
DROP TABLE IF EXISTS AllergyRecord;
DROP TABLE IF EXISTS WellnessRecord;
DROP TABLE IF EXISTS BillingRecord;
DROP TABLE IF EXISTS InsurancePlan;
DROP TABLE IF EXISTS Message;
DROP TABLE IF EXISTS HealthRecords;
DROP TABLE IF EXISTS Prescriptions;
DROP TABLE IF EXISTS LabResults;
DROP TABLE IF EXISTS Visit;
DROP TABLE IF EXISTS InsuranceRepresentative;
DROP TABLE IF EXISTS WellnessCoach;
DROP TABLE IF EXISTS Doctor;
DROP TABLE IF EXISTS Patient;
