from .database import db_manager

class BaseRepository:
    def __init__(self, model):
        self.model = model
        self.BD = db_manager.get_db()

    def getAll(self, schema, limit: int = None):
        query = self.BD.query(self.model)
        if limit:
            query = query.limit(limit)

        data = query.all()
        return [schema(**item.__dict__) for item in data]

    def get_by_id(self, id):
        return self.BD.query(self.model).get(id)

    def create(self, data):
        item = self.model(**data)
        self.BD.add(item)
        self.BD.commit()
        self.BD.refresh(item)
        return item

    def update(self, id, data):
        item = self.BD.query(self.model).get(id)
        if item:
            for key, value in data.items():
                setattr(item, key, value)
            self.BD.commit()
            self.BD.refresh(item)
        return item

    def delete(self, id):
        item = self.BD.query(self.model).get(id)
        if item:
            self.BD.delete(item)
            self.BD.commit()
        return item