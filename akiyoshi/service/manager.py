from db.model.node import Node
from service.node import nodeService

class ManagerService():

    def nodes(self, orm, dir):
        controlNodes = orm.query(Node).all()
        fsNodes = nodeService.list(dir)
        return (controlNodes, fsNodes)

managerService = ManagerService()
