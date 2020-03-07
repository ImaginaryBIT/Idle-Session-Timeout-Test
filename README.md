# Idle Session Timeout Test (WSTG-SESS-007)
A handy tool to test idle session timeout. 

### Description:
This is a Idle Session Timeout test script
* Currently only support GET request
* Currently only support cookie based session
version 0.1

### How to use:
* Capture two requests from burp, one with valid session, another with invalid session after user logout.
* According to the request and response, fill in the headers, cookies, timeoutMsg and timeoutStatus

### Further improvement:
1. Improve it to command-line tool
2. Add validation of session timeout after valid cookie expired
3. Add idle session timeout for token based session
