-- Create Tables for IoT Anti-Sleep Glasses System
CREATE TABLE Driver (
    DriverID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Age INT CHECK (Age >= 18 AND Age <= 80),
    Contact NVARCHAR(100),
    LicenseNumber NVARCHAR(20),
    IsActive BIT DEFAULT 1,
    CreatedDate DATETIME2 DEFAULT GETDATE()
);

CREATE TABLE Device (
    DeviceID INT IDENTITY(1,1) PRIMARY KEY,
    Type NVARCHAR(50) NOT NULL CHECK (Type IN ('AntiSleepGlasses', 'DashboardCamera', 'SteeringWheelSensor')),
    SerialNumber NVARCHAR(50) UNIQUE NOT NULL,
    DriverID INT NOT NULL,
    FirmwareVersion NVARCHAR(20),
    LastCalibrationDate DATETIME2,
    IsActive BIT DEFAULT 1,
    FOREIGN KEY (DriverID) REFERENCES Driver(DriverID) ON DELETE CASCADE
);

CREATE TABLE SensorReading (
    ReadingID INT IDENTITY(1,1) PRIMARY KEY,
    DeviceID INT NOT NULL,
    Timestamp DATETIME2 NOT NULL,
    EyeBlinkDuration FLOAT CHECK (EyeBlinkDuration >= 0),
    HeadTiltAngle FLOAT,
    EyeClosureRatio FLOAT CHECK (EyeClosureRatio >= 0 AND EyeClosureRatio <= 1),
    PERCLOS_score FLOAT CHECK (PERCLOS_score >= 0 AND PERCLOS_score <= 100),
    IsDrowsy BIT DEFAULT 0,
    ConfidenceLevel FLOAT CHECK (ConfidenceLevel >= 0 AND ConfidenceLevel <= 1),
    FOREIGN KEY (DeviceID) REFERENCES Device(DeviceID) ON DELETE CASCADE
);

CREATE TABLE Alert (
    AlertID INT IDENTITY(1,1) PRIMARY KEY,
    ReadingID INT NOT NULL,
    Timestamp DATETIME2 NOT NULL,
    Type NVARCHAR(50) NOT NULL CHECK (Type IN ('AudioAlert', 'Vibration', 'VisualWarning', 'SystemNotification')),
    Severity NVARCHAR(20) CHECK (Severity IN ('Low', 'Medium', 'High', 'Critical')),
    Message NVARCHAR(255),
    IsAcknowledged BIT DEFAULT 0,
    FOREIGN KEY (ReadingID) REFERENCES SensorReading(ReadingID) ON DELETE CASCADE
);

CREATE TABLE Vehicle (
    VehicleID INT IDENTITY(1,1) PRIMARY KEY,
    Model NVARCHAR(100) NOT NULL,
    LicensePlate NVARCHAR(20) UNIQUE NOT NULL,
    DeviceID INT UNIQUE,
    Year INT,
    LastMaintenanceDate DATETIME2,
    FOREIGN KEY (DeviceID) REFERENCES Device(DeviceID) ON DELETE SET NULL
);

-- Create indexes for better performance
CREATE INDEX IX_SensorReading_Timestamp ON SensorReading(Timestamp);
CREATE INDEX IX_SensorReading_IsDrowsy ON SensorReading(IsDrowsy);
CREATE INDEX IX_Alert_Timestamp ON Alert(Timestamp);
CREATE INDEX IX_Device_DriverID ON Device(DriverID);