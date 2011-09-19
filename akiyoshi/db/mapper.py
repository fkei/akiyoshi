import sqlalchemy
import model
import model.user
import model.node
import model.notebook
import model.tag
import model.node2tag

def reload_mappers(metadata):
    if metadata.bind.name == "sqlite":
        now = sqlalchemy.func.datetime("now", "localtime")
    else:
        now = sqlalchemy.func.now()

    # User Table mapping!!
    model.user.reload_mapper(metadata, now)

    # NoteBook Table mapping!!
    model.notebook.reload_mapper(metadata, now)

    # Node2Tag Table mapping!!
    model.node2tag.reload_mapper(metadata, now)

    # Tag Table mapping!!
    model.tag.reload_mapper(metadata, now)

    # Node Table mapping!!
    model.node.reload_mapper(metadata, now)
