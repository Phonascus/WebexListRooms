# Webex Spaces Exporter

This Python script retrieves a list of Webex spaces that the user is a member of and generates two files: `WebexSpaces.txt` and `WebexSpaces.csv`, containing the names of the spaces and links to them in plain text and tab-delineated CSV format, respectively.

## Prerequisites

- Python 3.x
- `requests` library
- `base64` library
- A valid Webex access token

## Setup

1. Clone the repository to your local machine.\
`git clone https://github.com/your-username/webex-spaces-exporter.git`\
`cd webex-spaces-exporter`

2. Install the required Python packages.\
`pip install requests`\
`pip install base64`

3. Update the script with your Webex access token.
Open the script in a text editor and replace `'YOUR_PERSONAL_ACCESS_TOKEN'` with your actual Webex access token.\
You can get a personal Webex API access token by logging in to the [Webex Developer Portal](https://developer.webex.com/docs/getting-started).

## Usage

Run the script from the command line:\
`python export_webex_spaces.py`


After execution, the script will create two files in the current directory:

- `WebexSpaces.txt`: A plain text file listing the names of Webex spaces and clickable links to open them in the Webex app.
- `WebexSpaces.csv`: A CSV file with the same information, tab-separated.

## Security Note

Please ensure that your Webex access token is stored securely and not exposed in the script or committed to version control. Use environment variables or other secure methods to manage sensitive credentials.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.