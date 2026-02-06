import pytest
from unittest.mock import patch, AsyncMock, Mock
from examples import batch

@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_batch_processing(mock_get):
    mock_resp = Mock()
    mock_resp.raise_for_status = Mock()
    mock_resp.json = AsyncMock(return_value={'id': 1})
    mock_get.return_value.__aenter__.return_value = mock_resp
    
    ids = [1, 2, 3, 4, 5, 6]
    await batch.batch_fetch_ids("http://test.com/items", ids)
    
    assert mock_get.call_count == len(ids)
    for id in ids:
        mock_get.assert_any_call(f"http://test.com/items/{id}")