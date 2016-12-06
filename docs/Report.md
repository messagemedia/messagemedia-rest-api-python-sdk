# Report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | The URL specified as the callback URL in the original submit message request | [optional] 
**date_received** | **datetime** | The date and time at which this delivery report was generated in UTC. | [optional] 
**delay** | **int** | Deprecated, no longer in use | [optional] 
**delivery_report_id** | **str** | Unique ID for this delivery report | [optional] 
**message_id** | **str** | Unique ID of the original message | [optional] 
**metadata** | **object** | Any metadata that was included in the original submit message request | [optional] 
**original_text** | **str** | Text of the original message. | [optional] 
**source_number** | **str** | Address from which this delivery report was received | [optional] 
**status** | **str** | The status of the message as per the delivery report | [optional] 
**submitted_date** | **datetime** | The date and time when the message status changed in UTC. For a delivered DR this may indicate the time at which the message was received on the handset. | [optional] 
**vendor_account_id** | [**ReplyVendorAccountId**](ReplyVendorAccountId.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


