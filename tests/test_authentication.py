import pytest
from unittest.mock import patch, AsyncMock, Mock
from examples import authentication

@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_basic_auth(mock_get):
    mock_resp = Mock()
    mock_resp.raise_for_status = Mock()
    mock_resp.json = AsyncMock(return_value={'authenticated': True})
    mock_get.return_value.__aenter__.return_value = mock_resp
    
    result = await authentication.basic_auth_call("http://test.com", "user", "pass")
    
    mock_get.assert_called_once()
    assert result.get('authenticated') == True

@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_oauth(mock_get):
    mock_resp = Mock()
    mock_resp.raise_for_status = Mock()
    mock_resp.json = AsyncMock(return_value={'authenticated': True})
    mock_get.return_value.__aenter__.return_value = mock_resp
    
    result = await authentication.oauth_call("http://test.com", "token123")
    
    mock_get.assert_called_once()
    assert result.get('authenticated') == True