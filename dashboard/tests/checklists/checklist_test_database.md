# Database-Level Testing

## Purpose
Validate that the database schema correctly enforces integrity constraints like foreign keys, unique constraints, and not null constraints.

## Tools
Use Django's `TestCase` which wraps each test in a transaction and rolls it back at the end of the test, or use tools that allow testing directly against the database's behavior.

## Coverage
Try to insert invalid data directly using Django’s ORM to check if the database rejects these entries as expected.

## Database-Level Cohort

- Develop tests that attempt to bypass Django's validations and manipulate the database directly to ensure constraints are enforced.
- These tests might involve intentionally trying to break constraints to see if the database reacts appropriately.
- Use a real database system that mimics your production environment closely, rather than relying solely on SQLite if your production uses a different DBMS.

# Database Testing Checklist

# Database-Level Testing Checklist for Django Models

## Dealers Model
- [ ] **Unique Constraints**: Test that the `D_ID` field is enforced as unique at the database level.
- [ ] **Primary Key Constraints**: Verify that `D_ID` functions effectively as a primary key in the database.
- [ ] **Data Validation**: Confirm database-level enforcement of valid formats for `DealerVATnumber`, particularly focusing on format constraints that should be handled by the database.
- [ ] **Field Length**: Ensure that database constraints for `max_length` on `DealerName`, `DealerVATnumber`, and `DealerEmail` are respected.
- [ ] **Automatic Date Handling**: Test that `CreatedDate` and `ModifiedDate` are automatically set and updated by the database.
- [ ] **Boolean Defaults**: Check that the database correctly defaults `is_active` to `True`.
- [ ] **Deletion Policy**: Ensure that attempts to delete a `Dealers` record results in an `IntegrityError`, verifying the database-level restriction on deletion.

## CreditNotes Model
- [ ] **Unique Constraints**: Ensure that the `CN_ID` field's uniqueness is enforced by the database.
- [ ] **Primary Key Constraints**: Confirm that `CN_ID` acts as a primary key at the database level.
- [ ] **Foreign Key Constraints**: Test that the `D_ID` correctly establishes a foreign key relationship to the `Dealers` model and enforces referential integrity.
- [ ] **Decimal Fields**: Check the precision and scale enforcement of `DecimalField`s such as `TotalDocumentAmount`, `TotalVATAmountDocumentt`, and `TotalDocumentAmountWithVAT`.
- [ ] **Default Values**: Verify that any default values specified are correctly applied by the database.
- [ ] **Integrity on Dealer Deletion**: Validate that deletion of a `Dealers` record cascades properly to related `CreditNotes`.

## CreditNoteResumeEmail Model
- [ ] **Auto Increment**: Verify that the `CNR_ID` auto-increments correctly in the database.
- [ ] **Foreign Key Constraints**: Ensure that `CN_ID` correctly references the `CreditNotes` model and respects database-level foreign key constraints.
- [ ] **Data Types**: Confirm that data type constraints for fields like `Month` and `Year` are enforced at the database level.
- [ ] **Boolean Fields**: Test the enforcement and default setting of `Status` and `IsValid` by the database.

## AcknowledgementRequest Model
- [ ] **Auto Increment**: Ensure that `R_ID` is auto-incremented and functions as a primary key.
- [ ] **Nullable Foreign Key**: Confirm that `CNR_ID` can be null and properly references `CreditNoteResumeEmail` with appropriate foreign key checks.
- [ ] **Boolean Fields**: Check that the `Status` field behaves as expected based on database rules.
- [ ] **Date Fields**: Validate the correct handling and storage of date fields (`CreatedDate` and `SendDate`) by the database.

## AcknowledgementReceived Model
- [ ] **Auto Increment and Uniqueness**: Test that `A_ID` is auto-incremented and maintained as unique across the database.
- [ ] **Nullable Foreign Key**: Verify that `R_ID` handles null values correctly and establishes a correct foreign key relationship to `AcknowledgementRequest`.
- [ ] **Binary Data**: Ensure that `MsgFile` correctly stores and retrieves binary data, testing the database’s handling of binary field types.


## Test Integrity Constraints
- [ ] Test that primary keys are unique and automatically generated as expected.
- [ ] Test foreign key constraints to ensure referential integrity.
- [ ] Test unique constraints to prevent duplicate entries.
- [ ] Test not null constraints to ensure mandatory fields are populated.

## Test Indexing and Performance
- [ ] Ensure that indexes are properly used for optimizing query performance.
- [ ] Test database queries under load to ensure performance benchmarks are met.

## Test Transactions
- [ ] Test transactional integrity to ensure that transactions are atomic, consistent, isolated, and durable.
- [ ] Test rollback capabilities to ensure data integrity after transaction failures.

## Test Security
- [ ] Test for SQL injection vulnerabilities.
- [ ] Ensure that database access is properly secured with appropriate authentication and authorization.

## Test Backup and Recovery
- [ ] Test backup procedures to ensure data is correctly archived and can be restored.
- [ ] Test recovery from backup to ensure it is complete and effective.

## Test Data Migration
- [ ] Test data migration scripts for accuracy and completeness.
- [ ] Ensure that migrations handle data correctly without loss or corruption.

## Test Scalability
- [ ] Test database scalability to handle increased loads.
- [ ] Test how the database handles large volumes of data.

## Test Failover and Redundancy
- [ ] Test database failover procedures to ensure high availability.
- [ ] Test redundancy mechanisms to ensure data integrity and availability during hardware or software failures.
