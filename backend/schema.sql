
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS event_hosts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    primary_host TEXT NOT NULL,
    host_email TEXT NOT NULL,
    organization_name TEXT UNIQUE NOT NULL,
    organization_address TEXT NOT NULL,
    organization_email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_id INTEGER,
    sender_email TEXT,
    receiver_id INTEGER,
    receiver_name TEXT,
    receiver_username TEXT,
    title TEXT,
    content TEXT,
    message_status TEXT,
    sent_on DATE
);

