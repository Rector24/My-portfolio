-- Recent drowsiness events with details
SELECT 
    D.Name AS DriverName,
    DEV.SerialNumber,
    SR.Timestamp,
    SR.PERCLOS_score,
    SR.ConfidenceLevel,
    A.Type AS AlertType,
    A.Severity,
    A.Message
FROM SensorReading SR
INNER JOIN Device DEV ON SR.DeviceID = DEV.DeviceID
INNER JOIN Driver D ON DEV.DriverID = D.DriverID
LEFT JOIN Alert A ON SR.ReadingID = A.ReadingID
WHERE SR.IsDrowsy = 1 
    AND SR.Timestamp >= DATEADD(DAY, -30, GETDATE())
ORDER BY SR.Timestamp DESC;

-- Driver performance summary
SELECT 
    D.Name,
    D.LicenseNumber,
    COUNT(SR.ReadingID) AS TotalReadings,
    SUM(CASE WHEN SR.IsDrowsy = 1 THEN 1 ELSE 0 END) AS DrowsyEvents,
    AVG(SR.PERCLOS_score) AS AvgPERCLOS,
    MAX(SR.PERCLOS_score) AS MaxPERCLOS,
    COUNT(A.AlertID) AS TotalAlerts
FROM Driver D
LEFT JOIN Device DEV ON D.DriverID = DEV.DriverID
LEFT JOIN SensorReading SR ON DEV.DeviceID = SR.DeviceID
LEFT JOIN Alert A ON SR.ReadingID = A.ReadingID
WHERE SR.Timestamp >= DATEADD(DAY, -7, GETDATE())
GROUP BY D.DriverID, D.Name, D.LicenseNumber
ORDER BY DrowsyEvents DESC;

-- Alert analysis and trends
WITH AlertStats AS (
    SELECT 
        Type,
        Severity,
        COUNT(*) AS AlertCount,
        AVG(CASE WHEN Severity = 'Critical' THEN 1.0 ELSE 0.0 END) * 100 AS CriticalPercentage
    FROM Alert 
    WHERE Timestamp >= DATEADD(DAY, -7, GETDATE())
    GROUP BY Type, Severity
)
SELECT 
    Type,
    Severity,
    AlertCount,
    CriticalPercentage,
    CASE 
        WHEN Severity = 'Critical' THEN 'Immediate Intervention Required'
        WHEN Severity = 'High' THEN 'Close Monitoring Needed'
        ELSE 'Routine Attention'
    END AS ActionRequired
FROM AlertStats
ORDER BY Severity DESC, AlertCount DESC;

-- Device performance and calibration status
SELECT 
    DEV.SerialNumber,
    DEV.Type,
    DEV.FirmwareVersion,
    DEV.LastCalibrationDate,
    DATEDIFF(DAY, DEV.LastCalibrationDate, GETDATE()) AS DaysSinceCalibration,
    COUNT(SR.ReadingID) AS ReadingsToday,
    SUM(CASE WHEN SR.IsDrowsy = 1 THEN 1 ELSE 0 END) AS DrowsyDetectionsToday
FROM Device DEV
LEFT JOIN SensorReading SR ON DEV.DeviceID = SR.DeviceID 
    AND SR.Timestamp >= CAST(GETDATE() AS DATE)
WHERE DEV.IsActive = 1
GROUP BY DEV.DeviceID, DEV.SerialNumber, DEV.Type, DEV.FirmwareVersion, DEV.LastCalibrationDate
ORDER BY DaysSinceCalibration DESC;