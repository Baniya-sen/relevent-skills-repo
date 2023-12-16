-- Keep a log of any SQL queries you execute as you solve the mystery. Fiftyville keeps records on SQL tables.
-- CS50 duck stolen. Duck may had something valuable inside. Gold? Diamonds? Maybe. That's why it is necessary to find theif.
-- Information so far, Theft took place aroung 10:15 AM on 28 july 2021. Emma's bakerey is spot.

-- First command, to scheme the database
.schema

-- Then details of crime_scene_reports of first hand information
SELECT * FROM crime_scene_reports;

-- Shorten the search for day of crime
SELECT * FROM crime_scene_reports
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28;

-- After reading the report for the crime, need to look at the interviews
SELECT * FROM interviews
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28;

-- After going through interviews, there is some leads.
-- Ruth said she saw theif taking his parked car from emma's bakerey within 10 minutes(approx.) after theft.
-- Eugene said theif was someone he knew but he don't know his name. He saw him that morning inside ATM withdrawing money on leggett street.
-- As he was leaving bakerey, Raymond saw theif calling someone, and heard talking them with someone.
-- Other end booked the next day's earliest flight out of fiftyville. Call duration was less than 1 minute.
-- Lead now is, parking lot security footage of bakerey, and ATM, call, and flight records.

-- Ruths lead:
-- Checking bakery_security_logs for car details
SELECT * FROM bakery_security_logs
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28;

-- There is no one exited bakerey after 8:59 till 10:16. Ruth said thief did leave within 10 mins so need to check timeframe.
SELECT COUNT(*) FROM bakery_security_logs
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
     AND hour IS 10
     AND minute > 15
     AND minute < 25;

-- Their are 8 people left bakerey within 10 mintues after theft and their number plates are
SELECT license_plate FROM bakery_security_logs
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
     AND hour IS 10
     AND minute > 15
     AND minute < 25;

-- Eugene's lead:
-- Checking ATM transactions of that morning
SELECT * FROM atm_transactions
  WHERE atm_location IS 'Leggett Street'
     AND transaction_type IS 'withdraw'
       AND year IS 2021
       AND month IS 7
       AND day IS 28;

SELECT COUNT(*) FROM atm_transactions
  WHERE atm_location IS 'Leggett Street'
     AND transaction_type IS 'withdraw'
       AND year IS 2021
       AND month IS 7
       AND day IS 28;

-- There are 8 transaction of withdraw from ATM at leggett street. Can't narrow it down right now. Will come to it later.

-- Raymonds lead:
-- Need to check phone calls
SELECT * FROM phone_calls
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28;

-- Need to check call logs with duration less than 60 seconds
SELECT caller FROM phone_calls
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
       AND duration < 60;

-- There were 9 calls that were less than 60 seconds in duration. Will come to this later
SELECT COUNT(*) FROM phone_calls
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
       AND duration < 60;

-- Now flights records
-- Theif's accomplice booked first flight out of fiftyville next day i.e. 29 july
SELECT * FROM flights
     JOIN airports
       ON flights.origin_airport_id = airports.id
  WHERE year IS 2021
     AND month IS 7
     AND day IS 29
        AND city LIKE 'Fiftyville'
        ORDER BY hour;

-- The first flight out of fiftyville departed about 8:20 and was to airport id #4, which is:
SELECT * FROM airports
  WHERE id IS 4;
-- LGA- LaGuardia Airport | New York City

-- Now I am gonna look at all passengers details for that particular flight
SELECT passport_number FROM passengers
     JOIN flights
     ON passengers.flight_id = flights.id
  WHERE flights.year IS 2021
     AND flights.month IS 7
     AND flights.day IS 29
     AND flights.hour IS 8
     AND flights.minute IS 20
        ORDER BY flights.hour;

-- Now time to look at peoples id with licence plate that were found at bakery_security_logs
SELECT name FROM people
    JOIN bakery_security_logs
    ON people.license_plate =  bakery_security_logs.license_plate
  WHERE bakery_security_logs.year IS 2021
     AND bakery_security_logs.month IS 7
     AND bakery_security_logs.day IS 28
     AND bakery_security_logs.hour IS 10
     AND bakery_security_logs.minute > 15
     AND bakery_security_logs.minute < 25;

