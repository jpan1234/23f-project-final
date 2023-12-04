# creating database HuskyHealth
CREATE DATABASE IF NOT EXISTS HuskyHealth;

# use the database
USE HuskyHealth;

# creating the Patient table
CREATE TABLE IF NOT EXISTS Patient
(
    patientID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    birthDate DATE,
    age INT,
    healthRecordConsent TINYINT(1) DEFAULT 0
);

# updating the age to be the timestamp difference between birth date and current date
UPDATE Patient SET age = TIMESTAMPDIFF(YEAR, birthDate, CURDATE());

# creating the Doctor table
CREATE TABLE IF NOT EXISTS Doctor (
    doctorID INT AUTO_INCREMENT PRIMARY KEY,
    specialization VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    healthRecordConsent TINYINT(1) DEFAULT 1
);

# creating WellnessCoach table
CREATE TABLE IF NOT EXISTS WellnessCoach (
    coachID INT AUTO_INCREMENT PRIMARY KEY,
    education VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    healthRecordConsent TINYINT(1) DEFAULT 0
);

# creating InsuranceRepresentative table
CREATE TABLE IF NOT EXISTS InsuranceRepresentative (
    repID INT AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    healthRecordConsent TINYINT(1) DEFAULT 0
);

# creating Visit table
CREATE TABLE IF NOT EXISTS Visit (
    visitID INT AUTO_INCREMENT PRIMARY KEY,
    purpose VARCHAR(255),
    visitDate DATE,
    patientID INT,
    doctorID INT,
    coachID INT,
    canceled TINYINT(1) DEFAULT 0,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (coachID) REFERENCES WellnessCoach(coachID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating LabResults table
CREATE TABLE IF NOT EXISTS LabResults (
    testID INT AUTO_INCREMENT PRIMARY KEY,
    result TEXT,
    type VARCHAR(255),
    testDate DATE
);

# creating Prescriptions table
CREATE TABLE IF NOT EXISTS Prescriptions (
    scriptID INT AUTO_INCREMENT PRIMARY KEY,
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
    inactive TINYINT(1) DEFAULT 0,
    FOREIGN KEY (visitID) REFERENCES Visit(visitID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (testID) REFERENCES LabResults(testID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating HealthRecords table
CREATE TABLE IF NOT EXISTS HealthRecords (
    healthRecordID INT AUTO_INCREMENT PRIMARY KEY,
    familyHistory TEXT,
    allergies TEXT,
    vaxHistory TEXT,
    patientID INT,
    doctorID INT,
    scriptID INT,
    complete TINYINT(1) DEFAULT 0,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (scriptID) REFERENCES Prescriptions(scriptID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating Message table
CREATE TABLE IF NOT EXISTS Message (
    comID INT AUTO_INCREMENT PRIMARY KEY,
    dateSent DATE,
    subject VARCHAR(255),
    content TEXT,
    patientID INT,
    doctorID INT,
    coachID INT,
    repID INT,
    deleted TINYINT(1) DEFAULT 0,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (coachID) REFERENCES WellnessCoach(coachID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (repID) REFERENCES InsuranceRepresentative(repID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating InsurancePLan table
CREATE TABLE IF NOT EXISTS InsurancePlan (
    planID INT AUTO_INCREMENT PRIMARY KEY,
    terminationDate DATE,
    copay DECIMAL,
    description TEXT,
    repID INT,
    inactive TINYINT(1) DEFAULT 0,
    FOREIGN KEY (repID) REFERENCES InsuranceRepresentative(repID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating BillingRecord table
CREATE TABLE IF NOT EXISTS BillingRecord (
    billingRecordID INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT,
    amount DECIMAL,
    patientID INT,
    planID INT,
    paid TINYINT(1) DEFAULT 0,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (planID) REFERENCES InsurancePlan(planID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating WellnessRecord table
CREATE TABLE IF NOT EXISTS WellnessRecord (
    wellnessRecordID INT AUTO_INCREMENT PRIMARY KEY,
    goal VARCHAR(255),
    description TEXT,
    patientID INT,
    complete TINYINT(1) DEFAULT 0,
    FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON UPDATE CASCADE ON DELETE SET NULL
);

# creating AllergyRecord table
CREATE TABLE IF NOT EXISTS AllergyRecord (
    healthRecordID INT AUTO_INCREMENT PRIMARY KEY,
    allergies TEXT,
    FOREIGN KEY (healthRecordID) REFERENCES HealthRecords(healthRecordID) ON UPDATE CASCADE ON DELETE CASCADE
);

# creating vaxhistoryRecord table
CREATE TABLE IF NOT EXISTS vaxHistoryRecord (
    healthRecordID INT AUTO_INCREMENT PRIMARY KEY,
    vaxHistory TEXT,
    FOREIGN KEY (healthRecordID) REFERENCES HealthRecords(healthRecordID) ON UPDATE CASCADE ON DELETE CASCADE
);
