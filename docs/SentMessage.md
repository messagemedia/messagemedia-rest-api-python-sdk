# SentMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account associated with this message | [optional] 
**content** | **str** | Content of the message | [optional] 
**delivered_timestamp** | **datetime** | If a delivery report was requested for this message, this is the time at which the message was delivered (or failed to be delivered) to the destination address. | [optional] 
**delivery_report** | **bool** | Indicates if a delivery report was requested for this message | [optional] 
**destination_address** | **str** | Address this message was delivered to | [optional] 
**destination_address_country** | **str** | Country associated with the destination address | [optional] 
**format** | **str** | Format of message, SMS or TTS (Text To Speech) | [optional] 
**id** | **str** | Unique ID for this message | [optional] 
**in_response_to** | **str** | If this message was sent in response to a received message (an auto response message for example) this is the ID of the received message. | [optional] 
**metadata** | **object** | Metadata associated with this message | [optional] 
**source_address** | **str** | Address this message was sent from | [optional] 
**source_address_country** | **str** | Country associated with the source address | [optional] 
**timestamp** | **datetime** | Date time at which this message was submitted to the API, refer to the delivered timestamp for the time at which the message was delivered (or failed to be delivered) to the destination address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


