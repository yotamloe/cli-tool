import json


class ArtiifactoryUser:
    def __init__(self, name, email, password, admin, groups, profileupdatable, disableuiccess,
                 internalpassworddisabled, watchmanager, policymanager):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
        self.groups = list(groups)
        self.profileupdatable = profileupdatable
        self.disableuiccess = disableuiccess
        self.internalpassworddisabled = internalpassworddisabled
        self.watchmanager = watchmanager
        self.policymanager = policymanager


    def to_json(self):
        """Convert class representation to json string to include in api calls"""
        return json.dumps({
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'admin': self.admin,
            'groups': self.groups,
            'profileupdatable': self.profileupdatable,
            'disableuiccess': self.disableuiccess,
            'internalpassworddisabled': self.internalpassworddisabled,
            'watchmanager': self.watchmanager,
            'policymanager': self.policymanager,

        })
