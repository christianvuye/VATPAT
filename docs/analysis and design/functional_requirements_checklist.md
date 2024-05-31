# Functional Requirements Document for "VAT Protocols Acknowledgement Tracker" (VATPAT)

## 1. User Management
### a. User Authentication:
- [X] Users should log in using a username and password.
- [X] The system should support only two user accounts: ‘business’ and ‘power user’.

### b. User Logout:
- [ ] Users should be able to log out from the system.

### c. Dashboard for Users:
- [ ] Users should view a real-time status of all acknowledgements.
- [ ] Users should view the communication history with dealers, including reminders sent and KPIs tracking dealer performance.
- [ ] Users should retrieve and view stored acknowledgement sheets or e-mail replies with acknowledgements from dealers.

### d. Power User Control:
- [ ] Power users should override the automated system if errors are detected.

## 2. Credit Note Management
### a. Collect List of Credit Notes:
- [X] Retrieve all credit notes issued to Dealers from the Navision database in the past month.

### b. Generate Credit Notes Resume Table:
- [X] The system should produce a Credit Notes Resume table for each dealer.

### c. Send Credit Notes Resume:
- [ ] Email the Credit Notes Resume table to dealers.

### d. Track Credit Notes Resume:
- [ ] Monitor whether dealers have responded to the Credit Notes Resume email appropriately.

### e. Send Reminders for Acknowledgements:
- [ ] If no acknowledgement is received after 7 days, send an automated reminder to the Dealer.

## 3. VAT Protocol Acknowledgement Tracking
### a. Generation of Acknowledgement Sheets:
- [X] Generate VAT protocol acknowledgement sheets for issued credit notes.

### b. Sending Acknowledgement Sheets:
- [ ] Email the generated sheets to Dealers.

### c. Tracking of Acknowledgements:
- [ ] Track the status of each sent acknowledgement sheet.
- [ ] If acknowledgements are not returned, send automated reminders.

## 4. Dealer Communication
### a. Monthly Summaries:
- [ ] Send monthly summaries of credit notes and VAT to Dealers.
- [ ] Use the existing shared email address: hp.finance@honda-eu.com to communicate.
- [ ] Record dealer replies by tracking replies to the email.

## 5. Record Keeping and Compliance
### a. Storage of Acknowledgements:
- [ ] Store all signed VAT protocol acknowledgement sheets securely for 10 years.
- [ ] Record and store replies from Dealers in a secure file storage system.

## 6. System Setup and Integration
### a. System Environment:
- [X] VATPAT should be a web-based application.
- [ ] It will fetch data from the Navision database and run from a local server EHEINWNAV03SP, which also hosts Microsoft Dynamics Business Central – Navision.

### b. Integration Points:
- [X] Integrate with the existing Navision database to fetch credit note information.
- [ ] Integrate with an email system for sending out reminders, summaries, and tracking acknowledgements.
- [ ] Integrate with a secure file storage system for record-keeping.