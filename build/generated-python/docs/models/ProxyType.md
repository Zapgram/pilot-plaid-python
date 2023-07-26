# plaid.model.proxy_type.ProxyType

An enum indicating whether a network proxy is present and if so what type it is.  `none_detected` indicates the user is not on a detectable proxy network.  `tor` indicates the user was using a Tor browser, which sends encrypted traffic on a decentralized network and is somewhat similar to a VPN (Virtual Private Network).  `vpn` indicates the user is on a VPN (Virtual Private Network)  `web_proxy` indicates the user is on a web proxy server, which may allow them to conceal information such as their IP address or other identifying information.  `public_proxy` indicates the user is on a public web proxy server, which is similar to a web proxy but can be shared by multiple users. This may allow multiple users to appear as if they have the same IP address for instance.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | An enum indicating whether a network proxy is present and if so what type it is.  &#x60;none_detected&#x60; indicates the user is not on a detectable proxy network.  &#x60;tor&#x60; indicates the user was using a Tor browser, which sends encrypted traffic on a decentralized network and is somewhat similar to a VPN (Virtual Private Network).  &#x60;vpn&#x60; indicates the user is on a VPN (Virtual Private Network)  &#x60;web_proxy&#x60; indicates the user is on a web proxy server, which may allow them to conceal information such as their IP address or other identifying information.  &#x60;public_proxy&#x60; indicates the user is on a public web proxy server, which is similar to a web proxy but can be shared by multiple users. This may allow multiple users to appear as if they have the same IP address for instance. | must be one of ["none_detected", "tor", "vpn", "web_proxy", "public_proxy", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

