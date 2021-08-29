import random
from uuid import uuid4

import pytest
from aioqvapay.v1 import QvaPay, QvaPayAuth, QvaPayException


@pytest.mark.asyncio
async def test_error():
    client = QvaPay("", "")
    try:
        await client.get_info()
        assert False
    except QvaPayException:
        assert True


@pytest.mark.asyncio
async def test_get_info():
    client = QvaPay.from_auth(QvaPayAuth())
    await client.get_info()


@pytest.mark.asyncio
async def test_create_invoice():
    client = QvaPay.from_auth(QvaPayAuth())
    await client.create_invoice(random.random(), "Invoice for testing", str(uuid4()))


@pytest.mark.asyncio
async def test_get_transactions():
    client = QvaPay.from_auth(QvaPayAuth())
    result = await client.get_transactions()
    if result.data:
        item = result.data[0]
        await client.get_transaction(item.id)
