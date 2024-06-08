# Worklog for June

# Week 23 (01/05/2024 - 05/05/2024)

### Date: 04/06/2024

**Task**: Evaluate which changes to the models are worth pursuing in the remaining time. Criteria for changes:
1. Necessity: Is the change essential for core functionality, bug fixes, or project requirements?
2. Impact: Does the change break existing functionality or require significant modifications?
3. Complexity: Can the change be implemented within the remaining time without introducing significant complexity?
4. Performance: Does the change improve performance, such as optimizing database queries?
5. User Experience: Does the change enhance user experience or provide business value?
6. Testing: Can the change be thoroughly tested and validated within the available time?
7. Maintainability: Is the change well-documented and easy to understand for future maintenance?

**Time Spent**: 2.5h

**Objective**: 

**Achievements**:
- updated models with evaluation framework for changes to be made
- updated models with decision on changing model object names from plural to singular
- updated models with decision on installing flake8 to enforce PEP-8 style guide in the code
- updated models with decision on changing variable names to adhere to PEP-8 and using db_column parameter to map the name of the column in the database
- updated models with decision on removing removing string method fields and limiting string methods to 20-30 characters
- updated models.py with 2 lines of whitespaces to adhere to PEP-8 style guide
- updated models by moving docstrings to different lines for improved readability
- updated models with decision on changing object name for CreditNoteResume model
- updated models with decision on removing month and year fields and only using datetime fields as month and year are not needed
- updated models with decision on whether to keep or remove validation methods
- removed obsolete line comment for string methods
- updated models with decision on whether to add a second mixin class for the models to inherit from to avoid code repetition
- removed obsolete comments
- updated models with decision on whether to remove default values for CN_ID and D_ID fields in the Credit Notes model
- removed obsolete comments in CreditNotes model
- updated models with decision on whether to remove default value for CNR_ID in the AcknowledgementRequest model
- removed obsolete comments in Acknowledgement Request model
- added comment on default value for R_ID in Acknowledgement Received model
- updated models with decision on changing the MsgFile in the Acknolwegement Received model to a text field instead of a binary BLOB

**What did I learn?**:

**Blockers**:

**Next Steps**:
- Review refactoring of business logic, services, utils, views and urls. 
- After reviewing existing code, decide on proceeding in the best way with the remaining time. 

---------------------------------------------------------------------------------------

### Date: 05/06/2024

**Task**: 
- Evaluate which changes and refactors are worth pursuing in the remaining time in the following files:
    - services.py
    - urls.py
    - utils.py
    - validations.py 
    - views.py

**Time Spent**: 2.5h

**Objective**: 

**Achievements**:
- updated services.py with decision on whether to keep credit note collection function, make it more generic and/or simply calling objects.filter when needed. 
- updated services file by removing obsolete comments.
- updated services.py with docstring on decison to replace Python function with a direct query in the database.
- updated services.py with docstrings whether functions should be kept or can be replaced with direct queries in the database.
- added docstring on whether totals should be added to creditnoteresume model as fields
- added docstring to generate email content function, consider whether to generate in view layer or service layer
- updated save email content to file function with docstring on whether this function should exist at all
- added docstring to create credit note resume function on changing approach of creating credit note resumes
- added docstring to get credit notes resume emails by month and year to signify it should be deleted
- added docstring to create acknowledgement request function to confirm it is gtg
- added docstrings to increment reminders set and send acknowledgement request email functions
- added docstring to url pattern for review
- added docstring to utils functions
- add docstrings and comments for validation functions that can be removed

**What did I learn?**:

**Blockers**:

**Next Steps**:

---------------------------------------------------------------------------------------

### Date: 06/06/2024

**Task**: 
- Refactor models, services, urls, utils, validations and views. 

**Time Spent**: 2.5h

**Objective**: 

**Achievements**:
- updated models by removing obsolete docstrings on changes that will not be made
- updated services by removing obsolete docstring
- updated business logic with more generic function for collecting credit notes by date instead of by previous month specifically
- removed collect credit notes from previous month function as the same result can be achieved with a queryset filter
- removed obsolete function that can be achieved with a queryset filter
- removed helper function that filters unique dealers from a given queryset of credit notes and replace it with an ORM based filter queryset function
- removed helper functions that group and aggregate credit notes by dealer by ORM QuerySet annotate, count and sum methods
- updated models by renaming credit note resume email object to credit note resume as it is clearer and avoids confusion about what the object is and what it does
- replaced credit note resume email with credit note resume object name in admin file
- removed import of credit note resume model description in business logic
- updated views to not import obsolete helper functions for dashboard view
- added migration for renaming credit note resume email to credit note resume
- updated credit note resume model by removing month and year as these are stored in date issued, removed obsolete date validations and added fields that add totals for each credit note resume
- updated string when integrity error is raised
- updated credit note resume model with missing brackets for total credit notes fields
- updated function that creates credit note resume by removing obsolete helper functions and replacing it with ORM queryset methods
- renamed create credit note resume function by removing email suffix
- removed unneccessary docstrings
- removed obsolete helper function because the same functionality can be achieved with a simple QuerySet method
- removed function that increments acknowledgement request tracker as this can be done when email is being sent
- updated increment sending to comment for now
- updated instance creation functions with type hinting for input and return values and put them on top of the script
- updated send acknowledgement email function with a new send email function that supports HTML
- updated function format to make it more readable
- added email base template for acknowledgement requests
- removed email template as python file
- removed obsolete imports into business logic
- removed function to generate email content
- removed function to store email html as file on a fileserver as the email text will be saved in the database in a text field instead
- removed obsolete imports
- added EmailMessage text field to AcknowledgementRequest model to store the html content of the acknowledgement email to be sent
- added docstring regarding why django forces a default value
- updated models with default values requested by django in order to make migrations
- added migrations for adding new fields to models
- removed double login path
- removed obsolete comment from url pattern
- moved login required decorator to views instead of wrapping it around urls
- removed obsolete validation functions
- update views with docstrings on class based views, creating common base.html, dedicated JS files
---------------------------------------------------------------------------------------

### Date: 07/06/2024

**Achievements**:
- updated base html template to serve as the foundation for all oher templates so they can be an extension of the base html template
- updated login html template
- made dashboard template an extension of base html template
- added navigation bar to base html
- removed duplicate vatpat button from navigation bar
- hid navigation bar on login screen
- removed duplicate VATPAT text in nav bar
- removed duplicate log out button from base html template
- updated login html template so user sees navigation bar when logged in
- added colour overlay on top of navigation bar buttons
- raised navigation bar to the same height as VATPAT header
- updated navigation bar button names to be more descriptive and succint
- moved credit notes last month title in navigation header when user is present on the page
- reduced margin between table and navigation bar
- updated acknowledgements dashboard so it is an extension of base html template
- update base html template so navigation bar buttons do not show when logged out
---------------------------------------------------------------------------------------

### Date: 08/06/2024
- moved custom JavaScript to static folder
- replaced custom inline javascript with javascript in static
- added comment for future staticfiles
- extends tag must be the first tag in the Django template, even before {% load static %}

**Next Steps**:
- download Bootstrap CSS and JS locally and place it in static