Lessons for next Django project: 

Evaluate suggested changes to the models to be made by the following criteria:
1. Necessity: Is the change essential for core functionality, bug fixes, or project requirements?
2. Impact: Does the change break existing functionality or require significant modifications?
3. Complexity: Can the change be implemented within the remaining time without introducing significant complexity?
4. Performance: Does the change improve performance, such as optimizing database queries?
5. User Experience: Does the change enhance user experience or provide business value?
6. Testing: Can the change be thoroughly tested and validated within the available time?
7. Maintainability: Is the change well-documented and easy to understand for future maintenance?

- PIP Install Flake8 to enforce PEP-8 style guide in the code.
- Classes that refer to one object, such as a dealer, should be singular. Therefore, the class name should be Dealer instead of Dealers. CreditNotes should be CreditNote.
- By PEP-8 standards, variable names should be lowercase with underscores between words. To maintain the PEP-8 standard, use the db_column parameter to map to the name of the column in the database.
- String methods should only return the most important fields, not all of them. The character limit for the string method should be around 20-30 characters.
- Model your objects in an object oriented way to define their methods and so on. See university books.
- The name of the object is CreditNoteResume, so the class name should be CreditNoteResume instead of CreditNoteResumeEmail. 
- A Django model is a Python class. Python classes can inherit from multiple parent classes. A Mixin class is a class that can be used to avoid repeating the same code in multiple classes.
- The field DateIssued is a DateTimeField, so the fields Month and Year are redundant. Instead of having separate fields for Month and Year, use a single DateIssued field with the date of the credit note. If you use Month and Year, you will need to convert them to a date format when doing operations on these fields. 
- Store emails as text values, not as BLOB. A BLOB is for images. 
- Add type hints to the functions and make them more generic. Avoid hardcoding model names and field names in the functions.
- Make functions more pure by removing print statements and side effects. Instead, return the data and let the caller decide what to do with it.
- Avoid using global variables in functions. Pass the required data as arguments to the functions.
- Avoid HTML formatting in Python code. Instead, use templates to generate HTML content.
- Use Querys instead of Python functions for aggregations where possible. 


    