# PhysicalDocumentCategory

The type of identity document detected in the images provided. Will always be one of the following values:    `drivers_license` - A driver's license for the associated country    `id_card` - A general national identification card, distinct from driver's licenses    `passport` - A passport for the associated country    `residence_permit_card` - An identity document permitting a foreign citizen to <em>temporarily</em> reside in the associated country    `resident_card` - An identity document permitting a foreign citizen to <em>permanently</em> reside in the associated country  Note: This value may be different from the ID type that the user selects within Link. For example, if they select \"Driver's License\" but then submit a picture of a passport, this field will say `passport`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The type of identity document detected in the images provided. Will always be one of the following values:    &#x60;drivers_license&#x60; - A driver&#39;s license for the associated country    &#x60;id_card&#x60; - A general national identification card, distinct from driver&#39;s licenses    &#x60;passport&#x60; - A passport for the associated country    &#x60;residence_permit_card&#x60; - An identity document permitting a foreign citizen to &lt;em&gt;temporarily&lt;/em&gt; reside in the associated country    &#x60;resident_card&#x60; - An identity document permitting a foreign citizen to &lt;em&gt;permanently&lt;/em&gt; reside in the associated country  Note: This value may be different from the ID type that the user selects within Link. For example, if they select \&quot;Driver&#39;s License\&quot; but then submit a picture of a passport, this field will say &#x60;passport&#x60; |  must be one of ["drivers_license", "id_card", "passport", "residence_permit_card", "resident_card", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


