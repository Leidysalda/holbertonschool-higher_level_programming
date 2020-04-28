#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function in C that inserts a number into a sorted singly
 * linked list.
 * @head: pointer to head of list
 * @number: number
 * Return: listint_t
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *current = *head;

	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (NULL);

	tmp->n = number;
	tmp->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		tmp->next = *head;
		*head = tmp;
	}
	else
	{
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		tmp->next = current->next;
		current->next = tmp;
	}
	return (*head);
}
