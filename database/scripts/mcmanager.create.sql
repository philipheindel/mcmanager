CREATE TABLE Audit (
	AuditID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	Timestamp DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%f', 'now', 'localtime')),
	Message TEXT NOT NULL,
	System TEXT NOT NULL
);

CREATE TABLE Players (
	UUID TEXT PRIMARY KEY NOT NULL,
	Username TEXT NOT NULL,
	Name TEXT,
	Invitee, TEXT,
	DateAdded DATETIME,
	Notes TEXT
);

INSERT INTO Players (
	UUID,
	Username,
	Name,
	Invitee,
	DateAdded,
	Notes
)
VALUES (
	"19229106-a9f4-4e90-8635-6c5a5ea70f42",
	"RedwardFlip",
	"Philip",
	"Founder",
	"2021-11-30 19:00:00",
	"Stuff"
);