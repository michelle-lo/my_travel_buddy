CREATE TABLE [dbo].[User]
(
  [Id] INT IDENTITY(1000,1) NOT NULL PRIMARY KEY,
  [Username] NVARCHAR(50) NOT NULL,
  [FirstName] NVARCHAR(50) NOT NULL,
  [LastName] NVARCHAR(50) NOT NULL,
  [Email] NVARCHAR(50) NOT NULL,
  [Password] NVARCHAR(50) NOT NULL,
)
