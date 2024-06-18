import httpx
import hashlib
import asyncio
from rich import print

def calculate_file_hash(file_path, hash_algorithm='sha256'):
    """Calculate the hash of a file using the specified hash algorithm.
    
    Args:
        file_path (str): The path to the file.
        hash_algorithm (str): The hash algorithm to use (e.g., 'md5', 'sha1', 'sha256').
        
    Returns:
        str: The computed hash value as a hexadecimal string.
    """
    hash_func = hashlib.new(hash_algorithm)
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

async def get_model_info(hash: str):
    url = f'https://civitai.com/api/v1/model-versions/by-hash/{hash}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params={'hash': hash})
        return response.json()
    
async def main():
    hash = calculate_file_hash('/Users/kinda/Developer/AI/ComfyUI/models/loras/art_v4.0.safetensors')
    model_info = await get_model_info(hash)
    print(model_info)
    
if __name__ == '__main__':
    asyncio.run(main())