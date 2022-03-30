from extensions import db
from sqlalchemy import text
class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key = True)
    sent_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    sent_to = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(500))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_list_messages(cls, user1, user2):
        query = text("""select * 
        from public.messages 
        where (sent_by = :user1 AND sent_to = :user2) or (sent_by = :user2 AND sent_to = :user1)
        order by created_at""")
        result = db.session.execute(query, {'user1': user1, 'user2': user2})
        return [{
                    'id': row['id'],
                    'sent_by': row['sent_by'],
                    'sent_to': row['sent_to'],
                    'message': row['message'],
                    'created_at': str(row['created_at']),
                } for row in result]

    def save(self):
        db.session.add(self)
        db.session.commit()
