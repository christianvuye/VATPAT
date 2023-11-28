# VAT Protocols Acknowledgement Tracker (VATPAT)

## Introduction
VATPAT is a web-based Django application designed to manage and automate the tracking of VAT protocol acknowledgements, streamline communications with dealers, and ensure proper record-keeping and compliance.

### User Management
- **User Authentication**: Support for two user accounts - ‘business’ and ‘power user’. Users log in with username and password.
- **Dashboard for Users**: Display real-time status of all acknowledgements, communication history with dealers, and view stored acknowledgement sheets or e-mail replies.
- **Power User Control**: Power users can override the automated system in case of errors.

### Credit Note Management
- **Collect List of Credit Notes**: Retrieve credit notes from the VATPAT database for the past month.
- **Generate Credit Notes Resume Table**: Produce a Credit Notes Resume table for each dealer.
- **Send Credit Notes Resume**: Automatically email the Credit Notes Resume table to dealers the past month sing the email address hp.finance@honda-eu.com. 
- **Track Credit Notes Resume**: Monitor dealer responses to the Credit Notes Resume email.
- **Send Reminders for Acknowledgements**: Send automated reminders after 7 days of no acknowledgement.

### Record Keeping and Compliance
- **Storage of Acknowledgements**: Securely store all signed VAT protocol acknowledgement sheets for 10 years.

### System Setup and Integration
- **System Environment**: VATPAT will run from a local server (EHEINWNAV03SP) and fetch data from the Navision database.
- **Integration Points**: Integrate with VATPAT database, an email system for reminders and tracking, and a secure file storage system for record-keeping.
