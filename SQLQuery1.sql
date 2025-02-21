ALTER DATABASE MacysPizza ADD FILEGROUP SecondaryFG;
GO
ALTER DATABASE MacysPizza ADD FILE (
    NAME = 'SecondaryFile',
    FILENAME = 'C:\SQLData\SecondaryFile.ndf'
) TO FILEGROUP SecondaryFG;
GO