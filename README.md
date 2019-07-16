<h1>Introduction</h1>
<p>This script is for use with Python 3. It can be run with a Python command line. There are several steps involved in extracting the relevant articles from a batch of Outlook e-mail messages (.msg format). These are outlined below.</p>

<h1>Step 1: Saving Outlook messages as a text file</h1>
<p>From within the Microsoft Outlook desktop client, you can select messages from your inbox (or specific folder), and using 'save as' select '.txt' to save to a specific location on your device. Call the file 'Emails_Summary.txt'. For further details, see the following web page: https://support.office.com/en-us/article/save-a-message-as-a-file-4821bcd4-7687-4d6d-a486-b89a291a56e2</p>

<h1>Step 2: Creating your target file</h1>
<p>Now that you have the source file, create a new (empty) text file in the same directory called 'Emails_Relevant.txt'.</p>

<h1>Step 3: Creating your Python scripts</h1>
<p>Download the 'email_batch_summary.py' and 'write_out.py' scripts and save these to the same directory.</p>

<h1>Step 4: Testing your script in the Python Shell</h1>
<p>To test out the script on the contents of your 'Emails_Summary.txt' source file, run the 'email_batch_summary.py' in your command line or preferred Python environment. You can edit the keyword in the script to one (or more, using boolean operators) of your choosing. You should have a read out in the Python shell of lines that match your conditional statement.</p>

<h1>Step 5: Writing results to another text file</h1>
<p>To write the results to another text file, run the 'write_out.py' script (with appropriate amendments to the keyword(s)). Now navigate to the file directory and open 'Emails_Relevant.txt' and you should see the list of lines that matched your conditional statement. This can be copied and pasted into another word processor, and if the URLs are enclosed in '<' and '>', these can be read as hyperlinks.</p>
