import pytest
from unittest.mock import patch, AsyncMock
from examples import pagination

@pytest.mark.asyncio
async def test_pagination():
    # Test against real API - check for at least the original count
    get_url = "https://pokeapi.co/api/v2/pokemon?limit=20&offset=0"

    result = await pagination.fetch_paginated(get_url)

    # Data grows over time, so check for at least the original count
    assert len(result) >= 1302
    assert isinstance(result, list)
    assert len(result) > 0