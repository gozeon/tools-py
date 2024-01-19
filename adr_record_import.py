import csv
import time

with open("sql.txt", 'w', encoding="utf8") as w:
    w.write("INSERT INTO `records` (`created_at`, `updated_at`, `deleted_at`, `title`, `description`, `status`, `project_id`) VALUES\n")

    with open('records.csv', 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            print(row)
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            w.write("('{now}', '{now}', NULL, '{title}', '', {status}, {project_id}),\n".format(
                now=now,
                title=row['title'],
                status= 1 or row['status'],
                project_id= 12 or row["project_id"] 
            ))
    f.close()
w.close()
