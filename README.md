<h1 align="center">CordRPC</h1>
<p align="center">CordRPC - is a utility to create a cool menu in your discord profile.</p>
<p align="center"><a href="LICENSE">License</a>

# Setup
* Download the CordRPC files
* Use `pip3 install -r requirements.txt` to install the requirements
## Editing config file
Open the config.json file and set all the params

Default config:
```json
{
    "client_id": "YOUR_CLIENT_ID_HERE",
    "large_image": "YOUR_LARGE_IMAGE",
    "large_text": "YOUR_LARGE_TEXT",
    "details": "YOUR_DETAILS",
    "state": "STATE",
    "update_time": 60,
    "buttons": [
        {
            "label":"BUTTON_LABEL",
            "url": "URL"
        },
        {
            "label":"BUTTON_LABEL",
            "url": "URL"
        }
    ]
}
```

* `client_id` - You can find the client id in [Discord Developer Portal](https://discord.com/developers/applications)/Your application/Oauth2/General
* `large_image` - This image will be displayed at Activity menu in your profile. You can edit it at [Discord Developer Portal](https://discord.com/developers/applications)/Your application/Rich Presence/ Art assets. NOTE! On some clients the image won't seem
* `large_text` - This parameter is a text that will be displayed when you point at the image
* `update_time` - Time after menu will disappear
* Other params you can see here


Code:
```json
{
    "client_id": "1094627712070582333",
    "large_image": "bb6",
    "large_text": "large text",
    "details": "Details",
    "state": "State",
    "update_time": 60,
    "buttons": [
        {
            "label":"Link 1",
            "url": "https://youtube.com"
        },
        {
            "label":"Link 2",
            "url": "https://github.com"
        }
    ]
}

```
And the menu:


![Menu](testpic.png)

NOTE! The bold text is a name of your bot. Please remember it. 
