from datetime import datetime
import json
import logging
import os
from typing import Dict, Optional

import click
import requests

logging.basicConfig(level=logging.INFO)

@click.command()
@click.option(
    "-t",
    "--table_id",
    type=str,
    required=True,
    help="Socrata table-id for the data of interest.",
)
@click.option(
    "-o",
    "--output_dir_path",
    type=click.Path(dir_okay=True),
    required=True,
    help="Output dir path.",
)
def main(table_id: str, output_dir_path: os.path) -> None:
    """CLI script for Socrata table metadata."""

    logging.info(f"Fetching metadata for Socrata table {table_id})")
    output_dir_abspath = os.path.abspath(output_dir_path)
    assert os.path.isdir(output_dir_abspath)
    output_abspath = os.path.join(output_dir_abspath, f"{table_id}_metadata.json")
    table_metadata = get_metadata(table_id)
    dump_json(table_metadata=table_metadata, file_path=output_abspath)
    
def get_metadata(table_id: str) -> Dict:
    api_call = f"http://api.us.socrata.com/api/catalog/v1?ids={table_id}"
    response = requests.get(api_call)
    if response.status_code == 200:
        response_json = response.json()
        results = {"_id": table_id, "time_of_collection": datetime.utcnow()}
        results.update(response_json["results"][0])
        return results
    
def dump_json(table_metadata: Dict, file_path: os.path) -> None:
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(table_metadata, json_file, ensure_ascii=False, indent=4, default=str)
        
if __name__ == "__main__":
    main()