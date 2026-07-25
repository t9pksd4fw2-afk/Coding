CREATE TABLE IF NOT EXISTS COMM(
activity_id INTEGER PRIMARY KEY,
activity_name TEXT NOT NULL,
activity_type TEXT NOT NULL,
day TEXT NOT NULL,
participants INTEGER NOT NULL,
duration_mins INTEGER NOT NULL);
INSERT INTO COMM VALUES (1, 'Yoga Class',        'Wellness', 'Monday',    18, 60);
INSERT INTO COMM VALUES (2, 'Art Workshop',      'Creative', 'Tuesday',   12, 90);
INSERT INTO COMM VALUES (3, 'Chess Club',        'Games',    'Wednesday', 16, 75);
INSERT INTO COMM VALUES (4, 'Dance Practice',    'Wellness', 'Thursday',  20, 60);
INSERT INTO COMM VALUES (5, 'Coding Club',       'Learning', 'Friday',    14, 90);
INSERT INTO COMM VALUES (6, 'Book Circle',       'Learning', 'Saturday',  10, 60);
INSERT INTO COMM VALUES (7, 'Painting Club',     'Creative', 'Saturday',  15, 75);
INSERT INTO COMM VALUES (8, 'Football Practice', 'Sports',   'Sunday',    22, 90);
INSERT INTO COMM VALUES (9, 'Meditation Hour',   'Wellness', 'Sunday',    13, 45);

SELECT * FROM COMM;

SELECT activity_name, participants
FROM COMM
ORDER BY participants ASC;

SELECT activity_name, participants
FROM COMM
ORDER BY participants DESC;

SELECT activity_name, activity_type
FROM COMM
ORDER BY activity_type ASC, participants DESC;

SELECT activity_name, participants
FROM COMM
ORDER BY participants DESC LIMIT 3;

SELECT activity_name, duration_mins
FROM COMM
ORDER BY duration_mins ASC LIMIT 5;

SELECT activity_type, COUNT(*) AS activity_count
FROM COMM
GROUP BY activity_type;

SELECT activity_type, SUM(participants) AS total_participants,
AVG(duration_mins) AS average_duration_mins FROM COMM
GROUP BY activity_type;

SELECT activity_type, AVG(participants) AS average_participants FROM COMM GROUP BY activity_type HAVING AVG(participants) >= 15;