@echo off
setlocal

REM Define the branches
set MAIN_BRANCH=DEVELOPMENT_1
set RELEASE_BRANCH=main

REM Checkout the main branch and pull the latest changes
git checkout %MAIN_BRANCH%
git pull origin %MAIN_BRANCH%

REM Checkout the release branch
git checkout %RELEASE_BRANCH%

REM Merge the main branch into the release branch
git merge %MAIN_BRANCH%

REM Optional: Push the changes to the remote release branch
<<<<<<< HEAD
git push origin %RELEASE_BRANCH%
=======
REM git push origin %RELEASE_BRANCH%
>>>>>>> DEVELOPMENT_1

echo Merged changes from %MAIN_BRANCH% to %RELEASE_BRANCH%
endlocal
