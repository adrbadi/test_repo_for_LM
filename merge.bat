@echo off
setlocal

REM Define the branches
set MAIN_BRANCH=Branch_to_merge
set RELEASE_BRANCH=main

REM Checkout the main branch and pull the latest changes
git checkout %MAIN_BRANCH%
git pull origin %MAIN_BRANCH%

REM Checkout the release branch
git checkout %RELEASE_BRANCH%

REM Merge the main branch into the release branch
git merge %MAIN_BRANCH%

REM Optional: Push the changes to the remote release branch
git push origin %RELEASE_BRANCH%

echo Merged changes from %MAIN_BRANCH% to %RELEASE_BRANCH%
endlocal
