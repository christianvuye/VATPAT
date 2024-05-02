CREATE TABLE [CreditNotes] (
  [CN_ID] varchar(20) UNIQUE PRIMARY KEY,
  [D_ID] nvarchar(10),
  [TotalDocumentAmount] decimal(38,20),
  [TotalVATAmountDocumentt] decimal(38,20),
  [TotalDocumentAmountWithVAT] decimal(38,20),
  [AccountingNumberID] nvarchar(30),
  [IssuedDate] datetime
)
GO

CREATE TABLE [Dealers] (
  [D_ID] nvarchar(10) UNIQUE PRIMARY KEY,
  [DealerName] nvarchar(100),
  [DealerVATnumber] nvvarchar(20),
  [DealerEmail] nvarchar(80),
  [CreatedDate] timestamp,
  [ModifiedDate] timestamp
)
GO

CREATE TABLE [CreditNoteResumeEmail] (
  [CNR_ID] integer UNIQUE PRIMARY KEY,
  [CN_ID] nvarchar(10),
  [DateIssued] datetime,
  [Month] integer,
  [Year] integer,
  [Body] nvarchar(MAX),
  [Subject] varchar(40),
  [Status] bool,
  [IsValid] bit
)
GO

CREATE TABLE [AcknowledgementRequest] (
  [R_ID] integer UNIQUE PRIMARY KEY,
  [CNR_ID] integer,
  [Status] bool,
  [CreatedDate] datetime,
  [SendDate] datetime
)
GO

CREATE TABLE [AcknowledgementReceived] (
  [A_ID] integer UNIQUE PRIMARY KEY,
  [R_ID] integer,
  [MsgFile] varbinary(max)
)
GO

EXEC sp_addextendedproperty
@name = N'Table_Description',
@value = 'List of Credit Notes, copied from Navision DB.',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'CreditNotes';
GO

EXEC sp_addextendedproperty
@name = N'Table_Description',
@value = 'List of dealers, copied from Navision DB.',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'Dealers';
GO

EXEC sp_addextendedproperty
@name = N'Table_Description',
@value = 'Replaces reminder table, tracks all sent messages (incl. email reminders).',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'AcknowledgementRequest';
GO

ALTER TABLE [AcknowledgementReceived] ADD FOREIGN KEY ([R_ID]) REFERENCES [AcknowledgementRequest] ([R_ID])
GO

ALTER TABLE [CreditNotes] ADD FOREIGN KEY ([D_ID]) REFERENCES [Dealers] ([D_ID])
GO

ALTER TABLE [CreditNotes] ADD FOREIGN KEY ([CN_ID]) REFERENCES [CreditNoteResumeEmail] ([CN_ID])
GO

ALTER TABLE [AcknowledgementRequest] ADD FOREIGN KEY ([CNR_ID]) REFERENCES [CreditNoteResumeEmail] ([CNR_ID])
GO
