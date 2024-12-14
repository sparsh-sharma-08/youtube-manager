import sqlite3

conn=sqlite3.connect('youtube_database.db')
cursor=conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    print('_'*40)
    for row in cursor.fetchall():
        print(row)
    print('_'*40)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (Name, Time) VALUES (?,?)",(name,time))
    conn.commit()
    print(f"Video '{name}' added successfully. ")

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name =?, time=? WHERE id=?", (name,time,video_id))
    conn.commit()
    print(f"Video with ID '{video_id}' has been Updated Successfully! ")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?", (video_id,))
    conn.commit()
    print(f"Video with ID {video_id} has been Deleted Successfully! ")

def main():
    try:  
        while True:
            print("Youtube Manager with DB || Choose anything to begin")
            print("1. List Videos")
            print("2. Add Videos")
            print("3. Update Videos")
            print("4. Delete Video")
            print("5. Exit Program")
            user_input=input("Enter Your Choice: ")
            match user_input:
                case "1":
                    list_videos()
                case "2":
                    name=input("Enter the video name: ")
                    time=input("Enter the video time: ")
                    add_video(name,time)
                case "3":
                    video_id=input("Enter video ID to update: ")
                    name=input("Enter the video name: ")
                    time=input("Enter the video time: ")
                    update_video(video_id,name,time)
                case "4":
                    video_id=input("Enter video ID to delete: ")
                    delete_video(video_id)
                case "5":
                    break
                case _:
                    print("Please enter a valid choice! ")
    finally:
        conn.close()

if __name__ =="__main__":
    main()