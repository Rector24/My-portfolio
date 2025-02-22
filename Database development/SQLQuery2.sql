INSERT INTO Members (MemberID, Name, Email, Phone, MembershipType) VALUES
(1, 'Alice Johnson', 'alice.johnson@example.com', '123-456-7890', 'Premium'),
(2, 'Bob Smith', 'bob.smith@example.com', '234-567-8901', 'Basic'),
(3, 'Charlie Brown', 'charlie.brown@example.com', '345-678-9012', 'Premium'),
(4, 'Diana Prince', 'diana.prince@example.com', '456-789-0123', 'Basic'),
(5, 'Ethan Hunt', 'ethan.hunt@example.com', '567-890-1234', 'Family');

INSERT INTO Trainers (TrainerID, Name, Specialty, ContactInfo) VALUES
(1, 'John Doe', 'Cardio', 'john.doe@example.com'),
(2, 'Jane Smith', 'Strength Training', 'jane.smith@example.com'),
(3, 'Mike Tyson', 'Boxing', 'mike.tyson@example.com'),
(4, 'Sarah Connor', 'Yoga', 'sarah.connor@example.com');

INSERT INTO Classes (ClassID, ClassName, Schedule, TrainerID, MaxCapacity) VALUES
(1, 'Morning Yoga', '2024-10-22 08:00:00', 4, 20),
(2, 'Cardio Blast', '2024-10-22 09:00:00', 1, 30),
(3, 'Strength Training', '2024-10-22 10:00:00', 2, 25),
(4, 'Boxing Basics', '2024-10-22 11:00:00', 3, 15);

INSERT INTO Payments (PaymentID, MemberID, Date, Amount, PaymentMethod) VALUES
(1, 1, '2024-10-01', 100.00, 'Credit Card'),
(2, 2, '2024-10-05', 50.00, 'Cash'),
(3, 3, '2024-10-10', 100.00, 'Debit Card'),
(4, 4, '2024-10-15', 50.00, 'Credit Card'),
(5, 5, '2024-10-20', 150.00, 'Bank Transfer');

INSERT INTO Feedback (FeedbackID, MemberID, FeedbackText, Rating, FeedbackDate) VALUES
(1, 1, 'Great classes and trainers!', 5, '2024-10-21'),
(2, 2, 'I enjoy the atmosphere.', 4, '2024-10-20'),
(3, 3, 'The boxing class was intense!', 5, '2024-10-19'),
(4, 4, 'Yoga sessions are relaxing.', 4, '2024-10-18'),
(5, 5, 'Need more equipment in the gym.', 3, '2024-10-17');

INSERT INTO Bookings (BookingID, MemberID, ClassID, BookingDate) VALUES
(1, 1, 1, '2024-10-21'),
(2, 2, 2, '2024-10-20'),
(3, 3, 3, '2024-10-19'),
(4, 4, 4, '2024-10-18'),
(5, 5, 1, '2024-10-17');

INSERT INTO Equipment (EquipmentID, EquipmentName, PurchaseDate, Condition) VALUES
(1, 'Treadmill', '2023-01-10', 'Good'),
(2, 'Dumbbells', '2023-02-15', 'New'),
(3, 'Yoga Mats', '2023-03-20', 'Used'),
(4, 'Punching Bag', '2023-04-25', 'Good');


INSERT INTO Inventory (ItemID, ItemName, Quantity, PurchaseDate, SupplierName) VALUES
(1, 'Protein Powder', 50, '2024-01-01', 'Fitness Supplier Inc.'),
(2, 'Yoga Mats', 30, '2024-01-02', 'Yoga Supplies Co.'),
(3, 'Water Bottles', 100, '2024-01-03', 'Hydration Experts Ltd.'),
(4, 'Resistance Bands', 75, '2024-01-04', 'Strength Gear Co.'),
(5, 'Foam Rollers', 40, '2024-01-05', 'Recovery Supplies Inc.'),
(6, 'Exercise Balls', 25, '2024-01-06', 'Balance Equipment Co.'),
(7, 'Gym Towels', 150, '2024-01-07', 'Towel Supply Co.'),
(8, 'Kettlebells', 35, '2024-01-08', 'Weight Gear Inc.'),
(9, 'Medicine Balls', 45, '2024-01-09', 'Fitness Tools Ltd.'),
(10, 'Heart Rate Monitors', 20, '2024-01-10', 'Tech Health Co.'),
(11, 'Jump Ropes', 80, '2024-01-11', 'Cardio Supplies Inc.'),
(12, 'Foam Mats', 60, '2024-01-12', 'Exercise Equipment Co.'),
(13, 'Exercise Bands', 70, '2024-01-13', 'Stretch Gear Ltd.'),
(14, 'TRX Straps', 25, '2024-01-14', 'Strength Training Co.'),
(15, 'Gloves', 90, '2024-01-15', 'Fitness Apparel Inc.'),
(16, 'Sports Drinks', 120, '2024-01-16', 'Hydration Experts Ltd.'),
(17, 'Jump Boxes', 30, '2024-01-17', 'Plyometric Gear Co.'),
(18, 'Lifting Belts', 40, '2024-01-18', 'Strength Gear Co.'),
(19, 'Foam Blocks', 50, '2024-01-19', 'Yoga Supplies Co.'),
(20, 'Training Cones', 60, '2024-01-20', 'Sports Equipment Inc.');