-- Backup Scripts
BACKUP DATABASE MacysPizza
TO DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\Backup\MacysPizza.bak';
GO

BACKUP DATABASE MacysPizza
TO DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\Backup\MacysPizza.bak'
WITH DIFFERENTIAL;
GO

BACKUP DATABASE MacysPizza
FILEGROUP = 'SecondaryFG'
TO DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\Backup\MacysPizza.bak';
GO