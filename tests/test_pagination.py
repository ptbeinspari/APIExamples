import pytest
from unittest.mock import patch, AsyncMock
from examples import pagination

@pytest.mark.asyncio
async def test_pagination():
    
    expected_response_length = 1302
    get_url = "https://pokeapi.co/api/v2/pokemon?limit=20&offset=0"

    result = await pagination.fetch_paginated(get_url)  

    assert len(result) == expected_response_length