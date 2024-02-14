# DatasetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**name** | **str** |  | 
**version** | **int** |  | 

## Example

```python
from structifyai.models.dataset_model import DatasetModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetModel from a JSON string
dataset_model_instance = DatasetModel.from_json(json)
# print the JSON string representation of the object
print DatasetModel.to_json()

# convert the object into a dict
dataset_model_dict = dataset_model_instance.to_dict()
# create an instance of DatasetModel from a dict
dataset_model_form_dict = dataset_model.from_dict(dataset_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


