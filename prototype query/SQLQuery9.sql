CREATE OR ALTER VIEW DashboardSummary AS
SELECT
    D.Name AS DriverName,
    D.LicenseNumber,
    V.Model AS VehicleModel,
    V.LicensePlate,
    DEV.Type AS DeviceType,
    DEV.SerialNumber,
    COUNT(DISTINCT A.AlertID) AS TotalAlerts,
    SUM(CASE WHEN A.Severity = 'Critical' THEN 1 ELSE 0 END) AS CriticalAlerts,
    SUM(CASE WHEN SR.IsDrowsy = 1 THEN 1 ELSE 0 END) AS DrowsyEvents,
    MAX(SR.Timestamp) AS LastReadingTime
FROM Driver D
INNER JOIN Device DEV ON D.DriverID = DEV.DriverID
LEFT JOIN Vehicle V ON DEV.DeviceID = V.DeviceID
LEFT JOIN SensorReading SR ON DEV.DeviceID = SR.DeviceID
LEFT JOIN Alert A ON SR.ReadingID = A.ReadingID
WHERE D.IsActive = 1 AND DEV.IsActive = 1
GROUP BY D.DriverID, D.Name, D.LicenseNumber, V.Model, V.LicensePlate, DEV.Type, DEV.SerialNumber;

-- Usage
SELECT * FROM DashboardSummary ORDER BY CriticalAlerts DESC;