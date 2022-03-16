from . import db


class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_title = db.Column(db.String(255))
    property_description = db.Column(db.String(255))
    noOfRooms = db.Column(db.Integer)
    noOfBathrooms = db.Column(db.Integer)
    property_price = db.Column(db.String(255))
    property_location = db.Column(db.String(255))
    property_type = db.Column(db.String(255))
    property_imgFilename = db.Column(db.String(255))

    def __init__(self, property_title, property_description, noOfRooms, noOfBathrooms, property_price, property_location, property_type, property_imgFilename):
        self.property_title = property_title
        self.property_description = property_description
        self.noOfRooms = noOfRooms
        self.noOfBathrooms = noOfBathrooms
        self.property_price = property_price
        self.property_location = property_location
        self.property_type = property_type
        self.property_imgFilename = property_imgFilename
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
    
    def __repr__(self):
        return '<Property %r>' % (self.property_title)
        


    

