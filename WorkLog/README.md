`Date last modified: 2023 04 04`

# Work Log

## Context
The WorkLog is a Command-line Application for managing a personal work journal. Entries are saved as .txt files and stored within the `worklog/LogFiles` directory. 

This project was developed while working @ Eagle & Associates, a logistics firm. I used the project to record and organize my day-to-day activites, questions, comments. It was nice to have something which was not dependent upon cloud-based solutions like Google Sheets, iOS Notes, etc. 

## Installation
* Clone this repository.
	- `gh clone <reponame> && cd <reponame>`
* Check your version of Python ( Using >= 3.0.0 ).
	- `python --version`
	- If python is not up to date:
		+ Update to at least version 3.
	- If python is not installed:
		+ Download python for your machine.
* Install the requirements.
	- `pip install -r requirements.txt`
* Run `app.py`
	- `python app.py`

## Project Structure
```
WorkLog
|---- worklog
    |---- app.py
    |---- LogAPI
    	|---- Entry.py
    	|---- User.py
    	|---- LogHandler.py
    |---- LogFiles
```

## API
Below are the methods calls associated with each class used throughout the application.

### User
These methods handle creating, modifying, viewing, and greeting a user.

| Class    | Method        | Parameters           | Purpose                                   |
|----------|---------------|----------------------|-------------------------------------------|
| User     | `get_current` | None                 | Returns current user.                     |
|          | `get_company` | None                 | Returns user's organization.              |
|          | `get_role`    | None                 | Returns user's role @ organization.       |
|          | `set_company` | `new_company:string` | Establishes new org for the current user. |
|          | `set_current` | `new_username:string`| Establishes new current user.             |
|          | `set_role`    | `new_role:string`    | Establishes new role for current user.    |
|          | `greet`       | None                 | Greets the user with a message.           |
|          | `view`        | None                 | Displays the user key/value pairs.        |


### Entry
These methods handle creating, modifying, viewing, and saving an entry.

| Class    | Method            | Parameters              | Purpose                                    |
|----------|-------------------|-------------------------|--------------------------------------------|
| Entry    | `get_current`     | None                    | Returns current user.                      |
|          | `get_entries`     | None                    | Returns entries made during session.       |
|          | `set_current`     | `current_entry:string`  | Establishes current entry for seesion.     |
|          | `set_destination` | `new_destination:string`| Establishes a new output destination.      |
|          | `input`           | None                    | Triggers input loop.                       |
|          | `edit`            | `entry_to_edit:string`  | Edits a key's value (if key exists).       |
|          | `output`          | None                    | Outputs current entries to source file.    |
|          | `view_all`        | None                    | Displays the entrie's key/value pairs.     |


### LogHandler
These methods handle modifying and viewing saved entries.

| Class    | Method            | Parameters              | Purpose                                    |
|----------|-------------------|-------------------------|--------------------------------------------|
| Entry    | `get_log_list`    | None                    | Returns current user.                      |
|          | `delete_log`      | `log_name:string`       | Deletes entry's .txt file.                 |
|          | `read_entry`      | `log_name:string`       | Reads contents of a specific entry.        |
|          | `read_recent`     | None                    | Reads the most recent entry                |
|          | `view_deleted`    | None                    | View deleted files ( for session )         |

## Future Work
* Enable parsing of command line arguments for more liberal usage.
* Option to restore deleted files.

## Credit
[Jack L.](https://www.linkedin.com/in/jacklester/)
