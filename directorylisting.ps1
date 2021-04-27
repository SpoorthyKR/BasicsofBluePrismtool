$a = dir "C:\program files (x86)\Blue Prism Limited\Blue Prism Automate" -Recurse 
$a | out-file -encoding ascii "c:\codestage\powershell\outputs\directoryoutput.txt"