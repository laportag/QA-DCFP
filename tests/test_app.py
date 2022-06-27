from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Plants, Gardens

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///testdb.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app

    def setUp(self):
        db.create_all()
        testGarden = Gardens(
            address = "Test Address"
        )
        testPlant = Plants(
            com_name = "Test com_name",
            sci_name = "test sci_name"
        )
        db.session.add(testGarden)
        db.session.add(testPlant)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_index(self):
        response = self.client.get(url_for("index"))
        self.assertEqual(response.status_code, 200)

    def test_gardens(self):
        response = self.client.get(url_for("gardens"))
        self.assertEqual(response.status_code, 200)

    def test_plants(self):
        response = self.client.get(url_for("plants"))
        self.assertEqual(response.status_code, 200)

class TestAdds(TestBase):
    def test_garden_add(self):
        response = self.client.post(
            url_for('garden_add'),
            data = dict(address="testing address")
        )
        self.assertEqual(Gardens.query.filter_by(id=2).first().address, "testing address")

    def test_plant_add(self):
        response = self.client.post(
            url_for('plant_add'),
            data = dict(
                com_name="test name",
                sci_name="test sci name"
                )
        )
        self.assertEqual(Plants.query.filter_by(id=2).first().com_name, "test name")


class TestDelete(TestBase):
    def test_delete_garden(self):
        response = self.client.get(
            url_for('delete_garden', id=1)
        )
        self.assertEqual(0, len(Gardens.query.all()))

    def test_delete_plant(self):
        response = self.client.get(
            url_for('delete_plant', id=1)
        )
        self.assertEqual(0, len(Plants.query.all()))


class TestUpdate(TestBase):
    def test_update_garden(self):
        response = self.client.post(
            url_for('update_garden', id=1),
            data = dict(address="testing address")
        )
        self.assertEqual(Gardens.query.filter_by(id=1).first().address, "testing address")
    
    def test_update_plant(self):
        response = self.client.post(
            url_for('update_plant', id=1),
            data = dict(
                com_name="test name",
                sci_name="test sci name"
                )
        )
        self.assertEqual(Plants.query.filter_by(id=1).first().com_name, "test name")