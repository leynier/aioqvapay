from typing import Union
from uuid import UUID

from aiohttp import ClientSession

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

    async def get_info(self) -> InfoModel:
        async with ClientSession() as session:
            url = self.base_url + "info"
            params = self.auth_params
            async with session.get(url, params=params) as response:
                validate_response(response)
                json = await response.json()
                result = InfoModel(**json)
                return result

    async def get_balance(self) -> float:
        async with ClientSession() as session:
            url = self.base_url + "balance"
            params = self.auth_params
            async with session.get(url, params=params) as response:
                validate_response(response)
                result = await response.json()
                return float(result)

    async def get_transactions(self, page: int = 1) -> PaginatedTransactionsModel:
        async with ClientSession() as session:
            url = self.base_url + "transactions"
            params = {"page": str(page), **self.auth_params}
            async with session.get(url, params=params) as response:
                validate_response(response)
                json = await response.json()
                result = PaginatedTransactionsModel(**json)
                return result

    async def get_transaction(self, id: Union[str, UUID]) -> TransactionDetailModel:
        async with ClientSession() as session:
            url = self.base_url + f"transaction/{str(id)}"
            params = self.auth_params
            async with session.get(url, params=params) as response:
                validate_response(response)
                json = await response.json()
                result = TransactionDetailModel(**json)
                return result

    async def create_invoice(
        self,
        amount: float,
        description: str,
        remote_id: str,
        signed: bool = False,
    ) -> InvoiceModel:
        async with ClientSession() as session:
            url = self.base_url + "create_invoice"
            params = {
                "amount": str(amount),
                "description": description,
                "signed": str(int(signed)),
                **self.auth_params,
            }
            if remote_id:
                params["remote_id"] = remote_id
            async with session.get(url, params=params) as response:
                validate_response(response)
                json = await response.json()
                result = InvoiceModel(**json)
                return result
