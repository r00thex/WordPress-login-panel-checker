# WordPress-login-panel-checker

DESCRIPTION
-----------
This tool scans multiple URLs to detect WordPress login panels by Root hex
response content for WP-specific indicators such as wp-admin, wp-includes, 
and WordPress signatures. Perfect for penetration testers and security 
researchers to identify WordPress installations efficiently.

FEATURES
--------
- Fast multi-URL scanning
- Detects WordPress login panels accurately
- Saves valid WP-login URLs to valid.txt
- Real-time progress tracking
- Colored terminal output for better visibility
- Error handling and timeout support

REQUIREMENTS
------------
Python 3.6+
requests
urllib3
colorama

INSTALLATION
------------
pip install -r requirements.txt

USAGE
-----
1. Create a text file with list of domains (one per line)
   Example: 
   example.com
   testsite.com
   wordpress.org
- With Out (Http,Htpps)

2. Run the tool:
   python scanner.py

3. Enter the file path when prompted

OUTPUT
------
- Green: Valid WordPress login panel found
- Red: No WordPress panel detected
- Results saved to valid.txt

================================================================================
                     ROot society
                    Developed By git @r00thex
                  new account tg :- @r00the

================================================================================

DISCLAIMER
----------
This tool is for educational and authorized testing purposes only.
Users are responsible for complying with applicable laws and regulations.
