USE dbacademychi;

CREATE TABLE User
(
  IdUser INT NOT NULL AUTO_INCREMENT,
  UserName VARCHAR(255) NOT NULL,
  BirthDate DATE NOT NULL,
  CPF NUMERIC(11) NOT NULL,
  RG NUMERIC(11) NOT NULL,
  UserPassword VARCHAR(255) NOT NULL,
  PRIMARY KEY (IdUser),
  UNIQUE (CPF)
);

CREATE TABLE Teacher
(
  IdUser INT NOT NULL AUTO_INCREMENT,
  EntryHour TIME NOT NULL,
  ExitHour TIME NOT NULL,
  PRIMARY KEY (IdUser),
  FOREIGN KEY (IdUser) REFERENCES User(IdUser)
);

CREATE TABLE Student
(
  IdUser INT NOT NULL AUTO_INCREMENT,
  PhoneNumber NUMERIC(11) NOT NULL,
  State CHAR(2) NOT NULL,
  City VARCHAR(255) NOT NULL,
  Neighbourdhood VARCHAR(255) NOT NULL,
  RegistrationDate DATE NOT NULL,
  MedicalData VARCHAR(800),
  PRIMARY KEY (IdUser),
  FOREIGN KEY (IdUser) REFERENCES User(IdUser)
);

CREATE TABLE Exercise
(
  IdExercise INT NOT NULL AUTO_INCREMENT,
  IdUser INT NOT NULL,
  ExerciseName VARCHAR(255) NOT NULL,
  SerNum INT NOT NULL,
  RepNum INT NOT NULL,
  PRIMARY KEY (IdExercise, IdUser),
  FOREIGN KEY (IdUser) REFERENCES Student(IdUser)
);

CREATE TABLE Measurements
(
  IdMeas INT NOT NULL AUTO_INCREMENT,
  IdUser INT NOT NULL,
  MeasDate DATE NOT NULL,
  Weight FLOAT NOT NULL,
  Height FLOAT NOT NULL,
  HighWaist FLOAT,
  LowWaist FLOAT,
  Bust FLOAT,
  Biceps FLOAT,
  Thigh FLOAT,
  PRIMARY KEY (IdMeas, IdUser),
  FOREIGN KEY (IdUser) REFERENCES Student(IdUser)
);

CREATE TABLE Class
(
  IdClass INT NOT NULL AUTO_INCREMENT,
  IdUser INT NOT NULL,
  ClassName VARCHAR(255) NOT NULL,
  ClassDate DATETIME NOT NULL,
  ClassDescriprion VARCHAR(800) NOT NULL,
  StudentsMax INT NOT NULL,
  PRIMARY KEY (IdClass, IdUser),
  FOREIGN KEY (IdUser) REFERENCES Teacher(IdUser)
);

CREATE TABLE Goal
(
  IdGoal INT NOT NULL AUTO_INCREMENT,
  IdUser INT NOT NULL,
  CardioMin INT,
  GoalWeight FLOAT,
  GoalDate DATE NOT NULL,
  FinalDate DATE NOT NULL,
  LeanMassPct FLOAT,
  FatPct FLOAT,
  PRIMARY KEY (IdGoal, IdUser),
  FOREIGN KEY (IdUser) REFERENCES Student(IdUser)
);

CREATE TABLE Card
(
  IdUser INT NOT NULL,
  ValidityDate DATE NOT NULL,
  CardHolderName VARCHAR(255) NOT NULL,
  CardNum NUMERIC(16) NOT NULL,
  CVV NUMERIC(3) NOT NULL,
  CardType VARCHAR(255) NOT NULL,
  PRIMARY KEY (IdUser),
  FOREIGN KEY (IdUser) REFERENCES Student(IdUser)
);

CREATE TABLE Take
(
  IdStudent INT NOT NULL,
  IdClass INT NOT NULL,
  IdTeacher INT NOT NULL,
  PRIMARY KEY (IdStudent, IdClass, IdTeacher),
  FOREIGN KEY (IdStudent) REFERENCES Student(IdUser),
  FOREIGN KEY (IdClass, IdTeacher) REFERENCES Class(IdClass, IdUser)
);

