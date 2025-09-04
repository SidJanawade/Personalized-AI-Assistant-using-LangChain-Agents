# HR Bot

An intelligent HR management chatbot built with LangChain and Google's Gemini AI that helps automate common HR tasks like candidate management, interview scheduling, and leave management.

## Features

### Candidate Management
- **View Candidate Information**: Get detailed info about candidates including skills, experience, and status
- **Update Candidate Status**: Change recruitment status (Applied, Interviewed, Hired, etc.)
- **Search by Skills**: Find candidates with specific technical skills
- **Remove Candidates**: Delete candidate records from the system

### Interview Management
- **Schedule Interviews**: Book interview slots with candidates
- **Track Interview Status**: Monitor candidate progress through the hiring pipeline

### Leave Management
- **Apply for Leave**: Submit leave requests with dates and reasons
- **Check Leave Status**: View pending/approved/rejected leave requests
- **Approve/Reject Leave**: Manage leave requests for team members

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd hr-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Get Google API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key for Gemini
   - Add it to your `.env` file

## Usage

### Starting the Bot
```bash
python main.py
```

### Example Commands

#### Candidate Management
```
"Get info about Alice"
"Update Bob's status to Hired"
"Find candidates with Python skills"
"Remove candidate Charlie"
```

#### Interview Scheduling
```
"Schedule interview with Alice on 2024-12-15 at 10:00 AM"
```

#### Leave Management
```
"Apply leave for John on 2024-12-20 for vacation"
"Check leave status for Alice"
"Approve leave for Bob on 2024-12-18"
"Reject leave for Eve on 2024-12-22"
```

## Project Structure

```
hr-bot/
├── main.py              # Entry point and chat interface
├── agent.py             # LangChain agent configuration
├── tools.py             # HR tool implementations
├── memory.py            # Conversation memory management
├── candidates.csv       # Candidate database
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
└── README.md           # This file
```

## File Descriptions

- **main.py**: Contains the main chat loop and user interface
- **agent.py**: Configures the LangChain agent with Gemini AI and available tools
- **tools.py**: Implements all HR-related tools and functions
- **memory.py**: Manages conversation history and context
- **candidates.csv**: Stores candidate information and recruitment data

## Data Format

### Candidates CSV Structure
```csv
name,email,skills,status,experience,department,location
Alice,alice@example.com,"Python,ML",Applied,2,Data Science,Bangalore
```

### Tool Input Formats
- **Schedule Interview**: `Name | Date | Time`
- **Update Status**: `Name | NewStatus`
- **Apply Leave**: `Name | Date | Reason`
- **Approve/Reject Leave**: `Name | Date`

## Dependencies

- **langchain**: Framework for building LLM applications
- **langchain-google-genai**: Google Gemini AI integration
- **python-dotenv**: Environment variable management
- **pandas**: Data manipulation and CSV handling

## Sample Data

The project includes sample candidate data with:
- 10 candidates across different departments
- Various skill sets (Python, Java, JavaScript, etc.)
- Different recruitment statuses
- Multiple Indian city locations

## Commands to Exit

Type any of the following to exit the bot:
- `exit`
- `quit`

## Error Handling

The bot includes comprehensive error handling for:
- Invalid input formats
- Missing candidates
- File operations
- API communication issues

## Customization

### Adding New Tools
1. Define new tool functions in `tools.py` using the `@tool` decorator
2. Add the tool to the `tools` list in `agent.py`
3. The agent will automatically incorporate the new functionality

### Modifying Candidate Data
- Edit `candidates.csv` directly or use the bot's update functions
- The CSV file is automatically updated when using status change commands

## Troubleshooting

### Common Issues
1. **API Key Error**: Ensure your Google API key is valid and added to `.env`
2. **Module Not Found**: Run `pip install -r requirements.txt`
3. **CSV Issues**: Check that `candidates.csv` exists and has proper formatting
4. **Memory Issues**: Restart the bot if conversation memory becomes corrupted

### Debug Mode
The agent runs in verbose mode by default, showing tool usage and reasoning steps.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

