/* Write your PL/SQL query statement below */
SELECT firstName,lastName,city,state FROM
person P LEFT JOIN address A
ON P.personId=A.personId;