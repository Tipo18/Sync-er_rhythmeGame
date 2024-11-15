# 🎵 Sync-er: A Rhythm Game in Python

**Sync-er** is an academic project developed as part of a coursework assignment. It's a rhythm game inspired by Guitar Hero, featuring a minimalist pixel-art aesthetic. The game is built using **Python** and **Pygame** with additional data analysis capabilities using **Matplotlib** and **Jupyter Notebooks**.

## 🚀 Features

- **Core Gameplay**: 
  - Hit the notes as they align with the target zone.
  - Tracks performance metrics such as perfect hits, streaks, and more.

- **Pixel-Art Aesthetic**:
  - Retro-style graphics with simple, pixelated designs.
  - Original visual assets created for this project.

- **Dynamic Difficulty**:
  - Game speed progressively increases based on player performance.

- **Leaderboard System**:
  - Tracks top scores for each player.
  - Displays total games played, points scored, and clicks registered in a leaderboard.

- **Data Logging**:
  - Player performance is saved in **CSV files** for post-game analysis.

- **Data Analysis**:
  - Jupyter Notebooks are used to analyze and visualize player performance trends.

## 📦 Project Structure

```
project/
├── src/
│   ├── main.py             # Main game logic
│   ├── assets/             # Game assets (images, sounds)
│   ├── Pixelify_Sans/      # Custom font
│   └── data/               # Folder for CSV data (auto-created for each player)
├── notebooks/
│   └── analysis.ipynb      # Jupyter Notebook for data visualization
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── .gitignore              # Ignored files and folders
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sync-er.git
   cd sync-er
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the game**:
   ```bash
   python src/main.py
   ```

## 🎮 How to Play

- **Menu Navigation**:
  - `ENTER`: Start a new game.
  - `L`: View the leaderboard.
  - `M`: Quit the game.
  
- **Gameplay**:
  - `A/Q`: Hit notes on different lines.
  - `P`: Pause the game.
  - Avoid missing notes; three misses will end the game.

## 📊 Data Analysis

After playing, analyze your performance data:

1. Navigate to the `notebooks/` folder.
2. Open the `analysis.ipynb` notebook:
   ```bash
   jupyter notebook notebooks/analysis.ipynb
   ```
3. Visualize trends such as:
   - Points vs. Game Duration
   - Performance evolution across games
   - Longest streaks and more.

### Example Plots

- **Points Distribution**:
  ![Points Distribution](assets/points_distribution.png)

- **Game Duration vs Points**:
  ![Game Duration vs Points](assets/game_duration_vs_points.png)

## 📝 CSV Data Format

Each player's performance is logged in a CSV file:

```csv
Creation_time_stamp,finished_game,finish_time_stamp,speed,point,validated_disk,perfect,great,ok,nb_click,missed_clicked,longest_streak,longest_grt_streak
2024-11-15 17:30:57,True,2024-11-15 17:31:49,16,3226,91,16,49,26,98,8,63,54
```

## 📋 Requirements

- Python 3.8+
- Pygame
- Matplotlib
- Pandas
- Jupyter Notebook

Install via:
```bash
pip install -r requirements.txt
```

## 🎨 Acknowledgements

- **Visual Assets**: All pixel-art visuals used in this project were created by me specifically for this academic project.
- **Font**: **Pixelify Sans**, used under free license.
- **Music**: The included music track is under a free license for non profit.

## 🤝 Contributing

This is an academic project, and contributions are not expected. However, feel free to fork the repository or use it as inspiration for your own projects.
