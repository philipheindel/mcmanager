CREATE TABLE Audit (
	AuditID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	Timestamp DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%f', 'now', 'localtime')),
	Message TEXT NOT NULL,
	System TEXT NOT NULL
);
