from application import db
from application.models import Plants, Gardens, Pla_Gar

db.drop_all()
db.create_all()

# add sample
# db.session.add(example)

db.session.commit()