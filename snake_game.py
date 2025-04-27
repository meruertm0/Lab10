import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="SnakeGameDB",
    user="postgres",
    password="118523",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

print("Connected to database successfully!")
def get_user():
    username = input("Enter your username: ")
    
    # Check if user exists in database
    cur.execute("SELECT id, level FROM Users WHERE username = %s", (username,))
    user_data = cur.fetchone()

    if not user_data:
        cur.execute("INSERT INTO Users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        level = 1
        print(f"Welcome, {username}! Your level is set to {level}.")
    else:
        user_id, level = user_data
        print(f"Welcome back, {username}! You're on level {level}.")
    
    conn.commit()
    return user_id, level
def adjust_game_settings(level):
    if level == 1:
        speed = 5
        walls = False
    elif level == 2:
        speed = 10
        walls = True
    else:
        speed = 15
        walls = True

    print(f"Level {level} settings → Speed: {speed}, Walls: {walls}")
    return speed, walls
def save_game(user_id, current_score):
    cur.execute("UPDATE user_score SET score = %s WHERE user_id = %s", (current_score, user_id))
    conn.commit()
    print(f"Game paused! Score {current_score} saved.")
# Setup game
user_id, level = get_user()
speed, walls = adjust_game_settings(level)

# Simulated gameplay (Replace with actual game logic)
current_score = 100  # Example score from game
save_game(user_id, current_score)

# Close connection
cur.close()
conn.close()

