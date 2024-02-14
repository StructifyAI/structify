# CreateDataset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**name** | **str** |  | 
**schemas** | **List[str]** |  | 

## Example

```python
from structifyai.models.create_dataset import CreateDataset

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataset from a JSON string
create_dataset_instance = CreateDataset.from_json(json)
# print the JSON string representation of the object
print CreateDataset.to_json()

# convert the object into a dict
create_dataset_dict = create_dataset_instance.to_dict()
# create an instance of CreateDataset from a dict
create_dataset_form_dict = create_dataset.from_dict(create_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


