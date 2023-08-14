# from dao.client_dao import ClientDao
# from dao.contract_dao import ContractDao
# from dao.event_dao import EventDao
# from dao.collaborator_dao import CollaboratorDao
from models.client import Client
# from models.collaborator import Collaborator
# from models.contract import Contract
# from models.event import Event
from datetime import date


class ClientRepository:
    def __init__(self, client_dao, contract_dao, event_dao, collaborator_dao):
        self.client_dao = client_dao
        # self.contract_dao = contract_dao
        # self.event_dao = event_dao
        # self.collaborator_dao = collaborator_dao

    # Repository methods
    def get_by_id(self, client_id):
        return self.client_dao.fetch_by_id(client_id)

    # def get_client_events(self, client_id):
    #     return self.event_dao.get_events_for_user(client_id)

    def create_client(self, client_data):
        client = Client(**client_data)
        self.client_dao.save(client)

    def update_client(self, client_id, new_data):
        client = self.client_dao.fetch_by_id(client_id)
        if client:
            # Update user's data based on new_data
            client.name = new_data.get('name', client.name)
            client.surname = new_data.get('surname', client.surname)
            client.email = new_data.get('email', client.email)
            client.telephone = new_data.get('telephone', client.telephone)
            # client.create_date = new_data.get('create_date', client.create_date)
            client.last_update_date = date.today()
            client.contact_id = new_data.get('contact_id', client.contact_id)
            self.client_dao.update(client)

    def delete_client(self, client_id):
        client = self.client_dao.fetch_by_id(client_id)
        if client:
            self.client_dao.delete(client)

    # def add_client(self)
    # def add_event(self)