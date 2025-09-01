import pytest
from examples import simple_api
import examples.utils
import aiohttp, asyncio


@pytest.mark.asyncio
async def test_get_endpoint():
    # Mock response data
    mock_response_data = {"count": 1302}
    get_url = "https://pokeapi.co/api/v2/pokemon"
    test_file = "test_simple_get_result.json"

    result = await simple_api.get(get_url, test_file)

    assert result.get("count") == mock_response_data.get("count")

@pytest.mark.asyncio
async def test_post_endpoint():
    # Mock response data
    mock_request_body = {"count": 1302}
    post_url = "https://jsonplaceholder.typicode.com/posts"
    test_file = "test_simple_post_result.json"

    result = await simple_api.post(post_url, mock_request_body, test_file)

    assert result.get("count") == mock_request_body.get("count")
    

