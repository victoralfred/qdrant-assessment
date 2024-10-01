import requests
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.exceptions import ApiException

def create_collection(
    url: str,
    collection_name: str,
    shard_number: int,
    sharding_method: str = "auto",
    shard_key: list = None,
) -> bool:
    """
    Create a collection in Qdrant Cloud if it doesn't already exist.

    Parameters:
    - url (str): The URL for the Qdrant instance.
    - collection_name (str): Name of the collection to be created.
    - shard_number (int): Number of shards to be used in the collection.
    - sharding_method (str): The method of sharding, default is "auto".
    - shard_key (list[str]): Names of user-defined sharding keys, default is None.
    
    Returns:
    - bool: True if the collection was created successfully, False otherwise.
    """
    status = False
    client = QdrantClient(url=url)
    # Use an empty list if shard_key is not provided
    if shard_key is None:
        shard_key = []
    try:
        # Check if the collection exists
        if not client.collection_exists(collection_name=collection_name):
            # Create a new collection if it does not exist
            client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=100,
                    distance=models.Distance.COSINE
                ),
                shard_number=shard_number,
                sharding_method=sharding_method,
                optimizers_config=models.OptimizersConfigDiff(
                    default_segment_number=5,
                    indexing_threshold=0  # Disabling indexing for faster uploads
                ),
                quantization_config=models.BinaryQuantization(
                    binary=models.BinaryQuantizationConfig(always_ram=True)
                )
            )
            #Shard Key cannot be created with Auto sharding method, only execute block
            # if sharding key is custom
            if sharding_method == 'custom' and shard_key:
                for key in shard_key:
                    client.create_shard_key(collection_name, key)
            status = True  # Collection created successfully
    except (ApiException, ConnectionError, ValueError) as e:
        print(f"Error creating collection: {e}")
        return False  
    return status

def get_shard_info(
    url: str,
) ->list:
    """
    Retrieve cluster information for a specific collection from a Qdrant cluster.
    Args:
        url (str): Qdrant full path to the request endpoint
    Returns:
        list: A list with the cluster information for the collection.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # Convert the JSON response to a list
        # Example: Convert values of the dictionary to a list
        if isinstance(data, dict):
            return list(data.values())  # Convert dictionary values to a list
        else:
            return [data]  # Convert to list if it's a single value or unknown format
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    
def print_table( data):
    # Extract the headers (keys) from the first dictionary.
    headers = list(data[0].keys())
    column_widths = {header: max(len(header), max(len(str(row[header])) for row in data)) for header in headers}
    header_row = " | ".join(f"{header:{column_widths[header]}}" for header in headers)
    print(header_row)
    print("-" * len(header_row))  # Print a separator line in multiple of the header length
    # Print each row of data
    for row in data:
        row_data = " | ".join(f"{str(row[header]):{column_widths[header]}}" for header in headers)
        print(row_data)
     
if __name__== '__main__':
    collection_name = 'research_papers_collection'
    url = 'http://localhost:6333'
    shard_number = 2
    created = create_collection(url=url, 
                                collection_name=collection_name, 
                                shard_number=shard_number,
                               shard_key=['netherland', 'germany'],
                               sharding_method='custom')
    if created:
        print('Created colection')
    cluster_info = get_shard_info(f'{url}/collections/{collection_name}/cluster')
    if cluster_info:
        local_shards = [
        {'shard_id': shard['shard_id'],
        'shard_key': shard['shard_key'],
        'state': shard['state']}
        for item in cluster_info
        if isinstance(item, dict) and 'local_shards' in item
        for shard in item['local_shards']
        ]
        remote_shards=[
            {'shard_id': shard['shard_id'],
        'shard_key': shard['shard_key'],
        'state': shard['state']}
        for item in cluster_info
        if isinstance(item, dict) and 'remote_shards' in item
        for shard in item['remote_shards']
        ]
        result = [x for x in [*remote_shards ,*local_shards]]
        total_shrads = [*remote_shards ,*local_shards]
        # result = [x for x in remote_shards]
        print_table(result)
        print(f'Total Shards {len(total_shrads)}')
