# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s dynamore.policy -t test_dynaperson.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src dynamore.policy.testing.DYNAMORE_POLICY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_dynaperson.robot
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

Scenario: As a site administrator I can add a dynaperson
  Given a logged-in site administrator
    and an add dynaperson form
   When I type 'My DynaPerson' into the title field
    and I submit the form
   Then a dynaperson with the title 'My DynaPerson' has been created

Scenario: As a site administrator I can view a dynaperson
  Given a logged-in site administrator
    and a dynaperson 'My DynaPerson'
   When I go to the dynaperson view
   Then I can see the dynaperson title 'My DynaPerson'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add dynaperson form
  Go To  ${PLONE_URL}/++add++dynaperson

a dynaperson 'My DynaPerson'
  Create content  type=dynaperson  id=my-dynaperson  title=My DynaPerson


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IDublinCore.title  ${title}

I submit the form
  Click Button  Save

I go to the dynaperson view
  Go To  ${PLONE_URL}/my-dynaperson
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a dynaperson with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the dynaperson title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
