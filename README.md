## Description

This command line interface (CLI) application fetches and displays information about popular, top-rated, upcoming, and now playing movies from The Movie Database (TMDB).

# Prerequisites

· Python 3.x
· TMDB API key

## Installation

1. Clone or download this project to your machine
2. Install the required dependencies:

```
pip install requests
```

## Configuration

1. Get a free TMDB API key by creating an account at https://www.themoviedb.org/settings/api
2. Set up your API key as an environment variable:
   · On Linux/macOS:
     ```bash
     export TMDB_API_KEY="your_api_key_here"
     ```
   · On Windows (Command Prompt):
     ```cmd
     set TMDB_API_KEY=your_api_key_here
     ```
   · On Windows (PowerShell):
     ```powershell
     $env:TMDB_API_KEY="your_api_key_here"
     ```

## Usage

Run the application with one of the following commands:

```bash
python tmdb-app.py --type "playing"    # Now playing movies
python tmdb-app.py --type "popular"    # Popular movies
python tmdb-app.py --type "top"        # Top rated movies
python tmdb-app.py --type "upcoming"   # Upcoming movies
```

## Features

· Displays movies with title, release date, and synopsis
· Handles API and network errors gracefully
· Simple and intuitive command line interface

## Original Project

This project is part of the roadmap.sh: URL:https://roadmap.sh/projects/tmdb-cli

## Code Structure

## The code uses:

· argparse to handle command line arguments
· requests to make API calls to TMDB
· Error handling for network or API issues

## Known Limitations

· Limited to the first page of results (20 movies)
· Language fixed to English (en-US)
