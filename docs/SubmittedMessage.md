# SubmittedMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | URL replies and delivery reports to this message will be pushed to | [optional] 
**content** | **str** | Content of the message | [optional] 
**destination_number** | **str** | Destination number of the message | [optional] 
**delivery_report** | **bool** | Request a delivery report for this message | [optional] [default to False]
**format** | **str** | Format of message, SMS or VOICE. | [optional] 
**message_expiry_timestamp** | **datetime** | Date time after which the message expires and will not be sent | [optional] 
**metadata** | **object** | Metadata for the message specified as a set of key value pairs, each key can be up to 100 characters long and each value can be up to 256 characters long &#x60;&#x60;&#x60; {    \&quot;myKey\&quot;: \&quot;myValue\&quot;,    \&quot;anotherKey\&quot;: \&quot;anotherValue\&quot; } &#x60;&#x60;&#x60;  | [optional] 
**scheduled** | **datetime** | Scheduled delivery date time of the message | [optional] 
**source_number** | **str** |  | [optional] 
**source_number_type** | **str** | Type of source address specified, this can be INTERNATIONAL, ALPHANUMERIC or SHORTCODE | [optional] 
**message_id** | **str** | Unique ID of this message | [optional] 
**status** | **str** | The status of the message | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


