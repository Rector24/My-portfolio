CREATE OR ALTER PROCEDURE LogReadingAndAlert
    @DeviceID INT,
    @EyeBlinkDuration FLOAT,
    @HeadTiltAngle FLOAT,
    @EyeClosureRatio FLOAT,
    @PERCLOS_score FLOAT,
    @ConfidenceLevel FLOAT = 0.9
AS
BEGIN
    SET NOCOUNT ON;
    
    BEGIN TRANSACTION;
    BEGIN TRY
        DECLARE @ReadingID INT;
        DECLARE @IsDrowsy BIT = 0;
        DECLARE @AlertMessage NVARCHAR(255);
        
        -- Determine drowsiness based on industry standards (PERCLOS > 40% indicates drowsiness)
        IF @PERCLOS_score > 40.0 AND @ConfidenceLevel > 0.7
            SET @IsDrowsy = 1;
        
        INSERT INTO SensorReading (
            DeviceID, Timestamp, EyeBlinkDuration, HeadTiltAngle, 
            EyeClosureRatio, PERCLOS_score, IsDrowsy, ConfidenceLevel
        )
        VALUES (
            @DeviceID, GETDATE(), @EyeBlinkDuration, @HeadTiltAngle,
            @EyeClosureRatio, @PERCLOS_score, @IsDrowsy, @ConfidenceLevel
        );
        
        SET @ReadingID = SCOPE_IDENTITY();

        -- Create alert if drowsy
        IF @IsDrowsy = 1
        BEGIN
            SET @AlertMessage = CONCAT('Drowsiness detected: PERCLOS ', 
                                     CAST(@PERCLOS_score AS NVARCHAR(10)), 
                                     '%, Confidence: ', 
                                     CAST(@ConfidenceLevel * 100 AS NVARCHAR(10)), '%');
            
            INSERT INTO Alert (ReadingID, Timestamp, Type, Severity, Message)
            VALUES (
                @ReadingID, 
                GETDATE(), 
                'AudioAlert', 
                CASE 
                    WHEN @PERCLOS_score > 70 THEN 'Critical'
                    WHEN @PERCLOS_score > 50 THEN 'High'
                    ELSE 'Medium'
                END,
                @AlertMessage
            );
        END

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH
END;

-- Example execution
EXEC LogReadingAndAlert 
    @DeviceID = 1,
    @EyeBlinkDuration = 3.2,
    @HeadTiltAngle = 32.1,
    @EyeClosureRatio = 0.85,
    @PERCLOS_score = 82.5,
    @ConfidenceLevel = 0.94;