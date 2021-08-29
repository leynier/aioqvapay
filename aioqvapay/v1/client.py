from typing import Union
from uuid import UUID

from httpx import AsyncClient, get

from .auth import QvaPayAuth
from .models.info_model import InfoModel
from .models.invoice_model import InvoiceModel
from .models.paginated_transactions_model import PaginatedTransactionsModel
from .models.transaction_detail_model import TransactionDetailModel
from .utils import validate_response


class QvaPayClient:
    def __init__(self, app_id: str, app_secret: str) -> None:
        self.app_id = app_id
        self.app_secret = app_secret
        self.auth_params = {"app_id": app_id, "app_secret": app_secret}
        self.base_url = "https://qvapay.com/api/v1/"

    @staticmethod
    def from_auth(auth: QvaPayAuth) -> "QvaPayClient":
        return QvaPayClient(auth.qvapay_app_id, auth.qvapay_app_secret)

    def get_info(self) -> InfoModel:
        url = self.base_url + "info"
        params = self.auth_params
        response = get(url, params=params)
        validate_response(response)
        json = response.json()
        result = InfoModel(**json)
        return result

    async def get_info_async(self) -> InfoModel:
        async with AsyncClient() as session:
            url = self.base_url + "info"
            params = self.auth_params
            response = await session.get(url, params=params)
            validate_response(response)
            json = response.json()
            result = InfoModel(**json)
            return result

    def get_balance(self) -> float:
        url = self.base_url + "balance"
        params = self.auth_params
        response = get(url, params=params)
        validate_response(response)
        result = response.json()
        return float(result)

    async def get_balance_async(self) -> float:
        async with AsyncClient() as session:
            url = self.base_url + "balance"
            params = self.auth_params
            response = await session.get(url, params=params)
            validate_response(response)
            result = response.json()
            return float(result)

    def get_transactions(self, page: int = 1) -> PaginatedTransactionsModel:
        url = self.base_url + "transactions"
        params = {"page": str(page), **self.auth_params}
        response = get(url, params=params)
        validate_response(response)
        json = response.json()
        result = PaginatedTransactionsModel(**json)
        return result

    async def get_transactions_async(self, page: int = 1) -> PaginatedTransactionsModel:
        async with AsyncClient() as session:
            url = self.base_url + "transactions"
            params = {"page": str(page), **self.auth_params}
            response = await session.get(url, params=params)
            validate_response(response)
            json = response.json()
            result = PaginatedTransactionsModel(**json)
            return result

    def get_transaction(self, id: Union[str, UUID]) -> TransactionDetailModel:
        url = self.base_url + f"transaction/{str(id)}"
        params = self.auth_params
        response = get(url, params=params)
        validate_response(response)
        json = response.json()
        result = TransactionDetailModel(**json)
        return result

    async def get_transaction_async(
        self, id: Union[str, UUID]
    ) -> TransactionDetailModel:
        async with AsyncClient() as session:
            url = self.base_url + f"transaction/{str(id)}"
            params = self.auth_params
            response = await session.get(url, params=params)
            validate_response(response)
            json = response.json()
            result = TransactionDetailModel(**json)
            return result

    def create_invoice(
        self,
        amount: float,
        description: str,
        remote_id: str,
        signed: bool = False,
    ) -> InvoiceModel:
        url = self.base_url + "create_invoice"
        params = {
            "amount": str(amount),
            "description": description,
            "signed": str(int(signed)),
            **self.auth_params,
        }
        if remote_id:
            params["remote_id"] = remote_id
        response = get(url, params=params)
        validate_response(response)
        json = response.json()
        result = InvoiceModel(**json)
        return result

    async def create_invoice_async(
        self,
        amount: float,
        description: str,
        remote_id: str,
        signed: bool = False,
    ) -> InvoiceModel:
        async with AsyncClient() as session:
            url = self.base_url + "create_invoice"
            params = {
                "amount": str(amount),
                "description": description,
                "signed": str(int(signed)),
                **self.auth_params,
            }
            if remote_id:
                params["remote_id"] = remote_id
            response = await session.get(url, params=params)
            validate_response(response)
            json = response.json()
            result = InvoiceModel(**json)
            return result
