import random
from uuid import uuid4

from aioqvapay.v1 import QvaPayAuth, QvaPayClient, QvaPayException
from pytest import mark as pytest_mark


@pytest_mark.asyncio
async def test_error():
    client = QvaPayClient("", "")
    try:
        await client.get_info()
        assert False
    except QvaPayException:
        assert True


@pytest_mark.asyncio
async def test_get_info():
    client = QvaPayClient.from_auth(QvaPayAuth())
    await client.get_info()


@pytest_mark.asyncio
async def test_get_balance():
    client = QvaPayClient.from_auth(QvaPayAuth())
    await client.get_balance()


@pytest_mark.asyncio
async def test_create_invoice():
    client = QvaPayClient.from_auth(QvaPayAuth())
    await client.create_invoice(random.random(), "Invoice for testing", str(uuid4()))


@pytest_mark.asyncio
async def test_get_transactions():
    client = QvaPayClient.from_auth(QvaPayAuth())
    result = await client.get_transactions()
    if result.data:
        item = result.data[0]
        await client.get_transaction(item.id)
