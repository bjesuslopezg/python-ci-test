from sqlalchemy.ext.automap import automap_base
from repository.database import db_manager

Base = automap_base()

def initialize_base():
    engine = db_manager.engine
    Base.prepare(engine, reflect=True)

    # print("Modelos generados:")
    # for class_name, class_type in Base.classes.items():
    #     print(class_name)

initialize_base()