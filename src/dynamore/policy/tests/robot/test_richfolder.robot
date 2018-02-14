# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s dynamore.policy -t test_richfolder.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src dynamore.policy.testing.DYNAMORE_POLICY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_richfolder.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a richfolder
  Given a logged-in site administrator
    and an add richfolder form
   When I type 'My RichFolder' into the title field
    and I submit the form
   Then a richfolder with the title 'My RichFolder' has been created

Scenario: As a site administrator I can view a richfolder
  Given a logged-in site administrator
    and a richfolder 'My RichFolder'
   When I go to the richfolder view
   Then I can see the richfolder title 'My RichFolder'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add richfolder form
  Go To  ${PLONE_URL}/++add++richfolder

a richfolder 'My RichFolder'
  Create content  type=richfolder  id=my-richfolder  title=My RichFolder


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IDublinCore.title  ${title}

I submit the form
  Click Button  Save

I go to the richfolder view
  Go To  ${PLONE_URL}/my-richfolder
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a richfolder with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the richfolder title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
