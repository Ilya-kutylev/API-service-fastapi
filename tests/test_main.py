import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from app.main import app


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_get_path_success(async_client):
    response = await async_client.post("/get_path/", json={'element_id': "zinc-whimsy-interject"})
    assert response.status_code == 200
    assert response.json() == ["zealous-utopia-intrigue", "zany-xylophone-investigate", "zodiac-xenon-inscribe", "zinc-whimsy-interject"]


@pytest.mark.asyncio
async def test_get_path_not_found(async_client):
    response = await async_client.post("/get_path/", json={'element_id': "zen-wattage-jug"})
    assert response.status_code == 404
    assert response.json() == {'detail': f"ID element is not found in structure"}


@pytest.mark.asyncio
async def test_get_path_invalid_input(async_client):
    response = await async_client.post("/get_path/", json={'element_id': 2})
    assert response.status_code == 422




