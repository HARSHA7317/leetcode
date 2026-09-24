/* Write your PL/SQL query statement below */
SELECT C.name AS customers FROM
customers C LEFT JOIN orders O
ON C.id=O.customerID
WHERE O.id is null;