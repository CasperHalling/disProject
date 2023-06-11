DELETE FROM course;


CREATE TABLE Course(
    course text,
    schedule varchar(1),
    termin int,
    average float,
    exam text,
    ects float
);



START TRANSACTION;
INSERT INTO Course(courseName, schedule, termin, average, exam, ects) VALUES  
    ('Co-design af digital sundhed', 'B', 1, 8.6, 'Skriftlig aflevering', 7.5),
    ('Computersystemer (CompSys)', 'C', 1, 4.9, 'Skriftlig prøve', 15),
    ('Diskret matematik og algoritmer (DMA)', 'B', 1, 0.0, 'Løbende Bedømmelse', 15),
    ('High Performance programmering og systemer (HPPS)', 'A', 2, 7.1, 'Skriftlig aflevering', 7.5),
    ('Introduktion til computergrafik (Grafik)', 'B', 2, 8.1, 'Løbende bedømmelse', 7.5),
    ('It-projektledelse (ITP)', 'A', 1, 7.7, 'Skriftlig aflevering', 7.5),
    ('It-sikkerhed (ITS)', 'B', 1, 5.9, 'Skriftlig prøve', 7.5),
    ('Logic in Computer Science (LICS)', 'A', 2, 6.0, 'Skriftlig prøve', 7.5),
    ('Matematisk analyse og sandsynlighedsteori i datalogi (MASD)', 'A', 1, 3.5, 'Skriftlig prøve', 7.5),
    ('Modelling and Analysis of Data (MAD)', 'A', 2, 6.3, 'Skriftlig aflevering', 7.5),
    ('Numerical Methods (NuMe)', 'C', 1, 6.1, 'Løbende Bedømmelse', 7.5),
    ('Python programmering til datavidenskab', 'C', 2, 5.2, 'Skriftlig prøve', 7.5),
    ('Python Programming for Data Science', 'B', 1, 7.5, 'Skriftlig prøve', 7.5),
    ('Reactive and Event Based Systems (REB)', 'B', 2, 8.4, 'Mundtlig bedømmelse', 7.5),
    ('Roboteksperimentarium (REX)', 'C', 2, 6.2, 'Mundtlig bedømmelse', 7.5),
    ('Udvikling af cloud-baserede sundheds-apps', 'C', 2, 10.3, 'Skriftlig aflevering', 7.5),
    ('Virksomhedsprojekt - hovedvejleder fra Datalogisk Institut 15 eller 30 ECTS', 'D', 1, 0.0, 'Skriftlig aflevering', 15),
    ('Virksomhedsprojekt - hovedvejleder fra Datalogisk Institut 15 eller 30 ECTS', 'D', 1, 0.0, 'Skriftlig aflevering', 30),
    ('Virksomhedsprojekt - hovedvejleder fra Datalogisk Institut 15 eller 30 ECTS', 'D', 2, 0.0, 'Skriftlig aflevering', 15),
    ('Virksomhedsprojekt - hovedvejleder fra Datalogisk Institut 15 eller 30 ECTS', 'D', 2, 0.0, 'Skriftlig aflevering', 30),
    ('Virtual Reality (VR)', 'A', 2, 9.9, 'Mundtlig bedømmelse', 7.5);

commit;