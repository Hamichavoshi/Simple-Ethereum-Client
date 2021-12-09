class UserError(Exception):
    pass

class ContractError(Exception):
    pass

class MethodNotFound(ContractError):
    pass

class ConnectionError(Exception):
    pass