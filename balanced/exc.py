import requests


class BalancedError(Exception):
    pass


class ResourceError(BalancedError):
    pass


class NoResultFound(BalancedError):
    pass


class MultipleResultsFound(BalancedError):
    pass


class HTTPError(BalancedError, requests.HTTPError):
    """
    Baseclass for all HTTP exceptions.
    """
    status_code = None


class MoreInformationRequiredError(HTTPError):
    redirect_uri = None


class FundingInstrumentVerificationFailure(HTTPError):
    pass


class BankAccountVerificationFailure(FundingInstrumentVerificationFailure):
    pass


errors = [
    'bank-account-authentication-not-pending',
    'bank-account-authentication-failed',
    'bank-account-authentication-already-exists'
]

category_code_map = {
    err: BankAccountVerificationFailure
    for err in errors
}
