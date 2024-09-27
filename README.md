# Tweet Insult Detector

This project uses the Twitter API to fetch mentions directed at the user and utilizes an artificial intelligence model to detect insults within those mentions. The identified data is then reported.

## Features

- Fetch mentions using the Twitter API
- Utilize Hugging Face model for insult detection
- Reporting system

## Requirements

- Python 3.7 or higher
- `tweepy` library
- `transformers` library
- `dotenv` library

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mertcanureten/tweet-insult-detector.git
   cd tweet-insult-detector
   ```

2. **Install Required Libraries**

   ```bash
   pip install -r requirements.txt
   ```

3. **Define Twitter API Keys**

   Create a `.env` file and add the following keys:

   ```plaintext
   API_KEY=your_api_key
   API_SECRET=your_api_secret
   ACCESS_TOKEN=your_access_token
   ACCESS_SECRET=your_access_secret
   ```

## Usage

To start the main application, run:

```bash
python main.py
```

### Code Structure

- `twitter_api.py`: Module for connecting to the Twitter API and fetching mentions.
- `text_cleaning.py`: Helper module for cleaning tweet texts.
- `insult_detection.py`: Module for detecting insults using the Hugging Face model.
- `report_generation.py`: Module for reporting detected insults.
- `requirements.txt`: File containing the necessary libraries for the project.

## Contributing

If you'd like to contribute to this project, please feel free to create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
