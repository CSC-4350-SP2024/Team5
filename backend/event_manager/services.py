
import sqlite3

class EventManagerServices:
    
    def fetch_users(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, first_name, last_name, username, email FROM users")

        event_attendees = cursor.fetchall()

        conn.close()
        if event_attendees:
            return event_attendees
        else:
            return "No attendees found."
    
    
    def send_message(self, message):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        sql_query = """
        INSERT INTO messages (sender_id, sender_email, receiver_id, receiver_name, receiver_username, title, content, message_status, sent_on)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(sql_query, (
            message.sender_id,
            message.sender_email,
            message.receiver_id,
            message.receiver_name,
            message.receiver_username,
            message.title,
            message.content,
            message.message_status,
            message.sent_on
        ))

        conn.commit()
        conn.close()
    
   
    

        
        
    
