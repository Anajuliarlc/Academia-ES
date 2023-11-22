USE dbacademychi;

INSERT INTO User (IdUser, UserName, BirthDate, CPF, RG, UserPassword)
VALUES
(1, 'John Doe', '1990-05-15', 12345678901, 987654321, 'password123'),
(2, 'Jane Smith', '1985-08-22', 23456789012, 876543210, 'testpass'),
(3, 'Adam Smith', '1985-08-22', 23456789015, 876543210, 'testpass'),
(4, 'Eve Smith', '1985-08-22', 23456789016, 876543210, 'testpass');
-- Adicione mais linhas conforme necessário

-- Inserindo dados fictícios na tabela Teacher
INSERT INTO Teacher (IdUser, EntryHour, ExitHour)
VALUES
(1, '08:00:00', '16:00:00'),
(2, '09:00:00', '17:00:00');
-- Adicione mais linhas conforme necessário

INSERT INTO Student (IdUser, PhoneNumber, State, City, Neighbourdhood, RegistrationDate, MedicalData)
VALUES
(3, 9876543210, 'CA', 'Los Angeles', 'Downtown', '2022-01-10', 'No medical conditions'),
(4, 8765432109, 'NY', 'New York', 'Midtown', '2022-02-15', 'Allergic to pollen');
-- Adicione mais linhas conforme necessário

-- Inserindo dados fictícios na tabela Exercise
INSERT INTO Exercise (IdUser, ExerciseName, SerNum, RepNum, WeightExercise)
VALUES
(3, 'Jogging', 3, 10, 20.0),
(4, 'Weightlifting', 4, 12, 20.0);
-- Adicione mais linhas conforme necessário

-- Inserindo dados fictícios na tabela Measurements
INSERT INTO Measurements (IdUser, MeasDate, Weight, Height, HighWaist, LowWaist, Bust, Biceps, Thigh)
VALUES
(3, '2022-03-01', 70.5, 175, 80, 70, 95, 30, 55),
(4, '2022-03-01', 65.2, 162, 75, 65, 88, 28, 50);
-- Adicione mais linhas conforme necessário

-- Inserindo dados fictícios na tabela Class
INSERT INTO Class (IdUser, ClassName, ClassDate, ClassDescriprion, StudentsMax)
VALUES
(1, 'Yoga Class', '2022-04-05 14:30:00', 'Relaxation and flexibility exercises', 15),
(2, 'High-Intensity Training', '2022-04-10 15:30:00', 'Intense workout for strength and endurance', 20);
-- Adicione mais linhas conforme necessário

-- Inserindo dados fictícios na tabela Goal
INSERT INTO Goal (IdUser, CardioMin, GoalWeight, GoalDate, FinalDate, LeanMassPct, FatPct)
VALUES
(3, 30, 65.0, '2022-05-01', '2022-07-01', 20.0, 15.0),
(4, 20, 60.0, '2022-05-01', '2022-08-01', 18.0, 12.0);
-- Adicione mais linhas conforme necessário

-- Inserindo dados fictícios na tabela Card
INSERT INTO Card (IdUser, ValidityDate, CardHolderName, CardNum, CVV, CardType)
VALUES
(3, '2023-12-31', 'John Doe', 1234567890123456, 123, 'Visa'),
(4, '2023-12-31', 'Jane Smith', 9876543210987654, 456, 'MasterCard');
-- Adicione mais linhas conforme necessário

-- Inserindo dados fictícios na tabela Take
INSERT INTO Take (IdStudent, IdClass, IdTeacher)
VALUES
(3, 1, 1),
(4, 2, 2);
