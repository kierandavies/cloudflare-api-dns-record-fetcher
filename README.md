# Cloudflare DNS Record Fetcher
## cloudflare-api-dns-record-fetcher

This script allows you to fetch DNS records for a given domain from the Cloudflare API.

## Prerequisites

Before running this script, ensure you have the following:

- Python 3 installed on your system
- `requests` library installed. You can install it using `pip install requests`.

## Usage

1. Replace the placeholder values with your actual Cloudflare API key, email address, and domain name:

    ```python
    api_key = 'API_KEY'
    email = 'EMAIL_ADDRESS'
    domain = 'DOMAIN_NAME'
    ```

2. Save the script to a file with a `.py` extension, for example, `cloudflare_dns_fetcher.py`.

3. Open a terminal or command prompt and navigate to the directory where the script is saved.

4. Run the script using the command:

    ```bash
    python cloudflare_dns_fetcher.py
    ```

## Script Explanation

The script contains the following functions:

- `get_zone_id(domain)`: Retrieves the Zone ID for the specified domain from Cloudflare.
- `get_dns_records(domain)`: Retrieves the DNS records for the specified domain from Cloudflare.
- `main()`: The main entry point of the script that fetches and prints the DNS records.

The script performs the following steps:

1. It uses the `get_zone_id()` function to obtain the Zone ID for the provided domain.
2. With the Zone ID, it calls the `get_dns_records()` function to fetch all the DNS records associated with the domain.
3. It then iterates over the DNS records and prints the record type, name, and content.

Note: Ensure that you have proper permissions and valid credentials to access the Cloudflare API.

## License

This script is licensed under the [MIT License](LICENSE).
