USE dbacademychi;

CREATE TABLE User
(
  IdUser INT NOT NULL,
  UserName VARCHAR(255) NOT NULL,
  BirthDate DATE NOT NULL,
  CPF NUMERIC(11) NOT NULL,
  RG NUMERIC(11) NOT NULL,
  UserPassaword VARCHAR(255) NOT NULL,
  PRIMARY KEY (IdUser),
  UNIQUE (CPF)
);

CREATE TABLE Teacher
(
  EntryHour TIME NOT NULL,
  ExitHour TIME NOT NULL,
  IdUser INT NOT NULL,
  PRIMARY KEY (IdUser),
  FOREIGN KEY (IdUser) REFERENCES User(IdUser)
);

CREATE TABLE Student
(
  PhoneNumber NUMERIC(11) NOT NULL,
  State CHAR(2) NOT NULL,
  City VARCHAR(255) NOT NULL,
  Neighbordhood VARCHAR(255) NOT NULL,
  ResgistrationDate DATE NOT NULL,
  MedicalData VARCHAR(800),
  IdUser INT NOT NULL,
  PRIMARY KEY (IdUser),
  FOREIGN KEY (IdUser) REFERENCES User(IdUser)
);

CREATE TABLE ComQuestion
(
  IdQuestion INT NOT NULL,
  QuestionText VARCHAR(800) NOT NULL,
  ResponseText VARCHAR(800) NOT NULL,
  PRIMARY KEY (IdQuestion)
);

CREATE TABLE Exercise
(
  IdExercise INT NOT NULL,
  ExerciseName VARCHAR(255) NOT NULL,
  SerNum INT NOT NULL,
  RepNum INT NOT NULL,
  IdUser INT NOT NULL,
  PRIMARY KEY (IdExercise, IdUser),
  FOREIGN KEY (IdUser) REFERENCES Student(IdUser)
);

CREATE TABLE Measurements
(
  IdMeas INT NOT NULL,
  MeasDate DATE NOT NULL,
  Weight FLOAT NOT NULL,
  Height FLOAT NOT NULL,
  HighWaist FLOAT,
  LowWaist FLOAT,
  Bust FLOAT,
  Biceps FLOAT,
  _Thigh FLOAT,
  IdUser INT NOT NULL,
  PRIMARY KEY (IdMeas, IdUser),
  FOREIGN KEY (IdUser) REFERENCES Student(IdUser)
);

CREATE TABLE Class
(
  IdClass INT NOT NULL,
  ClassName VARCHAR(255) NOT NULL,
  ClassDate DATE NOT NULL,
  ClassDescriprion VARCHAR(800) NOT NULL,
  StudentsMax INT NOT NULL,
  IdUser INT NOT NULL,
  PRIMARY KEY (IdClass, IdUser),
  FOREIGN KEY (IdUser) REFERENCES Teacher(IdUser)
);

CREATE TABLE Goal
(
  IdGoal INT NOT NULL,
  CardioMin INT,
  GoalWeight FLOAT,
  GoalDate DATE NOT NULL,
  FinalDate DATE NOT NULL,
  LeanMassPct FLOAT,
  FatPct FLOAT,
  IdUser INT NOT NULL,
  PRIMARY KEY (IdGoal, IdUser),
  FOREIGN KEY (IdUser) REFERENCES Student(IdUser)
);

CREATE TABLE Card
(
  ValidityDate DATE NOT NULL,
  CardHolderName VARCHAR(255) NOT NULL,
  CardNum INT NOT NULL,
  CVV NUMERIC(3) NOT NULL,
  CardType VARCHAR(255) NOT NULL,
  IdUser INT NOT NULL,
  PRIMARY KEY (IdUser),
  FOREIGN KEY (IdUser) REFERENCES Student(IdUser)
);

CREATE TABLE Take
(
  IdStuden INT NOT NULL,
  IdClass INT NOT NULL,
  IdTeacher INT NOT NULL,
  PRIMARY KEY (IdStuden, IdClass, IdTeacher),
  FOREIGN KEY (IdStuden) REFERENCES Student(IdUser),
  FOREIGN KEY (IdClass, IdTeacher) REFERENCES Class(IdClass, IdUser)
);

