<><><><><><><><><><><><><><><><><><><><>
Readme or Instructions for 1st-System-health.py :

Let me explain what this script does:

It imports the psutil library, which provides an interface to access system details, and the logging library, which allows us to log messages to a file.
It sets up logging to a file named system_health.log with an info level.
It defines three thresholds: CPU usage, memory usage, and disk usage. If any of these metrics exceed these thresholds, the script will log a warning message.
The script defines four functions to retrieve system metrics:
get_cpu_usage(): returns the current CPU usage as a percentage.
get_memory_usage(): returns the current memory usage as a percentage.
get_disk_usage(): returns the current disk usage as a percentage.
get_running_processes(): returns the number of running processes.
The check_system_health() function retrieves the system metrics, checks if any of them exceed the thresholds, and logs warning messages if necessary. It also logs an info message with the number of running processes.
The script runs an infinite loop, calling check_system_health() every 10 seconds using time.sleep(10).
To use this script, save it to a file (e.g., system_health.py), make it executable with chmod +x system_health.py, and then run it with ./system_health.py. The script will log messages to system_health.log and print the system health metrics to the console every 10 seconds.

Note: You can adjust the thresholds and logging levels to suit your needs. Additionally, you can modify the script to send alerts to a notification service or email instead of logging to a file.

<><><><><><><><><><><><><><><><><><><><><><>

For 2nd Problem Statement or 2nd-backup.py

Let me explain what this script does:

It imports the necessary libraries: os for file system operations, paramiko for SSH and SCP connections, datetime for timestamping, and logging for logging messages.
It sets up logging to a file named backup.log with an info level.
It defines the backup settings: LOCAL_DIR is the local directory to backup, REMOTE_DIR is the remote directory to store the backup, REMOTE_HOST is the remote server IP, REMOTE_USER is the remote server username, and REMOTE_PASSWORD is the remote server password.
The create_ssh_client() function creates an SSH client using Paramiko and connects to the remote server.
The backup_directory() function takes the SSH client, local directory, and remote directory as arguments. It creates the remote directory if it doesn't exist, and then uses SCP to transfer the files from the local directory to the remote directory.
The main() function creates an SSH client, calls backup_directory() to perform the backup, and logs the result.
The script runs the main() function when executed.
To use this script, save it to a file (e.g., backup.py), replace the placeholders with your actual backup settings, and then run it with python backup.py. The script will log messages to backup.log and print the result of the backup operation to the console.

<><><><><><><><><><><><><><><><><><><><><>

For 3rd-log-file-analyzer.py or 3rd Problem Statement

Let me explain what this script does:

It imports the necessary libraries: re for regular expressions, collections for data structures, and logging for logging messages.
It sets up logging to a file named log_analyzer.log with an info level.
It defines the log file path and patterns for extracting data from log lines.
The parse_log_line() function takes a log line as input and extracts the IP address, request method, request URI, HTTP status code, and user agent using regular expressions.
The analyze_log_file() function reads the log file line by line, parses each line using parse_log_line(), and updates four dictionaries to store the data: ip_addresses, request_uris, http_status_codes, and user_agents.
The generate_report() function takes the analyzed data as input and generates a summarized report with the top 10 IP addresses by request count, top 10 requested URIs, HTTP status code distribution, and top 10 user agents by request count.
The main() function calls analyze_log_file() to analyze the log

<><><><><><><><><><><><><><><><><><><><><><>

For 4th-app-health-checker.py or 4th Problem Statement

Let me explain what this script does:

It imports the necessary libraries: requests for sending HTTP requests, time for sleeping between checks, and logging for logging messages.
It sets up logging to a file named app_health_checker.log with an info level.
It defines the application URL and the expected HTTP status code (200 OK) that indicates the application is functioning correctly.
The check_app_status() function sends a GET request to the application URL using requests.get() and checks the response status code. If the status code matches the expected value, it returns 'up', indicating the application is functioning correctly. Otherwise, it returns 'down'.
The main() function runs an infinite loop that checks the application status every 1 minute using check_app_status(). It logs the result to the log file, including the HTTP status code if the application is down.
The script runs the main() function when executed.
To use this script, save it to a file (e.g., app_health_checker.py), replace the APP_URL variable with the URL of the application you want to monitor, and run it with python app_health_checker.py. The script will log the application status to app_health_checker.log every 1 minute.


<><><><><><><><><><><><><><><><><><><><><><>
Thanks For Reading this.
Writer -> Karan Singh (https://github.com/karansingh2004)
<><><><><><><><><><><><><><><><><><><><><><>
