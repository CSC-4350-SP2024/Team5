
import sqlite3


class EventGuestServices:
    
    def get_unread_notifications(self, receiver_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        sql_query = """
        SELECT * FROM messages
        WHERE receiver_id = ? AND message_status = 'Unread'
        """

        cursor.execute(sql_query, (receiver_id,))

        unread_messages = cursor.fetchall()
        print(unread_messages)
        
        conn.close()

        return unread_messages
    
    def update_message_status(self, message_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        sql_query = """
        UPDATE messages
        SET message_status = 'Read'
        WHERE id = ?
        """

        cursor.execute(sql_query, (message_id,))

        conn.commit()

        cursor.close()
        conn.close()
        
        