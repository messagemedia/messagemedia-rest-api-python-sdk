# DeliveryReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account associated with this delivery report | [optional] 
**destination_address** | **str** | Address this delivery report was delivered to. This is the source address of the sent message that this delivery report is in response to | [optional] 
**destination_address_country** | **str** | Country associated with the destination address | [optional] 
**format** | **str** | Format of message, SMS or VOICE | [optional] [default to 'SMS']
**id** | **str** | Unique ID for this delivery report | [optional] 
**in_response_to** | **str** | Unique ID of the sent message that this delivery report is in response to | [optional] 
**metadata** | **object** | Metadata associated with the sent message | [optional] 
**source_address** | **str** | Address this delivery report was received from, the destination address of the sent message that this delivery report is in response to | [optional] 
**source_address_country** | **str** | Country associated with the source address | [optional] 
**status** | [**MessageStatus**](MessageStatus.md) |  | [optional] 
**status_code** | [**MessageStatusCode**](MessageStatusCode.md) |  | [optional] 
**timestamp** | **datetime** | Date time at which this delivery report was received | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


