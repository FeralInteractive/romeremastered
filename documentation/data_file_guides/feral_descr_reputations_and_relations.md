![Workshop_header_template](/Workshop_header_template.png)
# feral_descr_reputations_and_relations.txt

## Table Of Contents

* [Introduction](#introduction)
   * [Example of default descr_campaigns.txt](#example-of-default-descr_campaignstxt)

## Introduction

This is a new addition for Rome Remastered. This file allows you to:

* Modify pre-existing modifiers from original Rome
* Modify new modifiers added to Rome Remastered.

The additional modifiers for positive behaviours and the ability to disable penalties for actions like bribing rebels should allow players and modders to avoid having factions repuations being constantly too low or high and improve the overall balance of the game.

See comments in the file for further details.

### Example of default descr_campaigns.txt

```
;;; Circumstances Increasing Reputation


; Reputation increases by value when the circumstance occurs, 10 is 1%

circumstance time
value 5

circumstance long_term_alliance
value 5

circumstance cancel_embargo
value 50

circumstance offer_compensation_accepted
value 50

circumstance ceasefire_accepted
value 50

circumstance offer_military_assist_accepted
value 100

circumstance ally_ally_of_ally
value 50


;;; Rebel Bribe Effect on Reputation

; Thing being bribed is type, 10 is 1%
; Original values in order were -40, -60, -70 and -110

rebel_type character
value 0

rebel_type army
value 0

rebel_type fort
value 0

rebel_type settlement
value 0


;;; Non-Rebel Bribe Effect on Reputation

; Thing being bribed is type, 10 is 1%

type character
value -40

type army
value -60

type fort
value -70

type settlement
value -110


;;; Relationship Bonus from Merchant Trade

; Income each merchant makes is divided by 20 and multiplied with the multiplier to affect relationship each turn
; 10 is 1% for cap and penalty
; Embargo penalty applies for each merchant in an embargo faction's borders and is limited to -cap

income_multiplier 1
cap 30
embargo_penalty 10
```
