import sqlalchemy
import model
import model.user

def reload_mappers(metadata):
    if metadata.bind.name == "sqlite":
        now = sqlalchemy.func.datetime("now", "localtime")
    else:
        now = sqlalchemy.func.now()

    # User Table mapping!!
    model.user.reload_mapper(metadata, now)
