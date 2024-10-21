import aiofiles
import json
import os
from typing import List, Dict, Optional
from fastapi import HTTPException

STRUCTURE_PATH = os.getenv("STRUCTURE_PATH", "structure.json")


async def load_structure() -> List[Dict]:
    try:
        async with aiofiles.open(STRUCTURE_PATH, 'r') as file:
            data = await file.read()
            return json.loads(data)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Structure file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid structure format")


async def find_path(structure: List[Dict], target_id: str) -> Optional[List[str]]:
    for point in structure:
        if point['uuid'] == target_id:
            return [point['uuid']]
        if point.get('children'):
            child_path = await find_path(point['children'], target_id)
            if child_path:
                return [point['uuid']] + child_path

    return None
