# 🚀 Trello SCRUM Progress Tracker Bot

The **Trello Progress Tracker Bot** is a tool designed to analyze tasks from the "Projeto Integrador I" subject on Trello and produce reports. While it's straightforward in its approach, it ensures that the task progress is presented clearly and efficiently.

## 🌟 Features

- **🏷️ Labels Analysis**: 
  - **📊 Difficulty**: A tag ranging from `10` to `100`. Note: A difficulty of `0` is not allowed, as it would imply the absence of a task.
  - **📑 Criteria**: Enumeration of criteria as specified in the problem's PDF.

- **📡 Data Retrieval**: 
  - Utilizes the Trello API to fetch data.

- **📈 Reports Generation**: 
  - 📉 A chart showing the accumulated actual score against the accumulated estimated score over time.
  - 📋 A list of criteria and the tasks addressing them.

## ⚙️ Configuration

| Constant | Description |
|----------|-------------|
| `TRELLO_API_LINK` | The link to the Trello API. |
| `TRELLO_BOARD_ID` | The unique ID of the Trello board. |
| `IGNORE_LIST_IDS` | List IDs that should be ignored during data retrieval. |
| `IGNORE_CARDS_IDS` | Card IDs that should be ignored. |
| `DONE_LIST_ID` | The ID of the list (or column) where completed tasks (cards) are placed. |

## 🛠️ How It Works

1. **Data Fetching**: `main.py` retrieves cards from Trello.
2. **Data Processing**: Sorts cards, calculates accumulated difficulty, and maps criteria to their respective tasks.
3. **Report Generation**: `output_utils.py` creates a difficulty chart and an Excel report.
4. **API Integration**: `trello_api.py` manages the interaction with the Trello API.
5. **Execution**: `trello_tracker.bat` serves as the entry point.

## 🚀 Usage

To run the bot:

```bash
./trello_tracker.bat
```

### Upon execution:

📊 A difficulty chart is generated and saved as a PNG in the output directory.
📄 An Excel report detailing the relationship between criteria and tasks is produced.

## 🤝 Contributing
Open source contributions are welcome:

1. **Fork** the repository.
2. Create a **new branch**.
3. Commit your changes.
4. Submit a **pull request**.
