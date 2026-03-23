SELECT p.firstName, p.lastName, a.city, a.state
from Person p
join on p.personId = a.personId;
