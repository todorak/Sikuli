import os

# Precondition
os.system("taskkill /IM chrome.exe /F")


##### RUN TESTS #####
os.system("fake cmd") # Workaround to enable colored logs
os.system(r"C:\mini-framework\Sikuli\runsikulix.cmd -r C:\mini-framework\Tests\smoke_tests.sikuli")


# Postcondition
os.system("taskkill /IM chrome.exe /F")