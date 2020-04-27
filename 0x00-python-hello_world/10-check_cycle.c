#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @List: lista
 *
 * Return: 0 or 1
*/

int check_cycle(listint_t *list)
{
	 listint_t *tmpOne = list, *tmpTwo = list;

	 while (tmpOne && tmpTwo && tmpTwo->next)
	 {
		 tmpOne = tmpOne->next;
		 tmpTwo = tmpTwo->next->next;

		 if (tmpOne == tmpTwo)
			 return (1);
	 }
	 return (0);
}
