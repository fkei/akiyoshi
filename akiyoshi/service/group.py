from db.access.tag import tagAccess

class GroupService:

    def find(self, session, category):
        return tagAccess.findbyCategory(session, category)

groupService = GroupService()
