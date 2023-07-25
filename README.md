<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/rodricorgom/AutomationProject">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Automation Project (Task 3) | Team 2</h3>

  <p align="center">
    The focus of this project is to build a functional Webex bot, capable of parsing CSV documents. Total functionality is expanded using commands.
    <br />
    <a href="https://github.com/rodricorgom/AutomationProject"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rodricorgom/AutomationProject">View Demo</a>
    ·
    <a href="https://github.com/rodricorgom/AutomationProject">Report Bug</a>
    ·
    <a href="https://github.com/rodricorgom/AutomationProject">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#team-members">Team members</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Standalone Installation</a></li>
        <li><a href="#installation">Docker Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Capture 1][code-c-2]](https://example.com)


This project aims to expand the information stored in the CSV file to add:
    
* Potential bugs information per version.
* PSIRT alerts per product.
* API consumption by providing additional access to Cisco Services API's. 

Using a Webex Bot: 

1. Share the report results with the (fictional) client.
2. Utilize the bot as a single point of contact/communication with the customer, where the customer can upload the initialCSV file, and the bot can provide a comprehensive analysis of the network.
3. With the PSIRT/bug information, inform the customer for any potentially catastrophic bug/PSIRT information and recommend the appropriate action to take (upgrade if available).
4. If memory usage is exceeding +90% notify the customer, ensuring explicit mention of a potential problem on the device.
5. Optimize/refactor the code: Identify and present the problems (or potential problems) on the code and how you solved them.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

----
## Team members

* Barrios Fernando
* Chávez Sánchez Juan Daniel
* Córdoba Gómez Rodrigo
* Espinosa Fernando
* Flores Constantino Diego
* Gomora Angélica

----
### Built With

* Python 3.9 or above (tested on Python 3.9 and 3.11) 
* The _webex_bot_ library by _Finbarr Brady_ (__fbradyirl__).
    * Available at: [https://github.com/fbradyirl/webex_bot](https://github.com/fbradyirl/webex_bot)
    * The official community webexteamssdk available at: [https://github.com/CiscoDevNet/webexteamssdk](https://github.com/CiscoDevNet/webexteamssdk)
    * The following core files have been modified to allow receiving messages with attachments:
        * __webex_bot.py__ and __webex_websocket_client.py__ 
* Cisco Product Security Incident Response Team (PSIRT)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This project can be run either standalone or via a Docker container. 
Docker container requiress building the image manually at the moment. 
__Please check the following sections for more information__.

### Standalone Installation

> It is highly recommended to use a virtual environment to run the dependencies. Virtualenv was used for development.

> __Project requires your bot access token.__

1. Clone the project repository and install the required dependencies
   ```sh
   pip install -r requirements.txt
   ```

2. Set the access token using an special _environmental variable_. This behavior is directly inherited from the __webexteamssdk__.
   ```sh
   export WEBEX_TEAMS_ACCESS_TOKEN=<your bots token>
   ```
    * Alternatively, you may edit the _.env file_ and add your access token to the __WEBEX_TEAMS_ACCESS_TOKEN__ key.
        ```sh
         WEBEX_TEAMS_ACCESS_TOKEN=[access_token]
        ```
        * Replacing __[access_toekn]__ with your own access token.

3. Run the project directly using python
   ```sh
   python3 ILSEH.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Docker Installation

1. Clone the repository.

2. Replace the environment variable for the bot's access token by editing the included __variables.env__ file.

3. Build the current Docker image via the included Dockerfile.
    > Replace [image_name] with your own name. Remeber to use descriptive names. This will be used in the next section.

   ```sh
   docker build -t [image_name] .
   ```

4. Run the container using the built image.

    > Replace [container_name] with your own name, and replace [image_name] with the image name from 3.

   ```python
   docker run --name [container_name] --env-file variables.env [image_name]
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Descriptions -->
## Changes made to the __webex_bot__ library (Finbarr Brady)

* By default, the library responds to Webex events through a webhook. This file is located in the path _./webex_bot/webex_bot/websockets/webex_websocket_client.py_. However, due to the way the websocket works in Webex, only those text-only messages (that is, they do not have embedded files) are received through this websocket.
    * The following code snippet shows the issue.

        [![Capture 1][code-c-1]](https://example.com)

        *  When processing the message it receives from the __Webex Clod__, it performs a <u>__preliminary check to determine the type of event__</u>. It is useful because the websocket catches a large number of events in the chat, both in 1-1 and in spaces. It can detect when someone is pinging the bot, when someone else is typing, and when the message was read. <u>Therefore we are not interested in these events</u>.

    * The following code snippet shows that the message is going to be reviewed to determine if the type of action is _"POST"_, that corresponds to messages containing text. However, there is __a verb that is used specifically to enclose a message with files__, and that is "SHARE". Therefore, a function is added to process messages that use "SHARE".
        ```sh
        if msg['data']['eventType'] == 'conversation.activity':
            activity = msg['data']['activity']
            if activity['verb'] == 'post':
                logger.debug(f"activity={activity}")

                message_base_64_id = self._get_base64_message_id(activity)
                webex_message = self.teams.messages.get(message_base_64_id)
                logger.debug(f"webex_message from message_base_64_id: {webex_message}")
                if self.on_message:
                    # ack message first
                    self._ack_message(message_base_64_id)
                    # Now process it with the handler
                    self.on_message(teams_message=webex_message, activity=activity)
            elif activity['verb'] == 'cardAction':
                logger.debug(f"activity={activity}")

        ```
    * The rest of the methods work the same way as for text messages. The important thing is getting the message details with a __GET request__ to the __/v1/messages/{_messageID_}__ endpoint. <u>The websocket library process the websocket message to get the Base64 message ID</u>. The above is done with the websocket URL and replaced by the message endpoint URL. We then move on to the __webex_bot__ library library
        ```sh

            logger.debug(msg)
                    if msg['data']['eventType'] == 'conversation.activity':
                        activity = msg['data']['activity']
                        if ((activity['verb'] == 'post') or (activity['verb'] == 'share')):
                            logger.debug(f"activity={activity}")

                            message_base_64_id = self._get_base64_message_id(activity)
                            webex_message = self.teams.messages.get(message_base_64_id)
                            logger.debug(f"webex_message from message_base_64_id: {webex_message}")
                            logger.debug(f"Message ID -> {message_base_64_id}")
                            if self.on_message:
                                # ack message first
                                self._ack_message(message_base_64_id)
                                # Now process it with the handler
                                self.on_message(teams_message=webex_message, activity=activity)
                        elif activity['verb'] == 'cardAction':
                            logger.debug(f"activity={activity}")

                            message_base_64_id = self._get_base64_message_id(activity)
                            attachment_actions = self.teams.attachment_actions.get(message_base_64_id)
                            logger.info(f"attachment_actions from message_base_64_id: {attachment_actions}")
                            if self.on_card_action:
                                # ack message first
                                self._ack_message(message_base_64_id)
                                # Now process it with the handler
                                self.on_card_action(attachment_actions=attachment_actions, activity=activity)
                        else:
                            logger.debug(f"activity verb is: {activity['verb']} ")
            -----------------------------
            def _get_base64_message_id(self, activity):
                """
                In order to geo-locate the correct DC to fetch the message from, you need to use the base64 Id of the
                message.
                @param activity: incoming websocket data
                @return: base 64 message id
                """
                logger.debug(f"Activity id = {activity['id']}")
                activity_id = activity['id']
                logger.debug(f"activity verb=post. message id={activity_id}")
                conversation_url = activity['target']['url']
                conv_target_id = activity['target']['id']
                if activity['verb'] == "post":
                    verb = "messages" 
                elif activity['verb']=="share":
                    verb = "messages"
                else: 
                    verb = "attachment/actions"
                conversation_message_url = conversation_url.replace(f"conversations/{conv_target_id}",
                                                                    f"{verb}/{activity_id}")
                headers = {"Authorization": f"Bearer {self.access_token}"}
                conversation_message = requests.get(conversation_message_url,
                                                    headers=headers).json()
                logger.debug(f"conversation_message={conversation_message}")
                return conversation_message['id']

        ```                 
            
    * The library works by recognizing keywords and matching them with a type corresponding to a command. So that it is possible to recognize when a file is sent, even when there is no associated keyword, it is checked if the message has the JSON "files" attribute. The <u>CSVCommand command is then called directly to read the request result as a CSV</u>.
        ```sh
            def process_raw_command(self, raw_message, teams_message, user_email, activity, is_card_callback_command=False):
                    room_id = teams_message.roomId
                    is_one_on_one_space = 'ONE_ON_ONE' in activity['target']['tags']

                    # Find the command that was sent, if any
                    command = None
                    user_command = raw_message.lower()
                    log.info(f"New user_command: {user_command}")
                    log.info(f"is_card_callback_command: {is_card_callback_command}")

                    log.debug(teams_message)
                    log.debug(self.files)

                    new_teams_message = str(teams_message).replace("Webex Teams Message:","")

                    if self.files != None:
                        parseData = json.loads(str(new_teams_message))
                        
                        #Retrieve the URL of the file 
                        attachmentURL = parseData['files'][0]

                        #Retrieve the message details via a GET request
                        request = requests.get(attachmentURL,headers={"Authorization": f"Bearer {self.teams_bot_token}"})
                        self.request=request

                        #Print the result of the CSV parsing
                        log.warning(request.text)

                        command = CSVCommand(request.text)

        ```



<p align="right">(<a href="#readme-top">back to top</a>)</p>


----------------
## Tasks descriptions 

### API Auth:
> Endpoint: https://id.cisco.com/oauth2/default/v1/token
- __Method__: POST
- __Headers__: Content-Type: application/x-www-form-urlencoded
- __Payload__: 
    - client_id=XXXXXX
    - client_secret=XXXXXX
    - grant_type=client_credentials 


```python
token = ''
url = 'https://id.cisco.com/oauth2/default/v1/token'
data = {
    'client_id': '63ed3gpqg5jbrrmbdch6zd4d',
    'client_secret': 'fTrzZVVTAMP9AdcRTXPvbSyS',
    'grant_type': 'client_credentials',
        }

response = requests.post(url, data=data)

if response.status_code == 200:
    global token
    token = response.json().get('access_token')
    print(f'Access token: {token}')
    
else:
    print(f'Request failed with status code {response.status_code}')

# HEADER 
headers = {
    'Authorization': f'Bearer {token}',
    }
device_id = 'CISCO2951/K9'
url = f"https://apix.cisco.com/bug/v3.0/bugs/products/product_id/{device_id}?page_index=1&modified_date=5"
response = requests.get(url, headers=headers)
# response.json()        

```

## BUG reporting:

> Auth: Bearer token (gather from the auth endpoint)
- __Get bugs associated to a product__
- Get additional information of a bug
    - URL: https://apix.cisco.com/bug/v3.0/bugs/bug_ids/CSCdr72939 


```python
df = pd.read_csv(csv_file)

df['Potential_bugs'] = ''
headers = {
    'Authorization': f'Bearer {token}',
            }

for index, row in df.iterrows():
    device_id = row['PID']
    if device_id:
        try:
            url = f"https://apix.cisco.com/bug/v3.0/bugs/products/product_id/{device_id}?page_index=1&modified_date=5"
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                response_data = (response.json())
                #print (response_data)
                bug_id = [bug['bug_id'] for bug in response_data['bugs']]
                df.at[index, 'Potential_bugs'] = bug_id
            else:
                print(f'Request failed with status code {response.status_code}')
                df.at[index, 'Potential_bugs'] = 'Wrong API access'
        except Exception as e:
            print(f"Failed to retrieve info from {device_id}: {str(e)}")
   
# Filter the response, and just get the bug_id, everything else, even though is important information will not be relevant for this task

csv_file = 'task_3_1.csv'
df.to_csv(csv_file, index = False)
```

## PSIRT API
Auth: Bearer token (gather from the auth endpoint)

- Get PSIRTS by Software release:
    - URL: https://apix.cisco.com/security/advisories/v2/OSType/iosxe?version=17.2.1

```python
# Create a new column name PSIRT and update it with the information retrieved by the Security Advisory API

csv_file = 'task_3_1.csv'
df = pd.read_csv(csv_file)

df['PSIRT'] = ''

# Define the proper authorization in the headers field
headers = {
    'Authorization': f'Bearer {token}',
            }

# This is an example to make sure the access/API is working as expected
url = f"https://apix.cisco.com/security/advisories/v2/product?product=Cisco%20IOS%20XE"
response = requests.get(url, headers=headers)

json_data = response.json()
    
# Extract the PSIRT information if available
psirt_info = json_data.get('advisories')
    
# Update the 'PSIRT' column with the retrieved information
df.at[index, 'PSIRT'] = psirt_info

csv_file = 'task_3_2.csv'
df.to_csv(csv_file, index = False)
```



[product-screenshot]: images/screenshot.png
[code-c-1]: images/code-c-1.png
[code-c-2]: images/code-c-2.png