-- Now id of those people who have taken first flight out of fiftyville on 29 july
SELECT name FROM people
     JOIN passengers
     ON people.passport_number = passengers.passport_number
     JOIN flights
     ON passengers.flight_id = flights.id
  WHERE flights.year IS 2021
     AND flights.month IS 7
     AND flights.day IS 29
     AND flights.hour IS 8
     AND flights.minute IS 20
        ORDER BY flights.hour;
-- Even though i can see some comman names between these two, need for details

-- Now its turn for phone records, names of those peoples who called someone just after theft to book flights
SELECT name FROM people
     JOIN phone_calls
     ON people.phone_number = phone_calls.caller
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
       AND duration < 60;


-- Now its time to combine all name and find distinct name that must be our little thiefs
SELECT name FROM people
     JOIN phone_calls
     ON people.phone_number = phone_calls.caller
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
       AND duration < 60

INTERSECT

SELECT name FROM people
     JOIN passengers
     ON people.passport_number = passengers.passport_number
     JOIN flights
     ON passengers.flight_id = flights.id
  WHERE flights.year IS 2021
     AND flights.month IS 7
     AND flights.day IS 29
     AND flights.hour IS 8
     AND flights.minute IS 20

INTERSECT

SELECT name FROM people
    JOIN bakery_security_logs
    ON people.license_plate = bakery_security_logs.license_plate
  WHERE bakery_security_logs.year IS 2021
     AND bakery_security_logs.month IS 7
     AND bakery_security_logs.day IS 28
     AND bakery_security_logs.hour IS 10
     AND bakery_security_logs.minute > 15
     AND bakery_security_logs.minute < 25;

-- There are three names, name that are comman between all these data. [Bruce, Kelsey, Sofia]
-- Mostly likely a name will emerge that will be our little thief surely. But for now i am stuck!

-- I got a lead! There accomplice of thief booked flight right? So if i can check who booked flight
-- out of fiftyville and cross-check it with these 3 names, Voila! Both will get caught!

-- Names of all who received call winthin 10 mins after theft and duration was less than 1 mintue.
-- Cross-check with names of people who were at the same flight
SELECT name FROM people
     JOIN phone_calls
     ON people.phone_number = phone_calls.receiver
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
       AND duration < 60

INTERSECT

SELECT name FROM people
     JOIN passengers
     ON people.passport_number = passengers.passport_number
     JOIN flights
     ON passengers.flight_id = flights.id
  WHERE flights.year IS 2021
     AND flights.month IS 7
     AND flights.day IS 29
     AND flights.hour IS 8
     AND flights.minute IS 20;
-- DORIS! ONly name that cross-verified at both places!

-- Now need to check who talked to doris at that time after theft
SELECT caller, receiver, name AS receivers_name FROM phone_calls
     JOIN people
     ON phone_calls.receiver = people.phone_number
        AND people.name LIKE 'Doris'
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
     AND duration < 60;

-- One number came who talked to doris at that time after theft, and their name is:
SELECT name FROM people
  WHERE phone_number IS
   (SELECT caller FROM phone_calls
      JOIN people
      ON phone_calls.receiver = people.phone_number
         AND people.name LIKE 'Doris'
   WHERE year IS 2021
      AND month IS 7
      AND day IS 28
      AND duration < 60);
-- Name that came forword is kenny! Hmm.. Kenny was not in those 3 peoples. Need to investigate more.

-- While my through investigation says after reviewing my data, Kenny's name came after search of phone records, he talked to doris.
-- The first flight out of fiftyville was on 8:20, doris and kenny was present on that flight.
-- But licence plate did'nt checks out, means he may not be at bakerey or using his own car.
-- Need to check ATM transactions.

-- Here are all persons who withdrew money in morning on the day of theft
SELECT * FROM bank_accounts
     JOIN atm_transactions
     ON bank_accounts.account_number = atm_transactions.account_number
       WHERE atm_location IS 'Leggett Street'
          AND transaction_type IS 'withdraw'
             AND year IS 2021
             AND month IS 7
             AND day IS 28;

SELECT name FROM people
     JOIN bank_accounts
     ON people.id = bank_accounts.person_id
         JOIN atm_transactions
         ON bank_accounts.account_number = atm_transactions.account_number
            WHERE atm_location IS 'Leggett Street'
               AND transaction_type IS 'withdraw'
                  AND year IS 2021
                  AND month IS 7
                  AND day IS 28;
