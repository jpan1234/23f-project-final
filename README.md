# CS 3200 Final Project: HuskyHealth

**HuskyHealth: Your Personal Health Record Hub for Northeastern University**

Welcome to HuskyHealth, a comprehensive Personal Health Record (PHR) System meticulously crafted for the Northeastern University community. Built on robust REST APIs and MySQL, this Appsmith-powered app integrates with university health services to empower students, faculty, and staff in managing their health information securely.

**Key Features:**
- **User-Friendly Interface:** Tailored for diverse users, including patients, doctors, insurance representatives, and wellness coaches.
- **Centralized Health Management:** Access and manage medical histories, medications, and wellness assistance in one digital hub.
- **Appointment Streamlining:** Schedule health consultations, counseling sessions, and wellness check-ups directly through the platform.
- **Personalized Wellness Education:** Tailored content, from stress management strategies to nutrition tips, promoting proactive health practices.

**User Personas Include but Aren't Limited To::**
- **Patients:** Access health records, prescriptions, allergies, and vaccination records. Schedule visits and receive timely reminders.
- **Doctors:** Manage patient appointments, access health records, and engage in secure communication.
- **Insurance Representatives:** Streamline information access for efficient claim processing.
- **Wellness Coaches:** Schedule visits, provide guidance, and enhance user wellness education.

Experience the future of healthcare management at Northeastern University with HuskyHealth—your reliable partner in fostering a healthy and connected community.

A video link explaining our routes and a short demo of our app!
https://drive.google.com/file/d/1MFKvSpSgVW_cDPoLeq16ZSPs7ivI_jD9/view?usp=sharing


## This repo contains a setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for database access
2. A Python Flask container to implement REST APIs
3. A Local AppSmith Server to access the HuskyHealthApp

## How to setup and start the containers to launch the app
**Important** - you need Docker Desktop installed

1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
2. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the non-root user named webapp. 
3. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
4. Build the images with `docker compose build`
5. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 
6. Open up Appsmith using `localhost:8080`
7. Enjoy the capabilities of the app!



