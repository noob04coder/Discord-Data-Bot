# discord2sheet-bot

This bot allows users to submit ethereum address to your Google Sheet.

Example:

`!s Hello world, How are you today?`

Output:

Username - UserID - Date - Field 1 - Field 2

![Google Sheet](https://i.imgur.com/MFx25Ik.png)

## How to set it up

**Step 1:** Enable the API and download credentials.json. This can be done here: https://developers.google.com/sheets/api/quickstart/python#step_1_turn_on_the

*Make sure to rename it to credentials.json and it is stored in the same directory as the bot.*

**Step 2:** Ceate config.json in the bot folder(same level as init.py) and paste the following and change the values(<>):

```
{
"prefix":"!s", "Comment":"prefix of the bot (make sure it consist of 2 letters like !s",
"token":"", "Comment":"bot token",
"spreadsheet":"1yzJklTMwrtyRUP8TI4256E0UlOSqagToyzSBRR8b20Q", "Comment":"spreadsheet id (present between two slashes)",
"role":null, "Comment":"set it to role id or null",
"channel":null,"Comment":"set it to channel id or null",
"start-row":"A1","Comment":"row from where data starts",
"toggle-purge":false,"Comment":"toogle wrong message deleting(it is case sensitive)",
"toggle-purge-success":false,"Comment":"toogle success message deleting(it is case sensitive)"
}
```
prefix = <> - command to which the bot will reply to . Default is '!s'

token = <> - The token of the Discord bot.

spreadsheet = <> - The ID of the spreashsheet to store the data. It can be found on the URL once opened.

role = <> - If you want to restrict the command to a specific role, insert here the role id(as integer). If not, insert `null`.

channel = <> - If you want to restrict the command to a specific channel, insert here the channel id (as integer). If not, insert `null`.

start-row = <> - Where the data should go in the spreadsheet. Default value is `A1`.

toggle-purge = <> - If you want to delete wrong messages (from pesron without the role or from wrong channel) . 'true' for enable, 'false' for disable (proper font-case is important)

toggle-purge-success = <> - If you want to delete success messages (after success data entry) . 'true' for enable, 'false' for disable (proper font-case is important)

**Step 3:** Install Python dependencies

If you haven't installed Python yet, download it [here](https://www.python.org/).

Install discordpy: `pip install discord.py`

Run the pip command listed here: https://developers.google.com/sheets/api/quickstart/python#step_2_install_the_google_client_library

**Step 4:** Run the bot

`python init.py` `python3 init.py`

------

## Additional configutations (can be done in init.py)
FIELDS = <> - Amount of fields/cells that get stored. They are on the user's message seperated by comma (!s field1, field2,field 3)

DATA = <> - What data goes to the rows, seperated by `[]`. Example: `DATA = [result[0]] + [''] + [result[1]]`
