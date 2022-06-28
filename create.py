from application import db
from application.models import Plants, Gardens, Pla_Gar

db.drop_all()
db.create_all()

sample_garden = Gardens(
    address = "Sample Street, Sampleton, SMP3L3"
)
sample_plant = Plants(
    com_name = "Sample",
    sci_name = "Exemplum planta"
)
sample_pla_gar = Pla_Gar(
    plant_id = "1",
    garden_id = "1"
)
db.session.add(sample_garden)
db.session.add(sample_plant)
db.session.add(sample_pla_gar)

db.session.commit()