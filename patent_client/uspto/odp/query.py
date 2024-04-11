import csv
from pathlib import Path
import typing
from .model.api_models import SearchRequest

if typing.TYPE_CHECKING:
    from patent_client.util.manager import ManagerConfig

field_file = Path(__file__).parent / "query_fields.csv"

field_index = dict()

with field_file.open("r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        record = {
            "field_name": row["field_name"],
            "type": row["type"],
        }
        field_index[row["field_name"]] = record
        field_index[row["underscore_case"]] = record
        field_index[row["simple_name"]] = record
        
    
def create_post_search_obj(config: "ManagerConfig") -> "SearchRequest":
    query_obj = dict(
        pagination=dict(offset=0, limit=100),
        sort=list(),
        )
    q_str = list()
    range_filters = dict()
    for field, value in config.filter.items():
        if field.endswith("_gte") or field.endswith("_lte"):
            field_name, tail = field.rsplit("_", 1)
            if field_name not in field_index:
                raise ValueError(f"Unknown field: {field_name}")
            field_name = field_index[field_name]['field_name']
            if field.endswith("_gte"):
                range_filters[field_name] = {"valueFrom": value[0]}
            elif field.endswith("_lte"):
                range_filters[field_name] = {"valueTo": value[0]}
        
        else:
            if field not in field_index:
                raise ValueError(f"Unknown field: {field}")
            field_data = field_index[field]
            if field_data['type'] == "search":
                q_str.append(f"{field_data['field_name']}:({' OR '.join(value)})")
            else:
                q_str.append(f"{field_data['field_name']}=({' OR '.join(value)})")
    
    for sort_field, direction in config.order_by:
        query_obj['sort'].append(dict(
            field=field_index[sort_field]['field_name'],
            direction=direction
        ))
    query_obj["q"] = " AND ".join(q_str)
    query_obj['rangeFilters'] = [{"field": k, **v} for k, v in range_filters.items()]
    query_obj['pagination']['offset'] = config.offset
    query_obj['pagination']['limit'] = config.limit or 25
    query_obj['fields'] = ["applicationNumberText", "inventionTitle", "filingDate", "patentNumber"]
    return SearchRequest(**query_obj)
