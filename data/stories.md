version: "2.0"

## Story path 1

* greet
  - utter_greet
  
* booking
  - utter_enquiry_room_no

* room_no
  - utter_enquiry_room_type

* choose{"room_type": "Simple"}
  - utter_confirmation
  
* affirm
  - utter_done

## Story path2

* greet
  - utter_greet
  
* booking
  - utter_enquiry_room_no
  
* room_no
  - utter_enquiry_room_type
  
* choose{"room_type": "Deluxe"}
  - utter_confirmation
  
## Story path 3

* greet
  - utter_greet
  
* book+room_no
  - utter_enquiry_room_type

* choose{"room_type": "Simple"}
  - utter_confirmation

* affirm
  - utter_done

## Story path 4

* greet
  - utter_greet
  
* book+room_no
  - utter_enquiry_room_type

* choose{"room_type": "Simple"}
  - utter_confirmation

* affirm
  - utter_done
## Story path 5
* greet
  - utter_greet
* cleaning
  - utter_ask_time
* clean+time
  - action_relative
* affirm
  - utter_done
  
## Story path 6
* greet
  - utter_greet
* cleaning
  - utter_ask_time
* immediate
  - utter_cleaning_confirm
* affirm
  - utter_done

  ## Story path 7
* checkin
  - utter_checkin
 ## Story path 8
* checkout
  - utter_checkout
   ## Story path 9
* cancelreservation
  - utter_cancelreservation
   ## Story path 10
* cancellationpolicy
  - utter_cancellationpolicy
   ## Story path 11
* restaurant
  - utter_restaurant
   ## Story path 12
* breakfast
  - utter_breakfast
   ## Story path 13
* breakfasttimings
  - utter_breakfasttimings
   ## Story path 14
* restauranttimings
  - utter_restauranttimings
   ## Story path 15
* goodbye
  - utter_bye