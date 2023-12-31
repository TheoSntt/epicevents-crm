# from dao.client_dao import ClientDao
# from dao.contract_dao import ContractDao
# from dao.event_dao import EventDao
# from dao.collaborator_dao import CollaboratorDao
# from models.client import Client
from models.collaborator import Collaborator
# from models.contract import Contract
# from models.event import Event
from auth.auth_handler import AuthHandler
from repository.authorization_decorators import has_permission


auth_handler = AuthHandler()


class CollaboratorRepository:
    def __init__(self,
                 # client_dao,
                 # contract_dao,
                 # event_dao,
                 collaborator_dao):
        # self.client_dao = client_dao
        # self.contract_dao = contract_dao
        # self.event_dao = event_dao
        self.collaborator_dao = collaborator_dao

    # Repository methods
    def get_by_id(self, collaborator_id):
        return self.collaborator_dao.fetch_by_id(collaborator_id)

    @has_permission(permission="read_collab")
    def get(self, token, filters):
        if filters != {}:
            return self.collaborator_dao.get_by_expression(filters)
        return self.collaborator_dao.get_all()

    def get_by_username(self, username):
        return self.collaborator_dao.get_by_username(username)

    @has_permission(permission="create_collab")
    def create_collaborator(self, token, collaborator_data):
        collaborator = Collaborator(**collaborator_data)
        collaborator.password = auth_handler.hash_password(collaborator.password)
        collaborator = self.collaborator_dao.create(collaborator)
        return collaborator

    @has_permission(permission="update_collab")
    def update_collaborator(self, token, collaborator_id, new_data):
        collaborator = self.collaborator_dao.fetch_by_id(collaborator_id)
        if collaborator:
            # Update user's data based on new_data
            collaborator.username = new_data.get('username', collaborator.username)
            if new_data.get('password'):
                collaborator.password = auth_handler.hash_password(new_data.get('password'))
            # collaborator.password = new_data.get('password', collaborator.password)
            collaborator.surname = new_data.get('surname', collaborator.surname)
            collaborator.name = new_data.get('name', collaborator.name)
            collaborator.surname = new_data.get('surname', collaborator.surname)
            collaborator.email = new_data.get('email', collaborator.email)
            collaborator.telephone = new_data.get('telephone', collaborator.telephone)
            collaborator.role_id = new_data.get('role_id', collaborator.role_id)
            collaborator = self.collaborator_dao.update(collaborator)
            return collaborator

    @has_permission(permission="delete_collab")
    def delete_collaborator(self, token, collaborator_id):
        collaborator = self.collaborator_dao.fetch_by_id(collaborator_id)
        if collaborator:
            self.collaborator_dao.delete(collaborator)
            return collaborator

    # def add_client(self)
    # def add_event(self)