-- Here is also, Kenny's name came out at ATM on leggett street who withdrew money on 28 july morning.


-- Now we cross verify all data to verrify kenny's name:
-- We would take the names of all who withdew money on 28 july,
-- then names of all who traveled out of fiftyville on 29 july,
-- and then names of all who called someone after theft and duration was less than a minute,
-- Lastly, name of person who talked to doris after theft
-- (Because Doris is only one who received a call just after theft, duration < 1 minute, and, doris was present in flight)
SELECT name FROM people
     JOIN bank_accounts
     ON people.id = bank_accounts.person_id
         JOIN atm_transactions
         ON bank_accounts.account_number = atm_transactions.account_number
            WHERE atm_location IS 'Leggett Street'
               AND transaction_type IS 'withdraw'
                  AND year IS 2021
                  AND month IS 7
                  AND day IS 28

INTERSECT

SELECT name FROM people
     JOIN passengers
     ON people.passport_number = passengers.passport_number
     JOIN flights
     ON passengers.flight_id = flights.id
  WHERE flights.year IS 2021
     AND flights.month IS 7
     AND flights.day IS 29
     AND flights.hour IS 8
     AND flights.minute IS 20

INTERSECT

SELECT name FROM people
     JOIN phone_calls
     ON people.phone_number = phone_calls.caller
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
       AND duration < 60

INTERSECT

SELECT name FROM people
  WHERE phone_number IS
   (SELECT caller FROM phone_calls
      JOIN people
      ON phone_calls.receiver = people.phone_number
         AND people.name LIKE 'Doris'
   WHERE year IS 2021
      AND month IS 7
      AND day IS 28
      AND duration < 60);

-- After all, Kenny, is the culprit, and Doris was his accomplice, according to me!
-- After check cs50 rejected my answer, i checked again... if i do not count the instance who talked to doris,
-- then Bruce name did caught up in many senerios. Like atm transaction, on flight, on call, and even on license plate.
SELECT name FROM people
     JOIN bank_accounts
     ON people.id = bank_accounts.person_id
         JOIN atm_transactions
         ON bank_accounts.account_number = atm_transactions.account_number
            WHERE atm_location IS 'Leggett Street'
               AND transaction_type IS 'withdraw'
                  AND year IS 2021
                  AND month IS 7
                  AND day IS 28

INTERSECT

SELECT name FROM people
     JOIN passengers
     ON people.passport_number = passengers.passport_number
     JOIN flights
     ON passengers.flight_id = flights.id
  WHERE flights.year IS 2021
     AND flights.month IS 7
     AND flights.day IS 29
     AND flights.hour IS 8
     AND flights.minute IS 20

INTERSECT

SELECT name FROM people
     JOIN phone_calls
     ON people.phone_number = phone_calls.caller
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
       AND duration < 60

INTERSECT

SELECT name FROM people
    JOIN bakery_security_logs
    ON people.license_plate = bakery_security_logs.license_plate
  WHERE bakery_security_logs.year IS 2021
     AND bakery_security_logs.month IS 7
     AND bakery_security_logs.day IS 28
     AND bakery_security_logs.hour IS 10
     AND bakery_security_logs.minute > 15
     AND bakery_security_logs.minute < 25;    -- Bruce name came up in all cross-references.

-- Lets check who bruce talked to during call, we'll take recievers number and check the name of same
SELECT * FROM people
     JOIN phone_calls
     ON people.phone_number = phone_calls.caller
       AND people.name LIKE 'Bruce'
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
       AND duration < 60;

SELECT name FROM people
  WHERE phone_number IS
    (SELECT receiver FROM people
     JOIN phone_calls
     ON people.phone_number = phone_calls.caller
       AND people.name LIKE 'Bruce'
  WHERE year IS 2021
     AND month IS 7
     AND day IS 28
       AND duration < 60);    -- Robin came up in this search.

-- New information just passes to me, that there is no record that thief accomplice did escape with them.
-- So, at last i can surely conclude that Bruce is the theif because his name came up more times than kenny's.
-- Kenny went new york with doris after talking to her, but in our case, accomplice didn't leave city.
-- Robin didn't escaped with Bruce, and Bruce was present in all evidences.

-- Thus my new and last conclution is Bruce is batman, i mean theif, and robin is his accomplice.
