# ServerInformation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 

## Example

```python
from structifyai.models.server_information import ServerInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInformation from a JSON string
server_information_instance = ServerInformation.from_json(json)
# print the JSON string representation of the object
print ServerInformation.to_json()

# convert the object into a dict
server_information_dict = server_information_instance.to_dict()
# create an instance of ServerInformation from a dict
server_information_form_dict = server_information.from_dict(server_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


