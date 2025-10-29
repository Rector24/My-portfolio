-- Insert Drivers
INSERT INTO Driver (Name, Age, Contact, LicenseNumber) 
VALUES 
    ('John Davis', 35, 'john.davis@example.com', 'DL123456'),
    ('Sarah Wilson', 28, 'sarah.wilson@example.com', 'DL789012');

-- Insert IoT Anti-Sleep Devices
INSERT INTO Device (Type, SerialNumber, DriverID, FirmwareVersion, LastCalibrationDate) 
VALUES 
    ('AntiSleepGlasses', 'ASG-2024-001', 1, 'v2.1.4', '2024-01-15'),
    ('DashboardCamera', 'DCM-2024-001', 1, 'v1.2.0', '2024-01-10');

-- Insert Sensor Readings with enhanced metrics
INSERT INTO SensorReading (DeviceID, Timestamp, EyeBlinkDuration, HeadTiltAngle, EyeClosureRatio, PERCLOS_score, IsDrowsy, ConfidenceLevel) 
VALUES 
    (1, '2024-01-20 14:30:00', 0.3, 5.2, 0.1, 8.5, 0, 0.92),
    (1, '2024-01-20 14:35:00', 2.8, 28.7, 0.8, 78.2, 1, 0.96);

-- Insert Alerts
INSERT INTO Alert (ReadingID, Timestamp, Type, Severity, Message) 
VALUES 
    (2, '2024-01-20 14:35:05', 'AudioAlert', 'High', 'Drowsiness detected - PERCLOS score 78.2%'),
    (2, '2024-01-20 14:35:10', 'Vibration', 'High', 'Immediate attention required');

-- Insert Vehicle
INSERT INTO Vehicle (Model, LicensePlate, DeviceID, Year, LastMaintenanceDate) 
VALUES ('Tesla Model 3', 'CA-ABC123', 2, 2023, '2024-01-05');