import re
import collections
import logging

# Set up logging
logging.basicConfig(filename='log_analyzer.log', level=logging.INFO)

# Define log file path and patterns
LOG_FILE = 'access.log'
PATTERNS = {
    'IP_ADDRESS': r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
    'REQUEST_METHOD': r'\b(GET|POST|PUT|DELETE|HEAD|OPTIONS|CONNECT|PATCH)\b',
    'REQUEST_URI': r'\b([^ ]+)\b',
    'HTTP_STATUS_CODE': r'\b\d{3}\b',
    'USER_AGENT': r'\b([^"]+)\b'
}

def parse_log_line(line):
    ip_address = re.search(PATTERNS['IP_ADDRESS'], line).group()
    request_method = re.search(PATTERNS['REQUEST_METHOD'], line).group()
    request_uri = re.search(PATTERNS['REQUEST_URI'], line).group()
    http_status_code = int(re.search(PATTERNS['HTTP_STATUS_CODE'], line).group())
    user_agent = re.search(PATTERNS['USER_AGENT'], line).group()
    return {
        'ip_address': ip_address,
        'equest_method': request_method,
        'equest_uri': request_uri,
        'http_status_code': http_status_code,
        'user_agent': user_agent
    }

def analyze_log_file(log_file):
    ip_addresses = collections.defaultdict(int)
    request_uris = collections.defaultdict(int)
    http_status_codes = collections.defaultdict(int)
    user_agents = collections.defaultdict(int)

    with open(log_file, 'r') as f:
        for line in f:
            log_data = parse_log_line(line)
            ip_addresses[log_data['ip_address']] += 1
            request_uris[log_data['request_uri']] += 1
            http_status_codes[log_data['http_status_code']] += 1
            user_agents[log_data['user_agent']] += 1

    return {
        'ip_addresses': ip_addresses,
        'equest_uris': request_uris,
        'http_status_codes': http_status_codes,
        'user_agents': user_agents
    }

def generate_report(analyzed_data):
    report = ''
    report += 'Top 10 IP Addresses by Request Count:\n'
    for ip_address, count in sorted(analyzed_data['ip_addresses'].items(), key=lambda x: x[1], reverse=True)[:10]:
        report += f'{ip_address}: {count}\n'
    report += '\n'

    report += 'Top 10 Requested URIs:\n'
    for request_uri, count in sorted(analyzed_data['request_uris'].items(), key=lambda x: x[1], reverse=True)[:10]:
        report += f'{request_uri}: {count}\n'
    report += '\n'

    report += 'HTTP Status Code Distribution:\n'
    for http_status_code, count in analyzed_data['http_status_codes'].items():
        report += f'{http_status_code}: {count}\n'
    report += '\n'

    report += 'Top 10 User Agents by Request Count:\n'
    for user_agent, count in sorted(analyzed_data['user_agents'].items(), key=lambda x: x[1], reverse=True)[:10]:
        report += f'{user_agent}: {count}\n'
    report += '\n'

    return report

def main():
    analyzed_data = analyze_log_file(LOG_FILE)
    report = generate_report(analyzed_data)
    print(report)
    logging.info('Log analysis complete')

if __name__ == '__main__':
    main()