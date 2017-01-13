# ReceivedMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account associated with this message | [optional] 
**action** | **str** | Action that was invoked for this message if any, OPTOUT, OPTIN, GLOBALOPTOUT | [optional] 
**content** | **str** | Content of the message | [optional] 
**destination_address** | **str** | Address this message was delivered to. If this message was received in response to a sent message, this is the source address of the sent message | [optional] 
**destination_address_country** | **str** | Country associated with the destination address | [optional] 
**format** | **str** | Format of message, SMS or TTS (Text To Speech) | [optional] 
**id** | **str** | Unique ID for this reply | [optional] 
**in_response_to** | **str** | If this message was received in response to a sent message, this is the ID of the sent message | [optional] 
**metadata** | **object** | If this message was received in response to a sent message, this is the metadata associated with the sent message | [optional] 
**source_address** | **str** | Address this message was received from. If this message was received in response to a sent message, this is the destination address of the sent message. | [optional] 
**source_address_country** | **str** | Country associated with the source address | [optional] 
**timestamp** | **datetime** | Date time at which this message was received | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


