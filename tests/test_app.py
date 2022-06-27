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
        self.assertEqual(Gardens.query.filter_by(id=2).address, "testing address")


class TestDelete(TestBase):
    def test_delete_garden(self):
        response = self.client.delete(
            url_for('delete_garden'),
            data = dict(address="Test Address")
        )
        self.assertEqual(0, len(Gardens.query.all()))

