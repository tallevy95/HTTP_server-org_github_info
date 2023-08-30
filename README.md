# HTTP_server-org_github_info
Home Assignment

	In this assignment, I was requested to write an HTTP server that provides information about
	a GitHub organization's repositories.


Description:
	
	- main.py will generate a HTTP server using Flask that contains the requested information.

	The requested information:
	- Name
	- Owner
	- URL
	- Creation time
	- Number of stars

	Given an organization name and a phrase, return a list containing the organization's
	visible repositories that match the provided phrase. 
 	If no phrase is provided, the endpoint should return the unfiltered list.

Installation:
	
	1. Clone the repository: git clone https://github.com/tallevy95/HTTP_server-org_github_info.git
	2. Change the directory: cd HTTP_server-org_github_info
	3. Install dependencies: pip install -r requirements.txt
	4. Run the project: python main.py
	   * <Organization> is a must (i.e: gofireflyio, aws, microsoft, etc.)
	   * <Phrase> optional - default value is None (must be length 3 or more)

Usage:
	
	To use this project, follow these steps:
		1. Run the project: python main.py
		2. Copy and paste this URL in your browser: http://127.0.0.1:5000/<Organization>
  		   Change the <Organization> name to the wanted organization name (i.e: gofireflyio, aws, microsoft, etc.).
       		3. Optional - if you wish to filter by a phrase, then copy and paste this URL: 
	 	   http://127.0.0.1:5000/<Organization>/<Phrase>
		   Change the <Phrase> to the requested filter.
