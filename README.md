# HTTP_server-organization_github_info
Junior SW Engineer - Home Assignment

	In this assignment, I was requested to write an HTTP server that provides information about
	a GitHub organization's repositories.


Description:
	
	- approach_1.py will generate a data.csv file that contains the wanted information (more on that later).
	- approach_2.py will generate a HTTP server using Flask that contains the wanted information (more on that later).

	The wanted information:
	- Name
	- Owner
	- URL
	- Creation Time
	- Number of stars

Installation:
	
	1. Clone the repository: git clone https://github.com/tallevy95/HTTP_server-organization_github_info.git
	2. Change the directory: cd HTTP_server-organization_github_info
	3. Install dependencies: pip install -r requirements.txt
	4. Run the project: python approach_<Number>.py  <Organization> <Phrase>
	   * <Number> can be 1 or 2
	   * <Organization> is a must 
	   * <Phrase> default value is None (has to be in length 3 or more)

Usage:
	
	To use this project, follow these steps:
		1. run the selected approach as mention above.
		2-a. for approach_1: open the csv file in the directory of the program.
		2-b. for approach_2: open the given url from the CMD, http://127.0.0.1:5000
