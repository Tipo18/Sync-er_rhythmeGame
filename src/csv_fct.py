import os
import csv
from datetime import datetime

print("launch")

file_name = "tima.csv"

def csv_init(file_name,):
    if not os.path.isfile(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Creation_time_stamp", "finished_game", "finish_time_stamp", "speed", "point", 
                "validated_disk", "perfect", "great", "ok", "nb_click", 
                "missed_clicked", "longest_streak", "longest_grt_streak"
            ])
    
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        creation_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([creation_timestamp, False] + [""] * 11)

def csv_end(file_name):
    with open(file_name, mode='r', newline='') as file:
        reader = list(csv.reader(file))
        
    if len(reader) < 2:
        print("No game data to update.")
        return
        
    last_row_index = len(reader) - 1
    '''
    reader[last_row_index] = [
        reader[last_row_index][0],
        True, 
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        self.speed,
        self.point,
        self.validated_disk,
        self.perfect,
        self.great,
        self.ok,
        self.nb_click,
        self.missed_clicked,
        self.longest_streak,
        self.longest_grt_streak
        ]
    '''
    reader[last_row_index] = [
        reader[last_row_index][0],
        True, 
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        5,
        100,
        2,
        1,
        0,
        1,
        10,
        4,
        3,
        1
    ]
        
        # Rewrite the CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)

#csv_init(file_name)
#csv_end(file_name)


        
class Leaderboard:
    def __init__(self):
        self.nb_partie_tt = 0
        self.point_tt = 0
        self.b_click_tt = 0
        self.array_5_best = []

    def update_leaderboard(self):
        data_folder = "data"
        scores = []

        for file_name in os.listdir(data_folder):
            if file_name.endswith(".csv"):
                file_path = os.path.join(data_folder, file_name)
                
                with open(file_path, mode='r') as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        self.nb_partie_tt += 1

                        try:
                            self.point_tt += int(row.get("point", 0) or 0)
                            self.b_click_tt += int(row.get("nb_click", 0) or 0)
                            scores.append(int(row.get("point", 0) or 0))
                        except ValueError:
                            print(f"Skipping invalid data in {file_name}: {row}")

        # Get top 5 scores
        self.array_5_best = sorted(scores, reverse=True)[:5]

        # Print results for verification
        print(f"Total games played: {self.nb_partie_tt}")
        print(f"Total points: {self.point_tt}")
        print(f"Total clicks: {self.b_click_tt}")
        print(f"Top 5 scores: {self.array_5_best}")

# Usage
leaderboard = Leaderboard()
leaderboard.update_leaderboard()