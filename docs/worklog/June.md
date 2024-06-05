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